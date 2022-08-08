import json
import os
import shutil
import zipfile

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

# 処理時間の計測 
import time
start = time.time()

student = {
    "name": "Suzuki",
    "age": 15,
    "gender": "male"
}



path = create_json_file(student)
create_zip([path])

# 処理時間　計測
end = time.time()
print(f'処理時間(秒)：{end-start}')



