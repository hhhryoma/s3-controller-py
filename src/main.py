from distutils.log import info
import module

bucket = "python-work"

for i in range(3):
    file_name = module.make_text_file("file_" + str(i))
    module.upload_file(file_name=file_name, bucket=bucket, object_name=None)