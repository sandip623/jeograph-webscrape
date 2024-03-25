- nb : all azure resources have been deleted to stop charges incurring
- nb : related microservices have been built with reproducability in mind (so only requires slight config tweaks and a cloud re-setup for a full restart)

# objectives
- visually informative approach via mapping job search query results immediately
- leveraging the use of cloud platform to automate data integration and app deployment cost-effectively

![Alt text](jeo%20webscrape%20ingestion%20pipeline.jpeg)

- the above flow diagram depicts how the raw data is to be ingested and processed within the system, including integration via the cloud for further servicing...

- note: this is a microservice delegate to the microservice webmap app (see https://github.com/sandip623/jeograph-webmap) 


----------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------
additional developer notes (can be ignored by readers):
pip install -r requirements.txt

project source - https://sandipgurung.atlassian.net/jira/software/projects/KAN/boards/1

based on source reed.co.uk 

azure resource group - dev-jeograph

blob storage -> azure data factory (copy, source, sink, schema, debug) -> azure sql db
serverName - jeographsqlserverauth.database.windows.net
db - jeographserverauthdb
schema - jeographserverauthsink

data factory config repo (private) - https://github.com/sandip623/jeograph-datafactory
