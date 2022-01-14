#!/usr/bin/python
# -*- coding: UTF-8 -*-


from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return {"message": "Mattbot"}

@app.route("/mattApi", methods = ["POST"])
def mattApi():
    data = request.get_json()
    if data["password"] == 123:
        from linebot import LineBotApi
        from linebot.models import TextSendMessage
        # 必須放上自己的Channel Access Token
        line_bot_api = LineBotApi('4ScrzrxvUDG4MxuX7XIbawoxU1Rnm+NLnmdqMPFL7NAH/OIqjcyIH2Efc2+1ThoOKKQFYM2b9EF9rO1RuDT6kNt2GXNvURMggfckeqlxus/c3bltb0ZltEERjAEipQjJNpbtdMZ61N2x5py/sWDTaAdB04t89/1O/w1cDnyilFU=')
        
        # 請填入您的ID
        # yourID = 'U52eee020ecebcaa58c22358f67cf2dd6'
        # 主動推播訊息給您上面的ID
        # line_bot_api.push_message(yourID, TextSendMessage(text='安安您早餐吃了嗎？'))
        
        # 廣播給所有人
        line_bot_api.broadcast(TextSendMessage(text=data["message"]))
        return {"message": "success"}

    return {"message": "fail"}