from flask import Flask, request
from flask_cors import CORS
from .rpc import CloudRPC
from .data import logger, Cats, logo, logging
import time
import json

print(logo)

cats = Cats()

rpc = CloudRPC()
rpc.connectRPC()

def timeToSeconds(time: str):
    time_parts = time.split(':')
    if len(time_parts) == 3:
        hours, minutes, seconds = map(int, time_parts)
        return hours * 3600 + minutes * 60 + seconds
    elif len(time_parts) == 2:
        minutes, seconds = map(int, time_parts)
        return minutes * 60 + seconds

class CloudRPCServer:
    def __init__(self, debug):
        self.debug = debug

    app = Flask('CloudRPC Server')
    CORS(app)

    # Disable logging
    logging.getLogger('werkzeug').setLevel(logging.ERROR)

    @app.route('/update', methods=['POST'])
    def update():
        data = json.loads(request.data.decode())

        logger.info('RPC update request')

        try: 
            if data['playing']:
                rpc.updateRPC(str(data['song']).split(' by ')[1], str(data['song']).split(' by ')[0], data['artwork'], data['link'], time.time() +  timeToSeconds(data['duration']) - timeToSeconds(data['current']), True, data['liked'], data['station'], str(data['volume']))
            
            else:
                assets = cats.getRandom()
                rpc.updateRPC(assets[0], "Doesn't listen to anything", assets[1], None, None, False, False, False, '0')

            return '200, Updated RPC'

        except Exception as e:
            logger.error('Error: ' + str(e))
            return 500, 'Error: ' + str(e)

    def run(self):
        self.app.run('127.0.0.1', '9888', self.debug)