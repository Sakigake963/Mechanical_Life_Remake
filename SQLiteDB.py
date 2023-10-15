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
    conn = sqlite3.connect('LineMessageDB.db')
    c = conn.cursor()

    # テーブル作成
    c.execute('''
        CREATE TABLE message_table (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            line_id TEXT,
            datetime DATE,
            content TEXT
        );
    ''')


# データを新しく挿入する関数
def insertData():
    # SQLiteデータベースに接続
    conn = sqlite3.connect('LineMessageDB.db')
    c = conn.cursor()

    # 現在の日時を取得
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M')

    # テーブルにデータ挿入
    c.execute('INSERT INTO message_table (datetime) VALUES (?)', (current_date,))
    conn.commit()

    print('データを挿入 ---')
    print(f'Date: {current_date}')




# 最新の日時を取得する関数
def getFirstDate():
    # SQLiteデータベースに接続
    conn = sqlite3.connect('LineMessageDB.db')
    c = conn.cursor()

    # テーブルを日時でソートして最初の行を取得
    c.execute('SELECT * FROM message_table ORDER BY datetime ASC LIMIT 1')
    result = c.fetchone()

    if result:
        # 結果を表示
        print('最新の行 ---')
        print(f'ID: {result[0]}, Date: {result[2]}')


# 最新の行を削除する関数
def deleteFirstDate():
    # SQLiteデータベースに接続
    conn = sqlite3.connect('LineMessageDB.db')
    result = c.fetchone()
    c = conn.cursor()

    c.execute('DELETE FROM message_table WHERE id = ?', (result[0],))

    conn.commit()


# テーブルの中身を一覧表示する関数
def showAll():
    # SQLiteデータベースに接続
    conn = sqlite3.connect('LineMessageDB.db')
    c = conn.cursor()

    c.execute('SELECT * FROM message_table')

    result = c.fetchall()

    # 結果を表示
    print('テーブル一覧 ---')
    for row in result:
        print(f'ID: {row[0]}, Date: {row[2]}')
