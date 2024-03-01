import json 
from jg_webscraper import WebScraper, webscrape_extension
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from azure_bindings import StorageAccountConfig

keyword = "Pharmacist"
base_url = "https://www.reed.co.uk"
listings = WebScraper(base_url=base_url, keyword=keyword).scrape_jobs()
# convert to json str obj for data ingestion
listings_dto = json.dumps(listings)

# Azure Storage account details
account_name = 'jeographstore001'
account_key = 'Teyi0JFeE4G/tInDqC5Ykv2A/nIokl5pUx1MyxKJ2STo0wCi/SrCn1iS/SRoEoOye+gZ8iUrJL9z+AStKYxQVQ=='
container_name = 'listingsdtoblobstore'
blob_name = 'joblistingsdto.json'

azConfig = StorageAccountConfig.get_config
print(azConfig)

# Authenticate to Azure Storage
blob_service_client = BlobServiceClient(account_url=f"https://{account_name}.blob.core.windows.net", credential=account_key)

# Get the container client
container_client = blob_service_client.get_container_client(container_name)

# Create a blob client and upload JSON data
blob_client = container_client.get_blob_client(blob=blob_name)
# blob_client.upload_blob(listings_dto, overwrite=True)

print(f"listings_dto obj uploaded to Azure Blob Storage: {blob_name}")

# TODO: setup oop blob config and initialiation w/ getter and setter for config class, async threading (likely daily than hourly due to cost incurrings)
#       maybe a more secure way to setup config on top of class encapsulation?