########  imports  ##########
from __future__ import print_function
import json
import requests
from flask import Flask, jsonify, request, render_template, Response
from flask_cors import CORS
import time
import os
import ProWritingAidSDK
from ProWritingAidSDK.rest import ApiException
import language_tool_python
import subprocess
from pprint import pprint


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'Hello, World!'

# @app.route('/API', methods=['POST'])
# def correctGrammarBot(text):
@app.route('/api/grammarbot', methods=['POST', 'OPTIONS'])
def use_grammarbot_api():
    start = time.time()
    response = Response()
    if request.method == 'OPTIONS':
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add('Access-Control-Allow-Headers', "*")
        response.headers.add('Access-Control-Allow-Methods', "POST")

    elif request.method == 'POST':
        response.headers.add("Access-Control-Allow-Origin", "*")

        received_frontend_data = request.get_json()

        received_frontend_text = received_frontend_data['text']
        # print(received_frontend_text)
        api_data = {
            "text": received_frontend_text,
            "language": "en-US"
        }

        api_url = "https://grammarbot.p.rapidapi.com/check"

        api_headers = {
            "content-type": "application/x-www-form-urlencoded",
            "x-rapidapi-key": "****",
            "x-rapidapi-host": "grammarbot.p.rapidapi.com",
            "useQueryString": "true"
        }

        api_result = requests.post(url=api_url, headers=api_headers, data=api_data).json()
        sending_api_result = {}
        sending_api_result['text'] = received_frontend_text

        if api_result['matches']:
            sending_api_result['matches'] = api_result['matches']

        sending_api_result['time'] = round((time.time() -start)*1000 , 0)
        response.set_data(json.dumps(sending_api_result, indent=2))

    return response

@app.route('/api/languagetool', methods=['POST', 'OPTIONS'])
def use_languagetool_api():
    start = time.time()
    response = Response()

    if request.method == 'OPTIONS':
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add('Access-Control-Allow-Headers', "*")
        response.headers.add('Access-Control-Allow-Methods', "POST")

    elif request.method == 'POST':
        response.headers.add("Access-Control-Allow-Origin", "*")

        received_frontend_data = request.get_json()
        received_frontend_text = received_frontend_data['text']

        url = "https://dnaber-languagetool.p.rapidapi.com/v2/check"
        payload = "text="+received_frontend_data['text']+"&language=en-US"
        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'x-rapidapi-key': "****",
            'x-rapidapi-host': "dnaber-languagetool.p.rapidapi.com"
        }

        api_result = requests.request("POST", url, data=payload, headers=headers).json()
        # print(api_result)
        sending_api_result = {'matches' : []}
        sending_api_result['text'] = received_frontend_text
        if api_result['matches']:
            for value in api_result['matches']:
                matches = {'replacements' : []}
                matches['start'] = value['offset']
                matches['end'] = value['length']+ value['offset']
                matches['word'] = received_frontend_text[ value['offset'] : value['offset'] + value['length'] ]
                for idx, subvalue in enumerate(value['replacements']) :
                    matches['replacements'].append( {'value': subvalue['value'] } )

            sending_api_result['matches'].append(matches)
        sending_api_result['time'] = round((time.time() -start)*1000 , 0)
        response.set_data(json.dumps(sending_api_result, indent=2))

    return response
    # return api_result

@app.route('/api/languagetoolpy', methods=['POST', 'OPTIONS'])
def use_languagetool_python():
    start = time.time()
    received_frontend_data = request.get_json()
    received_frontend_text = received_frontend_data['text']
    tool = language_tool_python.LanguageTool('en-US')

    result = {'matches':[]}
    result['text'] = received_frontend_text
    module_result = tool.check( received_frontend_text )

    for value in module_result:
        matches = {'replacements' : []}
        matches['start'] = value.offset
        matches['end'] = value.offset+ value.errorLength
        matches['word'] = received_frontend_text[value.offset: value.offset+ value.errorLength]

        for subvalue in value.replacements:
            matches['replacements'].append( {'value': subvalue} )

        result['matches'].append(matches)

    result['time'] = round((time.time() -start)*1000 , 0)
    sending_api_result = json.dumps(result, indent=2)

    return sending_api_result


