"""This file can be run stand-alone to start a Fargate task with default values"""

import pprint

import boto3

from config.poky_config import ECSConfig


# AWS credentials are assumed to be present on local system
def run_fargate_task(source_bucket: str, source_key: str, destination_bucket: str) -> dict:
    client = boto3.client('ecs')
    response = client.run_task(
        cluster=ECSConfig.cluster,
        launchType='FARGATE',
        taskDefinition=ECSConfig.task_definition,
        count=1,
        platformVersion='LATEST',
        networkConfiguration={
            'awsvpcConfiguration': {
                'subnets': ECSConfig.subnets,
                'assignPublicIp': 'ENABLED'
            }
        },
        overrides={
            'containerOverrides': [
                {
                    'name': ECSConfig.container_name,
                    # Parameterization happens here by overriding the ENV variables.  Modify these to suit your needs.
                    'environment': [
                        {
                            'name': 'SOURCE_BUCKET',
                            'value': source_bucket
                        },
                        {
                            'name': 'SOURCE_KEY',
                            'value': source_key
                        },
                        {
                            'name': 'DESTINATION_BUCKET',
                            'value': destination_bucket
                        },
                    ],
                },
            ],
            'taskRoleArn': ECSConfig.task_role,
            'executionRoleArn': ECSConfig.task_role
        },
    )
    return response


result = run_fargate_task(source_bucket='test-poky-input', source_key='test_file.txt',
                          destination_bucket='test-poky-output')
pprint.pprint(result)
