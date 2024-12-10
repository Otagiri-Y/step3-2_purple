from db import db  # SQLAlchemyインスタンスをインポート
from db.models import Queue  # Queueモデルをインポート
from db.crud.reset import reset_queue_on_threshold  # 必要に応じてリセット関数を利用

call_count = 0  # グローバル変数で呼び出し回数を管理

def add_to_queue(name, email, people_count, waiting_time):
    """
    新しいユーザーをキューに追加する関数
    """
    global call_count

    try:
        # 呼び出し回数を増加
        call_count += 1
        print(f"add_to_queue called {call_count} times")

        # 新しいエントリを作成し、データベースに追加
        new_entry = Queue(
            name=name,
            email=email,
            people_count=people_count,
            waiting_time=waiting_time
        )
        db.session.add(new_entry)
        db.session.commit()

        # 呼び出し回数が条件を満たした場合、キューをリセット
        if call_count % 5 == 0:
            reset_queue_on_threshold()

    except Exception as e:
        print(f"Error adding to queue: {e}")
        db.session.rollback()  # エラー時にロールバック
        raise