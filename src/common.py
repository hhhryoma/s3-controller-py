import json
import logging
import os
import shutil
import zipfile


def set_up():
    pass
    # dbのコレクションにDelete時のパラメーター設定がされているか
    # s3バケットがそんざいするか 
    

# Jsonのファイル出力とZip化
def create_json_file(dic):
    file_name = 'test.json'
    path = os.path.join(ret_exec_path(), 'tmp', file_name)
    with open(path, "w") as f:
        json.dump(dic, f)
    return path

def create_zip(file_names):
    zip_file_name = 'test.zip'
    path = os.path.join(ret_exec_path(), 'tmp', zip_file_name)
    with zipfile.ZipFile(path, mode='w') as archive:
        for file_name in file_names:
            archive.write(file_name)

def rm_file_in_tmp():
    path = os.path.join(ret_exec_path(), 'tmp')
    shutil.rmtree(path)
    os.mkdir(path)


def ret_exec_path():
    path = os.path.dirname(os.path.abspath(__file__))
    return path


# route_listからDict参照文を生成
def get_node_id(dict, route_list):
    route_str = ''
    for val in route_list:
        route_str += f'["{val}"]'
    node_id = eval(f'dict{route_str}')
    
    return node_id 
    
