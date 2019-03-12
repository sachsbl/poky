# Run this file to test your Docker container locally.  You will need to build the image first (see build_docker.sh)

#!/usr/bin/env bash

# source config file
. aws_credentials.config

# params can be overridden here via ENV variables.  This is the method used for passing the parameters to the task.
docker run \
    -e SOURCE_BUCKET='test-poky-input' \
    -e SOURCE_KEY='test_file.txt' \
    -e OUTPUT_BUCKET='test-poky-output' \
    -e AWS_DEFAULT_REGION=$AWS_DEFAULT_REGION \
    -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
    -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
    poky