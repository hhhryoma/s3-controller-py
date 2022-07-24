import boto3
import os

def upload_file(file_name, bucket, object_name=None):
    """ s3へのファイルアップロード時のAPIとして1,upload_file/2.put_objectの2種類ある
        双方のAPIの仕様差異については右記参照（https://stackoverflow.com/questions/43739415/what-is-the-difference-between-file-upload-and-put-object-when-uploading-fil）
    Args:
        file_name (_type_): _description_
        bucket (_type_): _description_
        object_name (_type_, optional): _description_. Defaults to None.
    """
    if object_name is None:
        object_name = os.path.basename(file_name)

    # boto3.set_stream_logger()
    # botocore.session.Session().set_debug_logger()
    with open(file_name, 'rb') as f:
        s3 = boto3.client('s3')
        response = s3.put_object(
            Body=f,
            Bucket=bucket,
            Key=object_name
        )
    print(response)
    return response['ResponseMetadata']['HTTPStatusCode'] == 200
    
    

def make_text_file(file_name):
    base_path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_path, "up", file_name)
    print(os.curdir)
    f = open(path, 'w')
    f.write('auto generate')
    f.close()
    return path

