Poky
=======
Running annoyingly slow processes in the Cloud using Python, Serverless, and AWS Fargate

Merriam-Webster defines "poky" as "annoyingly slow or dull".  
Poky accepts the slowness, but tries to offload some of the dullness to the cloud.  
It uses AWS Fargate to orchestrate long-running processes coded in Python.  
The setup and deployment is handled using the Serverless framework. 
The goal is a simple, standardized workflow for long-running tasks that process files using parameters.  
The process can be run on-demand, with no charges incurred when not actually processing files.   

Inspired by the blog post and examples at:
https://serverless.com/blog/serverless-application-for-long-running-process-fargate-lambda/

Fargate FAQ:
https://aws.amazon.com/fargate/faqs/

Serverless Info:
https://serverless.com/

Good Python in Docker Tutorial:
https://www.wintellect.com/containerize-python-app-5-minutes/

Flask and Serverless together:
https://serverless.com/blog/flask-python-rest-api-serverless-lambda-dynamodb/



Workflow
-----
1.  Files are uploaded to the input s3 bucket
2.  An AWS Lambda function is triggered to process the file.  
    Base app simply logs the upload, but this could initiate processing if parameters are not needed.
3.  When ready, a REST API is called to initiate the processing.  Parameters for the processing can be supplied here.
4.  An AWS Fargate process is spawned for each task. 
5.  Result files are moved to the output s3 bucket.
6.  Another Lambda is triggered via s3 event.  Base app simply logs the output file creation.  

Notes:  Input files are never modified.  For example purposes, Poky simply renames and copies the input files.

Obviously there are a lot of ways to design a workflow like this.  
Poky aims to be as simple as possible, while allowing for both parameterization and extensibility.  
Additional desired functionality can be added to the processing logic without major changes to Poky itself.  