from db.connection import get_db_connection

def get_total_waiting_time():
    """待機時間の合計を取得"""
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT SUM(waiting_time) FROM queue")
    total_waiting_time = cursor.fetchone()[0]
    connection.close()
    return total_waiting_time if total_waiting_time else 0