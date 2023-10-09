from flask import Flask, request
from flask_cors import CORS
from rpc import CloudRPC
from data import *
import logging
import time
import json

komaru = Komaru()

rpc = CloudRPC()
rpc.connectRPC()

def timeToSeconds(time: str):
    minutes, seconds = map(int, time.split(':'))
    return minutes * 60 + seconds

app = Flask('CloudRPC Server')

#logging.getLogger('werkzeug').setLevel(logging.ERROR)

CORS(app)

@app.route('/update', methods=['POST'])
def update():
    data = json.loads(request.data.decode())

    if data['playing']:
        rpc.updateRPC(str(data['song']).split(' by ')[1], str(data['song']).split(' by ')[0], data['artwork'], data['link'], time.time() +  timeToSeconds(data['duration']) - timeToSeconds(data['current']), True)
    
    else:
        assets = komaru.getRandom()
        rpc.updateRPC(assets[0], "Doesn't listen to anything", assets[1], None, None, False)

    return {'status': 'good'}

app.run('127.0.0.1', '9888', True)