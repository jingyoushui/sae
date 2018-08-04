# coding=utf-8
import sys
import importlib
importlib.reload(sys)
from templates import youdao
from templates import translation
from templates import baidu
from flask import Flask, jsonify
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app=app)
api_key = "XsYKMmPFHxyRG2dGdIbHmnjf"
api_secert = "KRGqbdFEnrxTi7v6RQMimsIW5y7gr3Uf"
# 初始化
bdr = baidu.BaiduRest("lixing1234", api_key, api_secert)

def playvoice():

    # 识别test.wav语音内容并显示
    a = bdr.getText("upload/3.wav")
    json_str = json.dumps(a, ensure_ascii=False)
    s = jsonify(json_str)

    return a['result'][0]


@app.route('/v1/translation/<words>', methods=['GET'])
def hello_world(words):
    
    words = words.replace('。','')
    words = words.replace('，','')
    words = words.replace('？','')
    if(words):
        
        x = translation.divide(words)
        #print(x)
        a = youdao.youdaomain(x)
        #print(a)
        #print(a['translation'][0])

        
        
       # bdr.getVoice(a['translation'][0], "down/out.wav")
        json_str = json.dumps(a, ensure_ascii=False)
        s = jsonify(json_str)
        return s, 400

    else:
        return 404

if __name__ == '__main__':

    app.run(host = '0.0.0.0',port = 5050)


