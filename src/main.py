import module

bucket = "python-work"

for i in range(3):
    file_name = module.make_text_file("file_" + str(i))
    result = module.upload_file(file_name=file_name, bucket=bucket, object_name=None)
    if result:
        print(f'{file_name} upload Succcess')
    else:
        print('upload failed')