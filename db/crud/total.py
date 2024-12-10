from db import db  # SQLAlchemyインスタンスをインポート
from db.models import Queue  # Queueモデルをインポート

def get_total_waiting_time():
    """
    待機時間の合計を取得
    """
    try:
        # データベースから待機時間の合計を取得
        total_waiting_time = db.session.query(db.func.sum(Queue.waiting_time)).scalar()
        return total_waiting_time if total_waiting_time else 0
    except Exception as e:
        print(f"Error fetching total waiting time: {e}")
        raise