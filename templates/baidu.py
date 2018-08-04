# coding=utf-8
import sys

import importlib
importlib.reload(sys)

import urllib.request
import urllib
import json
import base64
import requests
class BaiduRest:
    def __init__(self, cu_id, api_key, api_secert):
        # token认证的url
        self.token_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s"
        # 语音合成的resturl
        self.getvoice_url = "http://tsn.baidu.com/text2audio?tex=%s&lan=zh&cuid=%s&ctp=1&tok=%s"
        # 语音识别的resturl
        self.upvoice_url = 'http://vop.baidu.com/server_api'

        self.cu_id = cu_id
        self.getToken(api_key, api_secert)
        return

    def getToken(self, api_key, api_secert):
        # 1.获取token
        token_url = self.token_url % (api_key,api_secert)

        r_str = urllib.request.urlopen(token_url).read()
        token_data = json.loads(r_str.decode('utf-8'))
        #print(token_data)
        self.token_str = token_data['access_token']
        pass

    def getVoice(self, text, filename):
        # 2. 向Rest接口提交数据
        get_url = self.getvoice_url % (urllib.parse.quote(text), self.cu_id, self.token_str)

        voice_data = urllib.request.urlopen(get_url).read()
        # 3.处理返回数据
        voice_fp = open(filename,'wb+')
        voice_fp.write(voice_data)
        voice_fp.close()
        pass


    def getText(self,filename):
        d = open(filename, 'rb').read()
        data = {
            "format": "wav",
            # "format": "wav",
            "rate": 16000,
            "channel": 1,
            "token": self.token_str,
            "cuid": "wewrffa",
            "len": len(d),

            "speech": base64.b64encode(d).decode('utf-8')

        }
        result = requests.post('http://vop.baidu.com/server_api', json=data,
                               headers={'Content-Type': 'application/json'})
        data_result = result.json()



        if data_result['err_msg'] == 'success.':
            return data_result
        else:
            return data_result

if __name__ == "__main__":
    # 我的api_key,供大家测试用，在实际工程中请换成自己申请的应用的key和secert
    api_key = "XsYKMmPFHxyRG2dGdIbHmnjf"
    api_secert = "KRGqbdFEnrxTi7v6RQMimsIW5y7gr3Uf"
    # 初始化
    bdr = BaiduRest("lixing1234", api_key, api_secert)
    # 将字符串语音合成并保存为out.mp3
    bdr.getVoice("你", "out.wav")
    # 识别test.wav语音内容并显示
    print(bdr.getText("16k.pcm"))

