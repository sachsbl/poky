"""Note that these test DO incur charges.  Mocks were avoided to keep it as simple as possible"""

import pytest

from poky_api import poky_api


@pytest.fixture
def client():
    poky_api.config['TESTING'] = True
    client = poky_api.test_client()

    return client


VALID_SOURCE_BUCKET = 'test-poky-input'
VALID_SOURCE_KEY = 'test_file.txt'
VALID_DESTINATION_BUCKET = 'test-poky-output'


def test_post_process_file_valid_request_returns_200_with_boto_response(client):
    response = client.post('/process_file',
                           data={'source_bucket': VALID_SOURCE_BUCKET,
                                 'source_key': VALID_SOURCE_KEY,
                                 'destination_bucket': VALID_DESTINATION_BUCKET})

    assert response.status_code == 200
    assert response.json['tasks'][0]['launchType'] == 'FARGATE'


def test_post_process_file_invalid_source_bucket_returns_400(client):
    response = client.post('/process_file',
                           data={'source_bucket': 'bad_baby',
                                 'source_key': VALID_SOURCE_KEY,
                                 'destination_bucket': VALID_DESTINATION_BUCKET})

    assert response.status_code == 400
    assert 'The source bucket provided does not exist, or you do not have permissions to access it' in response.json


def test_post_process_file_invalid_source_key_returns_400(client):
    response = client.post('/process_file',
                           data={'source_bucket': VALID_SOURCE_BUCKET,
                                 'source_key': 'bad',
                                 'destination_bucket': VALID_DESTINATION_BUCKET})

    assert response.status_code == 400
    assert 'The source key provided does not exist, or you do not have permissions to access it' in response.json


def test_post_process_file_invalid_destination_bucket_returns_400(client):
    response = client.post('/process_file',
                           data={'source_bucket': VALID_SOURCE_BUCKET,
                                 'source_key': VALID_SOURCE_KEY,
                                 'destination_bucket': 'bad'})

    assert response.status_code == 400
    assert 'The destination bucket provided does not exist,' \
           ' or you do not have permissions to access it' in response.json


def test_post_process_file_no_params_returns_400_with_fields_list(client):
    response = client.post('/process_file')

    assert response.status_code == 400
    assert 'Missing required field.  Required fields are ["source_bucket", ' \
           '"source_key", "destination_bucket"]' in response.json


def test_post_process_file_one_param_returns_400_with_fields_list(client):
    response = client.post('/process_file', data={'source_bucket': VALID_SOURCE_BUCKET})

    assert response.status_code == 400
    assert 'Missing required field.  Required fields are ["source_bucket", ' \
           '"source_key", "destination_bucket"]' in response.json


def test_simple_post_root_index_returns_404(client):
    response = client.post('/')
    assert response.status_code == 404
