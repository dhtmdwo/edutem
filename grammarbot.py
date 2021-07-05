from typing import Text
import requests
import json
import re


def grammarBot(sent):
    url = "https://grammarbot.p.rapidapi.com/check"

    # payload = "text=Susan%20go%20to%20the%20store%20everyday&language=en-US"
    payload = "text="+sent
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'x-rapidapi-key': "30ac9ddc37msh23d389f079899d5p1d82ccjsn1126b4f6d889",
        'x-rapidapi-host': "grammarbot.p.rapidapi.com",
        "useQueryString": "true"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    sentence = json.loads(response.text)

    c_sent = correction(sentence, sent)
    # for i in range(len(sentence['matches'])):
    #     for j in range(min(len(sentence['matches'][i]['replacements']), 3)):
    #         print(sentence['matches'][i]['replacements'][j]['value'])
    # print(c_sent)
    return c_sent


def correction(sentence, sent):
    c_sent = sent
    for i in range(len(sentence['matches'])):
        word = sent[sentence['matches'][i]['offset']:sentence['matches']
                    [i]['offset']+sentence['matches'][i]['length']]
        try:
            c_sent = sent.replace(word,
                                  sentence['matches'][i]['replacements'][0]['value'])
        except IndexError:
            print('IndexError')
            continue
    return c_sent


# text = "My naem is Peter."
# grammarBot(text)
