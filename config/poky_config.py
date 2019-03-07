from pathlib import Path
from configparser import ConfigParser

config_file = Path(__file__).parent.joinpath('poky_config.ini').resolve()
config = ConfigParser()
config.read(config_file)


class ECSConfig:
    cluster = config['ECS']['CLUSTER']
    task_definition = config['ECS']['TASK_DEFINITION']
    subnets = config['ECS']['subnets'].split(',')
    task_role = config['ECS']['TASK_ROLE']
    container_name = config['ECS']['CONTAINER_NAME']
