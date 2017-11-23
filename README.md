# AWS Lambda & Cloud watch

## Terms:
- event driven
- Trigger
- scalability
- parallel executions
- serverless 
- There are some “hard limitations” for the runtime environment: the disk space is limited to 512 MB,
- 15 mins 
- First 1M requests / monthFree & First 400K GB-sec / monthFree

## User cases:
http://docs.aws.amazon.com/lambda/latest/dg/use-cases.html

website with api gateway
Processing uploaded S3 objects
Bulk api calling based on csv
monitoring & Security Alerts
crons / Scheduled events 
event-based triggers to help automate the encoding process of media files
validation of backup completions 
Log analysis on the fly
build your own event sources using custom apps



## 1) Processing uploaded S3 objects (async model)
http://docs.aws.amazon.com/lambda/latest/dg/with-s3.html
In Orchard we have eg of: 
- Bulk api calling based on csv
- Asset uplaod making DB entries to queue it for rbencoder
- lovelive sync assets to lovelice AWS server and zen encoders 


## 2) monitoring & Security Alerts , crons / Scheduled events 
http://docs.aws.amazon.com/lambda/latest/dg/vpc-rds-deployment-pkg.html
http://docs.aws.amazon.com/lambda/latest/dg/with-scheduledevents-example.html

In Orchard we have eg of: 
- Data alert for ETL feeds 
- crons to generate some reports
- regular send some data exports
- regularly trigger an SWF to ingest data 

## 3) Website / Microservice:
http://docs.aws.amazon.com/lambda/latest/dg/with-on-demand-https-example.html


## 4) build your own event sources using custom apps
http://docs.aws.amazon.com/lambda/latest/dg/with-userapp-walkthrough-custom-events.html
https://github.com/boto/boto3/issues/885#issuecomment-308296242



