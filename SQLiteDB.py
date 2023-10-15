import sqlite3
from datetime import datetime

'''
Todo
1. カラムを増やす（アカウント情報、日時、内容）
2. データを挿入する関数を作る（アカウント情報、日時、内容）

多少の実行速度/メモリ使用率は犠牲にしてでも引数はなるべく少なくする(実装保守が楽かどうかの実験)
'''

# 初期設定する関数
def init_db():
    # SQLiteデータベースに接続
    conn = sqlite3.connect('example.db')
    c = conn.cursor()

    # テーブル作成
    c.execute('''
        CREATE TABLE IF NOT EXISTS my_table (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            my_date DATE
        )
    ''')

# データを新しく挿入する関数

# 最新の日時を取得する関数
def popFirstDate():
    # SQLiteデータベースに接続
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    # 現在の日時を取得
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M')

    # テーブルにデータ挿入
    c.execute('INSERT INTO my_table (my_date) VALUES (?)', (current_date,))
    conn.commit()

    # テーブルを日時でソートして最初の行を取得
    c.execute('SELECT * FROM my_table ORDER BY my_date ASC LIMIT 1')
    result = c.fetchone()

    if result:
        # 結果を表示
        print(f'ID: {result[0]}, Date: {result[1]}')

# 最新の行を削除する関数
def deleteFirstDate():
    # SQLiteデータベースに接続
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('DELETE FROM my_table WHERE id = ?', (result[0],))
    conn.commit()
