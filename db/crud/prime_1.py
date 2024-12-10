from db import db  # SQLAlchemyインスタンスをインポート
from db.models import Queue  # Queueモデルをインポート

class NoAvailableTicketsError(Exception):
    """NULLレコードが存在しない場合のカスタム例外"""
    pass

def prime_to_queue(name, email, people_count, waiting_time):
    """
    特急チケット購入者をキューの最もIDが小さいNULLまたは空レコードに追加する関数。
    NULLレコードが存在しない場合、エラーをフロントに伝える。
    """
    try:
        # いずれかのカラムがNULLまたは空文字列のレコードを取得
        null_record = Queue.query.filter(
            (Queue.name == None) | (Queue.name == ''),
            (Queue.email == None) | (Queue.email == ''),
            (Queue.people_count == None) | (Queue.people_count == 0),
            (Queue.waiting_time == None) | (Queue.waiting_time == 0)
        ).order_by(Queue.id.asc()).first()

        if null_record:
            # NULLまたは空レコードが存在する場合、そのレコードを更新
            null_record.name = name
            null_record.email = email
            null_record.people_count = people_count
            null_record.waiting_time = waiting_time
            db.session.commit()
            print(f"Record with ID {null_record.id} updated successfully")
        else:
            # NULLまたは空レコードが存在しない場合
            print("No NULL or empty records found in the queue table")
            raise NoAvailableTicketsError("特急チケットは販売しておりません")

    except Exception as e:
        print(f"Error in prime_to_queue: {e}")
        db.session.rollback()  # エラー時にロールバック
        raise