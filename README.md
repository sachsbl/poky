Poky
=======
Running annoyingly slow processes in the Cloud using Python, Zappa, and AWS Fargate.

Merriam-Webster defines "poky" as "annoyingly slow or dull".  
Poky accepts the slowness, but tries to offload some of the dullness to the cloud. It uses Python and AWS Fargate to 
orchestrate long-running processes in an on-demand fashion with no permanent infrastructure.  This is an example project
intended to get you going quickly with this workflow.   

Goals
-----
Minimalist application for running 'poky' tasks that process things using parameters.  
Can be run on-demand, with no charges incurred when not actually processing something.  
Provides a simple, testable REST API to initiate processing and provide parameters.

Fargate FAQ:
https://aws.amazon.com/fargate/faqs/

Zappa:
https://github.com/Miserlou/Zappa

Why Python, Zappa, and Fargate?
-----
Python: Because Python is just the best. ;)

Zappa: Zappa is the most mature pure-Python framework for deploying "serverless" apps. It works on multiple clouds, 
and it supports Flask.

Fargate: This is the best/only current option for easily running tasks longer than 15min (AWS Lambda limitation) with no 
permanent infrastructure. 

Workflow
-----
1.  Files are uploaded to the input s3 bucket
2.  When ready, a REST API is called to initiate the processing.  Parameters for the processing can be supplied here.
3.  An AWS Fargate process is spawned for each task (one API call == one task). 
4.  Result files are moved to the output s3 bucket.

Behind the scenes
-----
A Flask app is deployed as an AWS Lambda using Zappa.  It can also be run locally.  The Fargate process is simply a 
Docker container running on AWS ECS.  Poky provides an example Docker container, but any can be used.   

Obviously there are a lot of ways to design a workflow like this, and a lot of niceties not included here.  
Poky aims to be as simple as possible, while allowing for both parameterization and extensibility.  
The example app simply copies and renames a file between s3 buckets.
The sample processing logic can be replaced without major changes to framework.  

Prerequisites
-----
Poky assumes you have an AWS account and specifically an AWS Fargate task you can initiate via the AWS API.  
We provide an example Docker container that copies/renames a test file between S3 buckets.  This can be used to create
a Fargate task.  The demo app requires two s3 buckets and the proper IAM credentials.  To demo this app, it is assumed 
that all these AWS dependencies are in place.  Basic knowledge of Docker is assumed, see the Docker docs for a good 
tutorial (https://docs.docker.com).  

Tests
-----
Automated tests can used to verify functionality of the example app.  Valid AWS dependencies required. 
These can be run with PyTest, which may need to be installed separately.  

Make sure the project's directory is part of your PYTHONPATH:

``` export PYTHONPATH="${PYTHONPATH}:/path/to/poky"```

Run the following from the root directory to run all tests:

```pytest test```

Setup and Deployment
-----
1.  Download the Poky Repo.
2.  Install requirements using pip install -r requirements.txt.  Install requirements_test.txt also if you want to run
the automated tests.
3.  Make sure you have AWS CLI installed and AWS credentials configured.
(https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
4.  Using the AWS Fargate "Get Started" tutorial and the examples in the file_processing folder, 
setup the simple Fargate task.  
5.  Create two buckets for testing.  Make sure your IAM role has full access to these (see blog post).
6.  Configure your S3 buckets and ECS values created above steps in config/poky_config.ini
7.  Run the automated tests to ensure everything is working.
8.  Test the running of the Fargate task with run_fargate_task.py.  This requires an aws_credentials.config file in the 
file_processing folder.
9.  Deploy the Flask REST app in poky_app.app.  See Flask Github/Tutorial (https://github.com/pallets/flask).
10. If desired, test REST app locally using Postman or similar.
11. Setup Zappa and deploy Zappa app.  See https://github.com/Miserlou/Zappa
12. Create a Policy in AWS IAM that allows ecs:RunTask and iam:PassRole and attach it to the Zappa-created IAM role


Tips
-----
This will help get you started with Fargate:
https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_GetStarted.html

A few oddities not covered:
1.  Service needs to be set to 0 "desired tasks" if you want on-demand execution only.  Otherwise it will keep running all
the time!
2.  Consider hosting your container in AWS ECR, as I saw issues with pulling from DockerHub


Issues:
-----
1.  Currently depends on Python 3.7 compliant Zappa from https://github.com/purificant/Zappa.git@py37
2.  Needs automated method for adding IAM roles