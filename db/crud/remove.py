from db import db  # SQLAlchemyインスタンスをインポート
from db.models import Queue  # Queueモデルをインポート

def remove_from_queue(entry_id):
    """
    指定されたIDのエントリをキューから削除する関数
    """
    try:
        # 指定されたIDのレコードを取得
        record = Queue.query.filter_by(id=entry_id).first()
        if record:
            # レコードが存在する場合、削除
            db.session.delete(record)
            db.session.commit()
            print(f"Record with ID {entry_id} removed successfully")
        else:
            # レコードが存在しない場合
            print(f"No record found with ID {entry_id}")
    except Exception as e:
        print(f"Error removing record with ID {entry_id}: {e}")
        db.session.rollback()  # エラー時にロールバック
        raise