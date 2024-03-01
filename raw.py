from bs4 import BeautifulSoup
import requests 
import json 
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

keyword = "Data-Scientist"
base_url = "https://www.reed.co.uk"
url = f"https://www.reed.co.uk/jobs/{keyword.replace(' ', '-')}"
url = f"{base_url}/jobs/{keyword.replace(' ', '-')}"
response = requests.get(url) 

# parse html content
soup = BeautifulSoup(response.text, 'html.parser')

# gets a set of all job cards
cards = soup.find_all('div', 'col-sm-12 col-md-7 col-lg-8 col-xl-9')

# prototype the model with a single record
card = cards[0]

job_title = (card.header.h2.a).get('title')
job_link = (card.header.h2.a).get('href')
job_by = (card.find('a', 'gtmJobListingPostedBy')).text.strip()
# when multiple elements share the same attributes and naming convention, we can use indexing to get a particular one
job_location = (card.find_all('li', class_='job-card_jobMetadata__item___QNud list-group-item'))[1].text

for card in cards:
    job_title = (card.header.h2.a).get('title')
    job_link = base_url+(card.header.h2.a).get('href')
    job_by = (card.find('a', 'gtmJobListingPostedBy')).text.strip()
    # when multiple elements share the same attributes and naming convention, we can use indexing to get a particular one
    job_location = (card.find_all('li', class_='job-card_jobMetadata__item___QNud list-group-item'))[1].text.strip()
    print(job_title, job_link, job_by, job_location)
    print("\n\n")


listings_dto = json.dumps(job_location)


# Azure Storage account details
account_name = 'jeographstore001'
account_key = 'Teyi0JFeE4G/tInDqC5Ykv2A/nIokl5pUx1MyxKJ2STo0wCi/SrCn1iS/SRoEoOye+gZ8iUrJL9z+AStKYxQVQ=='
container_name = 'listingsdtoblobstore'
blob_name = 'joblistingsdto.json'

# Authenticate to Azure Storage
blob_service_client = BlobServiceClient(account_url=f"https://{account_name}.blob.core.windows.net", credential=account_key)

# Get the container client
container_client = blob_service_client.get_container_client(container_name)

# Create a blob client and upload JSON data
blob_client = container_client.get_blob_client(blob=blob_name)
blob_client.upload_blob(listings_dto, overwrite=True)

print(f"listings_dto obj uploaded to Azure Blob Storage: {blob_name}")

# TODO: setup oop blob config and initialiation w/ getter and setter for config class, async threading (likely daily than hourly due to cost incurrings)