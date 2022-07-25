import module

bucket = "python-work"
key = "sample.zip"

file_name = "sample.zip"

module.upload_file(file_name=file_name, bucket=bucket, object_name=key)
module.get_object(bucket, key)