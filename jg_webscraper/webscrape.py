import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url):
        self.url = url

    def fetch_html(self):
        try: 
            response = requests.get(self.url)
            if (response.status_code == 200):
                return response.text
        except Exception:
            return Exception
    
    def scrape_jobs(self):
        try:
            html_content = self.fetch_html()
            
        except:
            pass 