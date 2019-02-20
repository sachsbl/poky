# poky
Running annoyingly slow processes in the Cloud using Python, Serverless, and AWS Fargate

Merriam-Webster defines "poky" as "annoyingly slow or dull".  This projects accepts the slow, but rejects the dull! Poky uses AWS Fargate to orchestrate long-running processes coded in Python.  The setup and deployment is orchestrated using the Serverless framework.  The goal is a clone-and-go project to perform some long-running process on some data.  The base project uses image processing as the template, but can be customized easily.  Inspired by the blog post and examples at:

https://serverless.com/blog/serverless-application-for-long-running-process-fargate-lambda/

