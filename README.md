# poky
Running annoyingly slow processes in the Cloud using Python, Serverless, and AWS Fargate

Merriam-Webster defines "poky" as "annoyingly slow or dull".  Poky accepts the slowness, but tries to offload some of the dullness to the cloud.  It uses AWS Fargate to orchestrate long-running processes coded in Python.  The setup and deployment is handled using the Serverless framework.  The base project uses image processing as the task performed, but could be customized easily to suit other purposes.  

Inspired by the blog post and examples at:
https://serverless.com/blog/serverless-application-for-long-running-process-fargate-lambda/

Fargate FAQ:
https://aws.amazon.com/fargate/faqs/

Serverless Info:
https://serverless.com/

Good Python in Docker Tutorial:
https://www.wintellect.com/containerize-python-app-5-minutes/

