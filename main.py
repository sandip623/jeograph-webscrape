from bs4 import BeautifulSoup
import requests 

keyword = "Data-Scientist"
base_url = f"https://www.reed.co.uk"
url = f"https://www.reed.co.uk/jobs/{keyword.replace(' ', '-')}"

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

