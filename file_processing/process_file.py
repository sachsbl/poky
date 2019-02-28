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

if 'DESTINATION_BUCKET' in os.environ:
    destination_bucket = os.environ['DESTINATION_BUCKET']
else:
    destination_bucket = 'test-poky-output'

# rename with unique key
destination_key = source_key.split('.')[0] + f"_{uuid.uuid4()}." + source_key.split('.')[1]

s3 = boto3.resource('s3')

copy_source = {
      'Bucket': source_bucket,
      'Key': source_key
    }
bucket = s3.Bucket(destination_bucket)

print(f"Copying {source_key} from s3 bucket {source_bucket} to s3 bucket {destination_bucket}.  "
      f"New name: {destination_key}")
bucket.copy(copy_source, destination_key)
print("Completed")