@app.route('/api/textGears', methods=['POST', 'OPTIONS'])
def use_textGears_api():
    start = time.time()
    response = Response()

    if request.method == 'OPTIONS':
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add('Access-Control-Allow-Headers', "*")
        response.headers.add('Access-Control-Allow-Methods', "POST")

    elif request.method == 'POST':
        response.headers.add("Access-Control-Allow-Origin", "*")

        received_frontend_data = request.get_json()
        received_frontend_text = received_frontend_data['text']

        url = "https://textgears-textgears-v1.p.rapidapi.com/grammar"

        payload = "text="+received_frontend_text
        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'x-rapidapi-key': "****",
            'x-rapidapi-host': "textgears-textgears-v1.p.rapidapi.com"
        }

        api_result = requests.request("POST", url, data=payload, headers=headers).json()

        sending_api_result = {}
        sending_api_result['text'] = received_frontend_text

        if api_result['status'] and api_result['response']['errors']:
            sending_api_result['errors'] = api_result['response']['errors']

        sending_api_result['time'] = round((time.time() -start)*1000 , 0)
        response.set_data(json.dumps(sending_api_result, indent=2))

    return response

@app.route('/api/proWritingAid', methods=['POST', 'OPTIONS'])
def use_proWritingAid_api():
    start = time.time()
    received_frontend_data = request.get_json()
    received_frontend_text = received_frontend_data['text']

    configuration = ProWritingAidSDK.Configuration()
    configuration.host = 'https://api.prowritingaid.com'
    configuration.api_key['licenseCode'] = "****"

    # create an instance of the API class
    api_instance = ProWritingAidSDK.TextApi(ProWritingAidSDK.ApiClient('https://api.prowritingaid.com'))
    result = {'matches':[]}
    result['text'] = received_frontend_text

    try:
        api_request = ProWritingAidSDK.TextAnalysisRequest(received_frontend_text,
                                                           ["grammar"],
                                                           "General",
                                                           "en")
        api_response = api_instance.post(api_request)
        for i, value in enumerate(api_response.result.tags):

            matches = {'replacements' : []}
            matches['start'] = value.start_pos
            matches['end'] = value.end_pos+1
            matches['word'] = value.subcategory

            for subvalue in value.suggestions:
                matches['replacements'].append( {'value': subvalue} )

            result['matches'].append(matches)


                # pprint(value.category)
            # pprint()
    except ApiException as e:
        print("Exception when calling API: %s\n" % e)

    result['time'] = round((time.time() -start)*1000 , 0)
    sending_api_result = json.dumps(result, indent=2)

    return sending_api_result
    # return received_frontend_data

@app.route('/api/gector', methods=['POST', 'OPTIONS'])
def use_gector():
    start = time.time()
    response = Response()
    if request.method == 'OPTIONS':
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add('Access-Control-Allow-Headers', "*")
        response.headers.add('Access-Control-Allow-Methods', "POST")

    elif request.method == 'POST':
        response.headers.add("Access-Control-Allow-Origin", "*")

        received_frontend_data = request.get_json()

        received_frontend_text = received_frontend_data['text']
        # print(received_frontend_text)

        with open('incorr.txt', 'w') as file:
            file.write(received_frontend_text)

        '''
        subprocess.call("""bash -c 'source activate gector && python ../../ai/gector/predict.py \\
            --model_path ../../ai/gector/model_v1/best.th \\
            --vocab_path ../../ai/gector/data/output_vocabulary \\
            --input_file incorr.txt \\
            --output_file corr.txt \\
            --iteration_count 5 \\
            --additional_confidence 0.2 \\
            --min_error_probability 0.5'""", shell=True)

        while True:
            if os.path.isfile('corr.txt'):
                break
            time.sleep(0.1)
        '''

        while True:
            if os.path.isfile('done.txt'):
                break
            else:
                time.sleep(0.01)

        with open('corr.txt', 'r') as file:
            lines = file.readlines()

        os.remove('corr.txt')
        os.remove('done.txt')

        sending_api_result = {}
        sending_api_result['text'] = lines[0]
        sending_api_result['time'] = round((time.time() -start)*1000 , 0)
        response.set_data(json.dumps(sending_api_result, indent=2))

        print(sending_api_result)

    return response





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)
