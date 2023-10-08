from flask import Flask, request
from flask_cors import CORS
from pypresence import Presence
from datetime import datetime
import time
import json

client_id = 1140224106009206864
RPC = Presence(client_id)
print('Connecting...')
RPC.connect()

def timeToSeconds(time: str):
    minutes, seconds = map(int, time.split(':'))
    return minutes * 60 + seconds

def updateRPC(songArtist: str, songName: str, artwork: str, link: str, end: int):
    RPC.update(state = songName, details=songArtist, large_image=artwork, buttons=[{'label': 'Listen', 'url': link}], end=end)
    print('Updated RPC')

app = Flask('CloudRPC Server')
CORS(app)

@app.route('/update', methods=['POST'])
def update():
    data = json.loads(request.data.decode())
    
    print(data)

    updateRPC(str(data['song']).split(' by ')[1], str(data['song']).split(' by ')[0], data['artwork'], data['link'], time.time() +  timeToSeconds(data['duration']) - timeToSeconds(data['current']))
    
    return {'status': 'good'}

app.run('127.0.0.1', '9888', True)