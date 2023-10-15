from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

# Line BotのChannel Access TokenとChannel Secretを設定
# Todo: トークンの入ったファイルから読み込むようにする
line_bot_api = LineBotApi('Your_Channel_Access_Token')
handler = WebhookHandler('Your_Channel_Secret')

# メッセージの受信



#　メッセージの送信


