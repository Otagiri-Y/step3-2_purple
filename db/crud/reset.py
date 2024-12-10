from db import db  # SQLAlchemyインスタンスをインポート
from db.models import Queue  # Queueモデルをインポート

def reset_queue_on_threshold():
    """
    キューをリセットする関数（条件に基づく）
    """
    try:
        # 空のエントリを作成
        empty_entry = Queue(
            name="",  # 空の名前
            email="",  # 空のメールアドレス
            people_count=0,  # 初期化された人数
            waiting_time=0  # 初期化された待ち時間
        )

        # データベースに挿入
        db.session.add(empty_entry)
        db.session.commit()
        print("Queue has been reset with an empty entry")

    except Exception as e:
        print(f"Error resetting the queue: {e}")
        db.session.rollback()  # エラー時にロールバック
        raise