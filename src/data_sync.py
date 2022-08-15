import dataclasses
import json
import logging
import os
from dataclasses import field
from time import sleep
from bson.json_util import dumps
from dataclasses_json import dataclass_json

import common
import db
import scheduler


logger = logging.getLogger(__name__)

@dataclass_json
@dataclasses.dataclass
class DataSyncFile:
    db: str
    col: str
    # documents_json: str
    documents: list = field(default_factory=list)
    
    
@dataclasses.dataclass
class UpstreamSrc:
    work_path:str = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tmp')
    data_sync_cols:list = field(default_factory=list)
    db_client: db.MongoHandler = None
    
    def exec(self):
        # データ同期対象のコレクションからデータ全件取得
        sync_data = []
        for col in self.data_sync_cols:
            sync_data.append(self.get_sync_data_from_col(col))
        
        # 取得したデータの件数比較
        # TODO
        
        # コレクションごとにデータ同期ファイルを作成
        file_names = self.create_data_sync_file(sync_data)
        # zipファイル
        # TODO
        zip_file_name = self.to_zip(file_names) 
        # ランダム秒数スリーブ（実行時間をずらす）
        # TODO
        
        # s3へデータ同期ファイルをアップロード
        # TODO
        
        # アップロードが正常に完了したことを確認
        # TODO
        
        # データ同期対象のコレクションからデータ全件削除
        # TODO

    def get_sync_data_from_col(self, col) -> DataSyncFile:
        # 引数として受け取ったコレクションからドキュメントを全件取得
        # DataSyncFielに設定してレスポンス
        documents_cursor = db.find(self.db_client[col])
        documents_json = dumps(list(documents_cursor))
        return DataSyncFile(self.db_client.name, col, json.loads(documents_json))
            
    def create_data_sync_file(self, sync_data: list[DataSyncFile]):
        # データ同期のデータリストからself.work_path配下にjsonファイルを生成
        file_names = []
        for data in sync_data:
            # dataclass を json へシリアライズ
            json_str = data.to_json(ensure_ascii=False)
            # ファイル名：{database}.{collection}.json
            file_name = f'{data.db}_{data.col}.json'
            with open(os.path.join(self.work_path, file_name), 'w') as json_file:
                json_file.write(json_str)
            file_names.append(file_name)
        return file_names
    def to_zip(file_names):
        pass
        



@dataclasses.dataclass
class UpstreamDst:
    def exec(self):
        pass
    # S3から未適用のデータ同期ファイルを取得
    # 取得したデータ同期ファイルからクエリ生成
    # クエリ実行
    # 未完了の取引データを削除
    # 取得したデータ同期ファイルをS3のディレクトリ移動
    # 最終的な適用結果をログとして出力（店舗数、適用対象店舗、実行結果）


@dataclasses.dataclass
class DownstreamSrc:
    def exec(self):
        pass
        # S3の最新の同期ファイルから
        # resume tokenを取得（ない場合はなしで）
        # while True:
            # change stream 作成（resumetoken設定）TODO resume to
            # ken設定時の動作は？ tokenのイベントを含むか、含まないか
            
            # for event in change stream
                # event をDictに追加
                # resume token詰めなおす
                #　if dic のサイズが一定以上 OR 前回アップロードから一定時間経過
                    # dicをnode id ごとに集計
                    # zipファイルを作成
                    # retry 成功するまで S3へのファイルアップロード
                    ## retry ライブラリはtenacityを使用するのがよさそう 
    

@dataclasses.dataclass
class DownstreamDst:
    node_id: str = ''
    def exec(self):
        # 定期間隔で実行
        scheduler.schedule_random(10, 60, self.get_yet_apply_data())
        while True:
            scheduler.schedule.run_pending()
        # S3バケットのディレクトリにファイルがあるか
        # ない場合 今回処理終了 
        # ある場合
            # ファイルをダウンロード 複数ダウンロードできるか？
            # ファイルの整合性チェック
        # ダウンロードしたファイルからクエリ文を生成
        # トランザクション生成
        # クエリ実行
        
        
        # 正常性チェック（件数比較）
        # トランザクションコミット
        # ダウンロードしたファイルを適用済みのディレクトリへ移動
        # 移動 ＝ cp, mv
            sleep(1)
    def get_yet_apply_data():
        pass
