from db.connection import get_db_connection

def execute_query(query, params=None):
    """SQLクエリを実行"""
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(query, params or ())
    connection.commit()
    connection.close()

def fetch_all(query, params=None):
    """全ての結果を取得"""
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(query, params or ())
    rows = cursor.fetchall()
    connection.close()
    return rows

def fetch_one(query, params=None):
    """1件の結果を取得"""
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(query, params or ())
    row = cursor.fetchone()
    connection.close()
    return row
