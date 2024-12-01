from db.connection import get_db_connection

def remove_from_queue(entry_id):
    """
    指定されたIDのエントリをキューから削除する関数
    """
    connection = get_db_connection()
    cursor = connection.cursor()

    # 指定されたIDを削除
    cursor.execute("DELETE FROM queue WHERE id = ?", (entry_id,))
    connection.commit()
    connection.close()
