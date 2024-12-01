from db.connection import get_db_connection

def get_queue():
    """
    現在のキューの状況を取得する関数
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM queue ORDER BY id ASC")
    rows = cursor.fetchall()
    connection.close()

    # 結果を辞書のリスト形式で返す
    return [dict(row) for row in rows]
