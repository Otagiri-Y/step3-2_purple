import sqlite3

# データベースファイルのパス
DB_PATH = "queue_app.db"

# 挿入するデータ
data = [
    (1, "Alice", "alice@example.com", 2, 10),  # id, name, email, people_count, waiting_time
    (2, "Bob", "bob@example.com", 3, 15),
    (3, "Charlie", "charlie@example.com", 1, 5),
    (4, "Diana", "diana@example.com", 4, 20),
    (5, "Eve", "eve@example.com", 2, 10)
]

def insert_data():
    # データベースに接続
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # テーブル作成（存在しない場合のみ）
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS queue (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            people_count INTEGER NOT NULL,
            waiting_time INTEGER NOT NULL
        )
    ''')
    
    # データを挿入
    cursor.executemany('''
        INSERT INTO queue (id, name, email, people_count, waiting_time)
        VALUES (?, ?, ?, ?, ?)
    ''', data)
    
    # 変更を保存して接続を閉じる
    conn.commit()
    conn.close()
    print("Data inserted successfully!")

if __name__ == "__main__":
    insert_data()
