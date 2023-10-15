from flask import Flask
import os
import SQLiteDB


# サーバの起動
app = Flask(__name__)

# main
@app.route('/')
def hello():
    return 'Hello, World!'

@app.route("/callback", methods=['POST'])
def callback():
    # Lineからのリクエストかどうか確認

    return 'OK'


def handle_message(event):
    # ユーザーからのメッセージを取得
    
    # ここで受け取ったメッセージに対する処理を追加
    # 今日の予定一覧
    # 明日の予定一覧
    # リマインド登録
    # キャンセル

    
    # Lineにメッセージを返信
    return 'OK'


if __name__ == "__main__":
    app.run(port=5000)


# サーバーの階層と処理


# DBと接続
SQLiteDB.init_db()
SQLiteDB.getFirstDate()

