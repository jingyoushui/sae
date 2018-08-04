# coding=utf-8
import requests
import urllib.parse
import sys

import importlib
importlib.reload(sys)


def translations(question):
    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': '0b31c5999c1b42dd8ad00d655640904f',
    }
    params = {
        # Query parameter
        'q': question,
        # Optional request parameters, set to default values
        'timezoneOffset': '0',
        'verbose': 'true',
        'spellCheck': 'true',

    }
    try:
        r = requests.get(
            'https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/c72b58a1-f907-440b-9c2e-b6e247c0db6e',
            headers=headers, params=params)
        return r

    except Exception as e:
        return "[Errno {0}] {1}".format(e.errno, e.strerror)


def divide(q):
    x = translations(q)
    #print(x.json())

    s = x.json().get('query')
    yuantype = x.json().get('topScoringIntent')['intent']
    words = {"query": s}
    for i in x.json()['entities']:
        s1 = i['entity']
        s2 = i['type']

        words[s2] = s1
    if words.__contains__('tolanguage'):
        pass
        if words['tolanguage'] == '英语'or words['tolanguage'] == '英文'or words['tolanguage'] == 'English':
            words['tolanguage'] = 'EN'
        elif words['tolanguage'] == '日语' or words['tolanguage'] == '日文'or words['tolanguage'] == 'Japanese':
            words['tolanguage'] = 'ja'
        elif words['tolanguage'] == '法语' or words['tolanguage'] == '法文'or words['tolanguage'] == 'French':
            words['tolanguage'] = 'fr'
        elif words['tolanguage'] == '韩语' or words['tolanguage'] == '韩文'or words['tolanguage'] == 'Korean':
            words['tolanguage'] = 'ko'
        elif words['tolanguage'] == '俄语' or words['tolanguage'] == '俄文'or words['tolanguage'] == 'russe':
            words['tolanguage'] = 'ru'
        elif words['tolanguage'] == '汉语' or words['tolanguage'] == '中文' or words['tolanguage'] == 'Chinese':
            words['tolanguage'] = 'zh-CHS'
        else:
            words['tolanguage'] = 'EN'
    else:
        if yuantype == 'English':
            words['tolanguage'] = 'zh-CHS'
        else:

            words['tolanguage'] = 'EN'

    #print(words)
    return words






