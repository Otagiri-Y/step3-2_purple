from db.connection import get_db_connection

call_count = 0  # グローバル変数で呼び出し回数を管理

def add_to_queue(name, email, people_count, waiting_time):
    """
    新しいユーザーをキューに追加する関数
    """
    global call_count
    connection = get_db_connection()
    cursor = connection.cursor()

    # 呼び出し回数を増加
    call_count += 1
    print(f"add_to_queue called {call_count} times")

    # キューに新しいエントリを追加
    cursor.execute(
        "INSERT INTO queue (name, email, people_count, waiting_time) VALUES (?, ?, ?, ?)",
        (name, email, people_count, waiting_time)
    )
    connection.commit()
    connection.close()

    # 条件が満たされた場合キューをリセット
    if call_count % 5 == 0:
        from db.crud.reset import reset_queue_on_threshold
        reset_queue_on_threshold()
