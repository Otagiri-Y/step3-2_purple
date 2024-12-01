import sqlite3
import os

# データベースファイルのパス
DB_PATH = "queue_app.db"

def initialize_db():
    # データベースファイルを削除（存在する場合のみ）
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        print(f"Existing database '{DB_PATH}' has been deleted.")

    # 新しいデータベースを作成
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # テーブルを作成
    cursor.execute('''
        CREATE TABLE queue (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            people_count INTEGER NOT NULL,
            waiting_time INTEGER NOT NULL
        )
    ''')
    
    # 変更を保存して接続を閉じる
    conn.commit()
    conn.close()
    print(f"Database '{DB_PATH}' has been initialized successfully!")

if __name__ == "__main__":
    initialize_db()
