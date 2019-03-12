from pathlib import Path
from configparser import ConfigParser

config_file = Path(__file__).parent.joinpath('poky_app_config.ini').resolve()
config = ConfigParser()
config.read(config_file)


class ECSConfig:
    cluster = config['ECS']['CLUSTER']
    task_definition = config['ECS']['TASK_DEFINITION']
    subnets = config['ECS']['subnets'].split(',')
    task_role = config['ECS']['TASK_ROLE']
    container_name = config['ECS']['CONTAINER_NAME']


# used for local testing only, in real-life these are parameters
class S3Config:
    input_bucket = config['S3']['INPUT_BUCKET']
    output_bucket = config['S3']['OUTPUT_BUCKET']
    test_file = config['S3']['TEST_FILE']
