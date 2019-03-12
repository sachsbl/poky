"""Note that these test DO incur charges.  Mocks were avoided to keep it as simple as possible"""

from poky_app.poky_helpers import verify_s3_object, verify_s3_bucket


VALID_SOURCE_BUCKET = 'test-poky-input'
VALID_SOURCE_KEY = 'test_file.txt'


def test_verify_s3_object_exists_returns_true():
    result = verify_s3_object(bucket=VALID_SOURCE_BUCKET, key=VALID_SOURCE_KEY)

    assert result is True


def test_verify_s3_object_exists_bad_key_returns_false():
    result = verify_s3_object(bucket=VALID_SOURCE_BUCKET, key='bad_buck123')

    assert result is False


def test_verify_s3_object_exists_bad_bucket_returns_false():
    result = verify_s3_object(bucket='bad_buck123', key=VALID_SOURCE_KEY)

    assert result is False


def test_verify_s3_bucket_valid_bucket_returns_true():
    result = verify_s3_bucket(VALID_SOURCE_BUCKET)

    assert result is True


def test_verify_s3_bucket_invalid_bucket_returns_false():
    result = verify_s3_bucket('bad_buck123')

    assert result is False
