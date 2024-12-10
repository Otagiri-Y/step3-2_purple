from db import db  # SQLAlchemyインスタンスをインポート
from db.models import Queue  # Queueモデルをインポート

def get_queue():
    """
    現在のキューの状況を取得する関数
    """
    try:
        # キューのすべてのレコードを取得
        records = Queue.query.order_by(Queue.id.asc()).all()
        
        # 結果を辞書のリスト形式に変換して返す
        return [
            {
                "id": record.id,
                "name": record.name,
                "email": record.email,
                "people_count": record.people_count,
                "waiting_time": record.waiting_time
            }
            for record in records
        ]
    except Exception as e:
        print(f"Error fetching queue: {e}")
        raise