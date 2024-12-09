from db.connection import get_db_connection

class NoAvailableTicketsError(Exception):
    """NULLレコードが存在しない場合のカスタム例外"""
    pass

def prime_to_queue(name, email, people_count, waiting_time):
    """
    特急チケット購入者をキューの最もIDが小さいNULLまたは空レコードに追加する関数。
    NULLレコードが存在しない場合、エラーをフロントに伝える。
    """
    connection = get_db_connection()
    cursor = connection.cursor()

    # いずれかのカラムが NULL または空文字列のレコードを取得
    cursor.execute(
        """
        SELECT id 
        FROM queue 
        WHERE name IS NULL OR name = ''
           OR email IS NULL OR email = ''
           OR people_count IS NULL OR people_count = 0
           OR waiting_time IS NULL OR waiting_time = 0
        ORDER BY id ASC LIMIT 1
        """
    )
    result = cursor.fetchone()

    if result:
        # NULLまたは空レコードが存在する場合、そのIDにエントリを更新
        null_id = result[0]
        cursor.execute(
            """
            UPDATE queue 
            SET name = ?, email = ?, people_count = ?, waiting_time = ?
            WHERE id = ?
            """,
            (name, email, people_count, waiting_time, null_id)
        )
        connection.commit()
        print(f"Record with ID {null_id} updated successfully")
    else:
        # NULLまたは空レコードが存在しない場合
        print("No NULL or empty records found in the queue table")
        raise NoAvailableTicketsError("特急チケットは販売しておりません")

    connection.close()
