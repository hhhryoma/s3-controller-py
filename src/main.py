import logging
import data_sync
import db
 
LOG_LEVEL = 'DEBUG'
 
# フォーマットを指定 (https://docs.python.jp/3/library/logging.html#logrecord-attributes)
_detail_formatting = '%(asctime)s %(levelname)-8s [%(module)s#%(funcName)s %(lineno)d] %(message)s'
 
 
# ログをコンソールに送るハンドラconsoleを作成
logger = logging.StreamHandler()
logger.setLevel(getattr(logging, LOG_LEVEL)) # LOG_LEVEL_CONSOLE = 'INFO' なら logging.INFOを指定していることになる
formatter = logging.Formatter(_detail_formatting)
logger.setFormatter(formatter)

# ロガーを取得し、ハンドラを追加する
logger = logging.getLogger(__name__)
logger.addHandler(logger)
logging.getLogger("db").addHandler(logger)
logging.getLogger("data_sync").addHandler(logger)
 
 
def main():
    bucket = "python-work"
    key = "sample.zip"

    file_name = "sample.zip"
    data_sync_cols = ['test', 'team']
    client = db.MongoHandler('test')
    agent = data_sync.UpstreamSrc(data_sync_cols, client.db)
    agent.exec()
    
# module.upload_file(file_name=file_name, bucket=bucket, object_name=key)
# module.get_object(bucket, key)


if __name__ == '__main__':
    main()