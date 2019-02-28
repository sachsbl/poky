#!/usr/bin/env bash

# source config file
. ../aws.config

docker run \
    -e SOURCE_BUCKET='test-poky-input' \
    -e SOURCE_KEY='test_file.txt' \
    -e DESTINATION_BUCKET='test-poky-output' \
    -e AWS_DEFAULT_REGION=$AWS_DEFAULT_REGION \
    -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
    -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
    poky