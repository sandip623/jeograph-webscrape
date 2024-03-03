import asyncio
import json 
from jg_webscraper import WebScraper
from azure.storage.blob import BlobServiceClient
from azure_bindings import StorageAccountConfig
from extension_functions import calculate_target_time_offset, notify, LatLong
from gcp_bindings import ApiServiceKeys

def scrape(keyword):
    base_url = "https://www.reed.co.uk"
    listings = WebScraper(base_url=base_url, keyword=keyword).scrape_jobs()
    return listings

async def schedule_blob_task():
        try:
            _config = StorageAccountConfig().get_config()
            _delay = calculate_target_time_offset(17, 00)
            _blob_service_client = BlobServiceClient(account_url=f"https://{_config['account_name']}.blob.core.windows.net", credential=_config['account_key'])
            _container_client = _blob_service_client.get_container_client(_config['container_name'])
            _blob_client = _container_client.get_blob_client(blob=_config['blob_name'])
            while True:
                await asyncio.sleep(_delay)
                _listings = json.dumps(LatLong(scrape("Data Scientist"), ApiServiceKeys().get_service_key()['googlemaps']).get_latlng())
                _blob_client.upload_blob(_listings, overwrite=True)
                notify()
        except Exception:
            return f"Something went wrong at schedule_blob_task() : {Exception}"

asyncio.run(schedule_blob_task())