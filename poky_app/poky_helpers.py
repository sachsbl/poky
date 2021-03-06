import boto3
from botocore.exceptions import ClientError


def verify_s3_object(bucket: str, key: str) -> bool:
    session = boto3.session.Session()
    s3 = session.client('s3')

    try:
        response = s3.list_objects_v2(
            Bucket=bucket,
            Prefix=key,
        )
        for obj in response.get('Contents', []):
            if obj['Key'] == key:
                return True
    except ClientError:
        return False

    return False


def verify_s3_bucket(bucket: str) -> bool:
    s3 = boto3.resource('s3')

    if s3.Bucket(bucket) in s3.buckets.all():
        return True
    else:
        return False
