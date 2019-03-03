import boto3
import pprint
from configparser import ConfigParser


config = ConfigParser()
config.read('poky_config.ini')

cluster = config['ECS']['CLUSTER']
task_definition = config['ECS']['TASK_DEFINITION']
subnets = config['ECS']['subnets'].split(',')
task_role = config['ECS']['TASK_ROLE']
container_name = config['ECS']['CONTAINER_NAME']


# AWS credentials are assumed to be present on local system
def run_fargate_task(source_bucket='test-poky-input', source_key='test_file.txt',
                     destination_bucket='test-poky-output'):
    client = boto3.client('ecs')
    response = client.run_task(
        cluster=cluster,
        launchType='FARGATE',
        taskDefinition=task_definition,
        count=1,
        platformVersion='LATEST',
        networkConfiguration={
            'awsvpcConfiguration': {
                'subnets': subnets,
                'assignPublicIp': 'ENABLED'
            }
        },
        overrides={
            'containerOverrides': [
                {
                    'name': container_name,
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
            'taskRoleArn': task_role,
            'executionRoleArn': task_role
        },
    )
    return response


result = run_fargate_task()
pprint.pprint(result)
