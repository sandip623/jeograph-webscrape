import json 
from jg_webscraper import WebScraper, webscrape_extension
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from azure_bindings import StorageAccountConfig

keyword = "Pharmacist"
base_url = "https://www.reed.co.uk"
listings = WebScraper(base_url=base_url, keyword=keyword).scrape_jobs()
# convert to json str obj for data ingestion
listings_dto = json.dumps(listings)

# get azure config
config_instance = StorageAccountConfig()
config = config_instance.get_config()

# Azure Storage account details
#account_name = 'jeographstore001'
#account_key = 'Teyi0JFeE4G/tInDqC5Ykv2A/nIokl5pUx1MyxKJ2STo0wCi/SrCn1iS/SRoEoOye+gZ8iUrJL9z+AStKYxQVQ=='
#container_name = 'listingsdtoblobstore'
#blob_name = 'joblistingsdto.json'

# Authenticate to Azure Storage
blob_service_client = BlobServiceClient(account_url=f"https://{config['account_name']}.blob.core.windows.net", credential=config['account_key'])

# Get the container client
container_client = blob_service_client.get_container_client(config['container_name'])

# Create a blob client and upload JSON data
blob_client = container_client.get_blob_client(blob=config['blob_name'])
blob_client.upload_blob(listings_dto, overwrite=True)

print(f"listings_dto obj uploaded to Azure Blob Storage: {config['blob_name']}")

# TODO: setup oop blob config and initialiation w/ getter and setter for config class, async threading (likely daily than hourly due to cost incurrings)
#       maybe a more secure way to setup config on top of class encapsulation?