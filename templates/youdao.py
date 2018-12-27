# coding=utf-8
import hashlib
import urllib.parse
import random
import requests
import sys
import importlib
importlib.reload(sys)

def youdao(word, tolang):
    appKey = '219b53a26f315c1d'
    secretKey = 'wfj9dtEhHuML4glxlLFHsISX4wjNXL21'

    httpClient = None
    myurl = 'https://openapi.youdao.com/api'
    q = word
    fromLang = 'auto'
    toLang = tolang
    salt = random.randint(1, 65536)

    sign = appKey + q + str(salt) + secretKey
    m1 = hashlib.md5()
    m1.update(sign.encode('utf-8'))

    sign = m1.hexdigest()
    myurl = myurl + '?appKey=' + appKey + '&q=' + urllib.parse.quote(
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign

    try:
        r = requests.get(myurl)

        # json.loads(response.read().decode('utf-8'))

        return r
    except Exception as e:
        return e

    finally:
        if httpClient:
            httpClient.close()


def youdaomain(q):
    if q.__contains__('chinese'):
        wordfrom = q['chinese']
    else:
        wordfrom = q['query']
    tolanguage = q['tolanguage']
    result = {'diword': wordfrom, 'tolanguage': tolanguage}

    x = youdao(wordfrom, tolanguage)
    x = x.json()
    if x.__contains__('web'):
        web = x['web']
        result['fromweb'] = web
    result['translation'] = x['translation']
    result['tSpeakUrl'] = x['tSpeakUrl']
    #print(result)
    return result

