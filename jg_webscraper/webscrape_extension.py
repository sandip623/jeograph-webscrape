class AddJobToList:
    def __init__(self, jobs, base_url):
        self.jobs = jobs
        self.base_url = base_url 

    def getJobList(self):
        self.job_list = []
        try:
            for job in self.jobs:
                job_dict = {
                    'job_title' : (job.header.h2.a).get('title'),
                    'job_link' : self.base_url+(job.header.h2.a).get('href'),
                    'job_by' : (job.find('a', 'gtmJobListingPostedBy')).text.strip(),
                    # when multiple elements share the same attributes and naming convention, we can use indexing to get a particular one
                    'job_location' : (job.find_all('li', class_='job-card_jobMetadata__item___QNud list-group-item'))[1].text.strip()
                }
                self.job_list.append(job_dict)
            return self.job_list
        except Exception:
            return Exception