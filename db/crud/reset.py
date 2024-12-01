from db.connection import get_db_connection

def reset_queue_on_threshold():
    """
    キューをリセットする関数（条件に基づく）
    """
    connection = get_db_connection()
    cursor = connection.cursor()

    # 空のエントリを追加してリセット
    cursor.execute(
        "INSERT INTO queue (name, email, people_count, waiting_time) VALUES (?, ?, ?, ?)",
        ("", "", 0, 0)
    )
    connection.commit()
    connection.close()
