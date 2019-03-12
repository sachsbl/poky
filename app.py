from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequestKeyError

from poky_app.run_fargate_task import run_fargate_task
from poky_app.poky_helpers import verify_s3_bucket, verify_s3_object


app = Flask(__name__)


@app.route('/process_file', methods=['POST'])
def process_file():
    required_fields = ['source_bucket', 'source_key', 'output_bucket']

    try:
        source_bucket = request.values['source_bucket']
        source_key = request.values['source_key']
        output_bucket = request.values['output_bucket']
    except BadRequestKeyError:
        return jsonify(f'Missing required field.  Required fields are {required_fields}'), 400

    if not verify_s3_bucket(source_bucket):
        return jsonify(f'The source bucket provided does not exist, or you do not have permissions to access it'), 400
    if not verify_s3_object(source_bucket, source_key):
        return jsonify(f'The source key provided does not exist, or you do not have permissions to access it'), 400
    if not verify_s3_bucket(output_bucket):
        return jsonify(f'The output bucket provided does not exist, '
                       f'or you do not have permissions to access it'), 400

    boto_response = run_fargate_task(source_bucket, source_key, output_bucket)
    return jsonify(boto_response)


if __name__ == '__main__':
    app.run()
