from flask import Flask, request
from flask_cors import CORS
from pypresence import Presence
from data import *
import time
import json

komaru = Komaru()

client_id = 1140224106009206864
RPC = Presence(client_id)
print('Connecting to Discord...')
RPC.connect()

def timeToSeconds(time: str):
    minutes, seconds = map(int, time.split(':'))
    return minutes * 60 + seconds

def updateRPC(details: str, state: str, large_image: str, link: str, end: int, playing: bool):
    if playing:
        RPC.update(state = state, details=details, large_image=large_image, buttons=[{'label': 'Listen', 'url': link}], end=end)
    
    else:
        RPC.update(state = state, details=details, large_image=large_image)
    
    print('Updated RPC')

app = Flask('CloudRPC Server')
CORS(app)

@app.route('/update', methods=['POST'])
def update():
    data = json.loads(request.data.decode())
    
    print(data)

    if data['playing']:
        updateRPC(str(data['song']).split(' by ')[1], str(data['song']).split(' by ')[0], data['artwork'], data['link'], time.time() +  timeToSeconds(data['duration']) - timeToSeconds(data['current']), True)
    
    else:
        assets = komaru.getRandom() # 1 - words, 2 - gifs
        updateRPC(assets[0], 'Not playing a song', assets[1], None, None, False)

    return {'status': 'good'}

app.run('127.0.0.1', '9888', True)