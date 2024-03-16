# nb : all azure resources have been deleted to stop charges incurring
# nb : related microservices have been built with reproducability in mind (so only requires slight config tweaks and a cloud re-setup for a full restart)

![Alt text](jeo%20webscrape%20ingestion%20pipeline.jpeg)

microservice to the webapp (add Dockerfile)

pip install -r requirements.txt

project source - https://sandipgurung.atlassian.net/jira/software/projects/KAN/boards/1

based on source reed.co.uk 

azure resource group - dev-jeograph

blob storage -> azure data factory (copy, source, sink, schema, debug) -> azure sql db
serverName - jeographsqlserverauth.database.windows.net
db - jeographserverauthdb
schema - jeographserverauthsink

data factory config repo (private) - https://github.com/sandip623/jeograph-datafactory
