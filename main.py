from jg_webscraper import WebScraper, webscrape_extension

keyword = "Data Scientist"
base_url = "https://www.reed.co.uk"
job_listings = WebScraper(base_url=base_url, keyword=keyword).scrape_jobs()
for job in job_listings:
    print(job)
