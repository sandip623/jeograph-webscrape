import requests
from bs4 import BeautifulSoup
from .webscrape_extension import AddJobToList

class WebScraper:
    def __init__(self, base_url, keyword):
        self.base_url = str(base_url) 
        self.key_word = str(keyword).replace(' ','-')
        self.url = f"{base_url}/jobs/{keyword}"

    def fetch_html(self):
        try: 
            response = requests.get(self.url)
            if (response.status_code == 200):
                return response.text
        except Exception:
            return f'Something went wrong WebScraper.fetch_html: {Exception}'
    
    def scrape_jobs(self):
        try:
            html_content = self.fetch_html()
            if html_content:
                 soup = BeautifulSoup(html_content, 'html.parser')
                 # get a set of all job cards
                 jobs = soup.find_all('div', 'col-sm-12 col-md-7 col-lg-8 col-xl-9')
                 job_list = AddJobToList(jobs, self.base_url).getJobList()
                 return job_list 
        except Exception:
            return f'Something went wrong WebScraper.scrape_jobs: {Exception}'