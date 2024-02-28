from bs4 import BeautifulSoup
import requests 

class AddJobToList:
    def __init__(self, jobs):
        self.jobs = jobs

    def getJobList(self):
        print(type(self.jobs))
        print(self.jobs[0])
        self.job_list = []
        for job in self.jobs:
            job_dict = {
                'job_title' : (job.header.h2.a).get('title')
            }
            self.job_list.append(job_dict)
        return self.job_list

url = "https://www.reed.co.uk/jobs/Data-Scientist"

response = requests.get(url) 

# parse html content
soup = BeautifulSoup(response.text, 'html.parser')

# gets a set of all job cards
cards = soup.find_all('div', 'col-sm-12 col-md-7 col-lg-8 col-xl-9')

obj = AddJobToList(cards)

job_titles = obj.getJobList()

print(job_titles)

del obj
del job_titles

print(job_titles)