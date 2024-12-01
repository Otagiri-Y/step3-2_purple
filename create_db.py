import sqlite3

# SQLite データベースファイル名
DATABASE = "queue_app.db"

def create_database():
    # データベースに接続（ファイルがない場合は新規作成）
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    # テーブルを作成
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS queue (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        people_count INTEGER NOT NULL,
        waiting_time INTEGER NOT NULL
    );
    """)

    # 変更を保存して接続を閉じる
    connection.commit()
    connection.close()
    print(f"Database and table created in {DATABASE}")

if __name__ == "__main__":
    create_database()
