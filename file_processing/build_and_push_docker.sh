# use this example script to push to DockerHub (or perhaps AWS ECR)

#!/usr/bin/env bash

docker login
docker build -t poky .
docker tag poky sachsbl/poky:latest
docker push sachsbl/poky:latest

# Consider using AWS ECR, example syntax below but AWS has good information in the ECR docs.
$(aws ecr get-login --no-include-email --region us-east-1)
docker tag poky:latest 116226363472.dkr.ecr.us-east-1.amazonaws.com/poky:latest
docker push 116226363472.dkr.ecr.us-east-1.amazonaws.com/poky:latest

