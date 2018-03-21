import sys
import time
import json
import certifi
import urllib3

from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
from bitcoin_mid import BitcoinMid


bot_key = '<channel access token>'
user_id = '<to>'

line_bot_api = LineBotApi(bot_key)

try:
    bit = BitcoinMid()
    message = ''

    while True:
        # Get Bitcoin rate
        ret = bit.get_mid()
        if (ret):
            message = 'Bitcoin rate: {0}'.format(bit.message)
        else:
            message = 'System Error. Status: {0}'.format(bit.status)

        # LINE push message
        line_bot_api.push_message(user_id, TextSendMessage(text=message))
        print(message)
        time.sleep(60 * 60)
except LineBotApiError as e:
    print(e)
    sys.exit



