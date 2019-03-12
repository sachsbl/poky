import os
import uuid

import boto3

if 'SOURCE_BUCKET' in os.environ:
    source_bucket = os.environ['SOURCE_BUCKET']
else:
    source_bucket = 'test-poky-input'

if 'SOURCE_KEY' in os.environ:
    source_key = os.environ['SOURCE_KEY']
else:
    source_key = 'test_file.txt'

if 'OUTPUT_BUCKET' in os.environ:
    output_bucket = os.environ['OUTPUT_BUCKET']
else:
    output_bucket = 'test-poky-output'

# rename with unique key
output_key = source_key.split('.')[0] + f"_{uuid.uuid4()}." + source_key.split('.')[1]

s3 = boto3.resource('s3')

copy_source = {
      'Bucket': source_bucket,
      'Key': source_key
    }
bucket = s3.Bucket(output_bucket)

print(f"Copying {source_key} from s3 bucket {source_bucket} to s3 bucket {output_bucket}.  "
      f"New name: {output_key}")
bucket.copy(copy_source, output_key)
print("Completed")
