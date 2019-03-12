"""Note that these test DO incur charges.  Mocks were avoided to keep it as simple as possible"""

import pytest

from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    return client


VALID_SOURCE_BUCKET = 'test-poky-input'
VALID_SOURCE_KEY = 'test_file.txt'
VALID_OUTPUT_BUCKET = 'test-poky-output'


def test_post_process_file_valid_request_returns_200_with_boto_response(client):
    response = client.post('/process_file',
                           data={'source_bucket': VALID_SOURCE_BUCKET,
                                 'source_key': VALID_SOURCE_KEY,
                                 'output_bucket': VALID_OUTPUT_BUCKET})

    assert response.status_code == 200
    assert response.json['tasks'][0]['launchType'] == 'FARGATE'


def test_post_process_file_valid_request_implements_env_container_overrides(client):
    response = client.post('/process_file',
                           data={'source_bucket': VALID_SOURCE_BUCKET,
                                 'source_key': VALID_SOURCE_KEY,
                                 'output_bucket': VALID_OUTPUT_BUCKET})

    assert response.json['tasks'][0]['overrides']['containerOverrides'][0]['environment'][0] == \
           {'name': 'SOURCE_BUCKET', 'value': VALID_SOURCE_BUCKET}
    assert response.json['tasks'][0]['overrides']['containerOverrides'][0]['environment'][1] == \
           {'name': 'SOURCE_KEY', 'value': VALID_SOURCE_KEY}
    assert response.json['tasks'][0]['overrides']['containerOverrides'][0]['environment'][2] == \
           {'name': 'OUTPUT_BUCKET', 'value': VALID_OUTPUT_BUCKET}


def test_post_process_file_invalid_source_bucket_returns_400(client):
    response = client.post('/process_file',
                           data={'source_bucket': 'bad_baby',
                                 'source_key': VALID_SOURCE_KEY,
                                 'output_bucket': VALID_OUTPUT_BUCKET})

    assert response.status_code == 400
    assert 'The source bucket provided does not exist, or you do not have permissions to access it' in response.json


def test_post_process_file_invalid_source_key_returns_400(client):
    response = client.post('/process_file',
                           data={'source_bucket': VALID_SOURCE_BUCKET,
                                 'source_key': 'bad',
                                 'output_bucket': VALID_OUTPUT_BUCKET})

    assert response.status_code == 400
    assert 'The source key provided does not exist, or you do not have permissions to access it' in response.json


def test_post_process_file_invalid_output_bucket_returns_400(client):
    response = client.post('/process_file',
                           data={'source_bucket': VALID_SOURCE_BUCKET,
                                 'source_key': VALID_SOURCE_KEY,
                                 'output_bucket': 'bad'})

    assert response.status_code == 400
    assert 'The output bucket provided does not exist,' \
           ' or you do not have permissions to access it' in response.json


def test_post_process_file_no_params_returns_400_with_message(client):
    response = client.post('/process_file')

    assert response.status_code == 400
    assert 'Missing required field' in response.json


def test_post_process_file_one_param_returns_400_with_message(client):
    response = client.post('/process_file', data={'source_bucket': VALID_SOURCE_BUCKET})

    assert response.status_code == 400
    assert 'Missing required field' in response.json


def test_simple_post_root_index_returns_404(client):
    response = client.post('/')
    assert response.status_code == 404
