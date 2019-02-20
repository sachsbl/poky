# poky
Running annoyingly slow processes in the Cloud using Python, Serverless, and AWS Fargate

Merriam-Webster defines "poky" as "annoyingly slow or dull".  Poky accepts the slow, but rejects the dull! It uses AWS Fargate to orchestrate long-running processes coded in Python.  The setup and deployment is orchestrated using the Serverless framework.  The goal is a clone-and-go project to perform some long-running process on a file, with the transformed file as an output.  The base project uses image processing as the template, but can be customized easily.  

Inspired by the blog post and examples at:
https://serverless.com/blog/serverless-application-for-long-running-process-fargate-lambda/

Fargate FAQ:
https://aws.amazon.com/fargate/faqs/

Serverless Info:
https://serverless.com/

