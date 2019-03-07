import json

from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequestKeyError

from run_fargate_task import run_fargate_task
from poky_helpers import verify_s3_bucket, verify_s3_object


poky_api = Flask(__name__)


@poky_api.route('/process_file', methods=['POST'])
def process_file():
    required_fields = ['source_bucket', 'source_key', 'destination_bucket']

    try:
        source_bucket = request.values['source_bucket']
        source_key = request.values['source_key']
        destination_bucket = request.values['destination_bucket']
    except BadRequestKeyError:
        return jsonify(f'Missing required field.  Required fields are {json.dumps(required_fields)}'), 400

    if not verify_s3_bucket(source_bucket):
        return jsonify(f'The source bucket provided does not exist, or you do not have permissions to access it'), 400
    if not verify_s3_object(source_bucket, source_key):
        return jsonify(f'The source key provided does not exist, or you do not have permissions to access it'), 400
    if not verify_s3_bucket(destination_bucket):
        return jsonify(f'The destination bucket provided does not exist, '
                       f'or you do not have permissions to access it'), 400

    boto_response = run_fargate_task(source_bucket, source_key, destination_bucket)
    return jsonify(boto_response)

