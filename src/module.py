import logging
from botocore.exceptions import ClientError
import boto3
import botocore
import os

def upload_file(file_name, bucket, object_name=None):
    """_summary_

    Args:
        file_name (_type_): _description_
        bucket (_type_): _description_
        object_name (_type_, optional): _description_. Defaults to None.
    """
    if object_name is None:
        object_name = os.path.basename(file_name)

    
    boto3.set_stream_logger()
    botocore.session.Session().set_debug_logger()

    
    s3_client = boto3.client('s3')
    
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
    

def make_text_file(file_name):
    base_path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_path, "up", file_name)
    print(os.curdir)
    f = open(path, 'w')
    f.write('auto generate')
    f.close()
    return path

