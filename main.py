import asyncio
import json 
import datetime 
from jg_webscraper import WebScraper, webscrape_extension
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from azure_bindings import StorageAccountConfig
from extension_functions import calculate_target_time_offset, notify

def scrape(keyword):
    base_url = "https://www.reed.co.uk"
    listings = WebScraper(base_url=base_url, keyword=keyword).scrape_jobs()
    return json.dumps(listings)

async def schedule_blob_task():
        try:
            _config = StorageAccountConfig().get_config()
            _delay = calculate_target_time_offset(17, 00)
            _blob_service_client = BlobServiceClient(account_url=f"https://{_config['account_name']}.blob.core.windows.net", credential=_config['account_key'])
            _container_client = _blob_service_client.get_container_client(_config['container_name'])
            _blob_client = _container_client.get_blob_client(blob=_config['blob_name'])
            while True:
                await asyncio.sleep(_delay)
                _listings = scrape("Data Scientist")
                _blob_client.upload_blob(_listings, overwrite=True)
                notify()
        except Exception:
            return f"Something went wrong at schedule_blob_task() : {Exception}"

asyncio.run(schedule_blob_task())