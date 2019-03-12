"""This file can be run stand-alone to start a Fargate task with default values"""

import pprint

import boto3

from poky_app.config.poky_app_config import ECSConfig


# AWS credentials are assumed to be present on local system
def run_fargate_task(source_bucket: str, source_key: str, output_bucket: str) -> dict:
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
                            'name': 'OUTPUT_BUCKET',
                            'value': output_bucket
                        },
                    ],
                },
            ],
            'taskRoleArn': ECSConfig.task_role,
            'executionRoleArn': ECSConfig.task_role
        },
    )
    return response


if __name__ == "__main__":
    from poky_app.config.poky_app_config import S3Config

    result = run_fargate_task(source_bucket=S3Config.input_bucket, source_key=S3Config.test_file,
                              output_bucket=S3Config.output_bucket)
    pprint.pprint(result)
