import hashlib
import zipfile
import io
import boto3
import botocore
import os

def upload_file(file_name, bucket, object_name=None):
    # s3へのファイルアップロード時のAPIとして1,upload_file/2.put_objectの2種類ある
    # 双方のAPIの仕様差異については右記参照（https://stackoverflow.com/questions/43739415/what-is-the-difference-between-file-upload-and-put-object-when-uploading-fil）

    if object_name is None:
        object_name = os.path.basename(file_name)

    # boto3.set_stream_logger()
    # botocore.session.Session().set_debug_logger()
    with open(ret_file_path(file_name), 'rb') as f:
        s3 = boto3.client('s3')
        response = s3.put_object(
            Body=f,
            Bucket=bucket,
            Key=object_name
        )

    print("\n--------------------- upload response ---------------------")
    print(response)
    print("--------------------- upload response ---------------------\n")

    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print(f'{file_name} upload Succcess')
    else:
        print('upload failed')


def get_object(bucket, key):    
    # S3バケットからファイルを取得、ファイル内容をコンソール出力

    s3 = boto3.client('s3')
    response = s3.get_object(
        Bucket=bucket,
        Key=key
    )
    
    print("\n--------------------- get object response ---------------------")
    print(response)
    print("--------------------- get object response ---------------------\n")
    
    obj = response['Body'].read()
    # メモリにZipファイルを保存
    zf = zipfile.ZipFile(io.BytesIO(obj))
    file = io.TextIOWrapper(zf.open(zf.namelist()[0], 'r'))
    
    print('get object content:')
    for row in file.readlines():
        print(row)
    get_hash('sha256', file)
    


def make_text_file(file_name):
    path = ret_file_path(file_name)
    f = open(path, 'w')
    f.write('auto generate')
    f.close()
    return path


def ret_file_path(file_name):
    base_path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_path, 'up', file_name)
    return path


def get_hash(algo, file):
    file_data = file.read()
    if algo == 'sha256':
        hash = hashlib.sha256(file_data.encode()).hexdigest() 
        # hash = hashlib.sha256(file_byte).hexdigest() 
    print(f'hash algo: {algo}   hash string: {hash}')
    return hash


def wrap_log_text(log_text, wrap_text):
    l = [wrap_text, log_text, wrap_text]
    return '\n'.join(l)