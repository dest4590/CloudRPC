from pypresence import Presence, DiscordNotFound
from .data import logger

class CloudRPC:
    client_id = 1140224106009206864
    RPC = Presence(client_id)

    def connectRPC(self):
        logger.info('Connecting to Discord...')
        
        try: 
            self.RPC.connect()
        except DiscordNotFound:
            logger.error('Please sure you started discord!')
            quit(0)

        logger.info('Connected!')


    def updateRPC(self, state: str, details: str, large_image: str, link: str, end: int, playing: bool, liked: bool, station):
        if playing:
            if not station:
                self.RPC.update(state = state, details=details, large_image=large_image, buttons=[{'label': 'Listen', 'url': link}], end=end, small_image='cloudrpc_logo' if not liked else 'heart', small_text='CloudRPC' if not liked else 'Liked')
            else:
                self.RPC.update(state = state, details=details, large_image=large_image, buttons=[{'label': 'Listen', 'url': link}, {'label': 'Listen Station', 'url': 'https://soundcloud.com/discover/sets/track-stations:' + str(station).split('%3A')[1]}], end=end, small_image='station', small_text='Listening Station!' if not liked else 'Listening Station, Liked track!')
    

        else:
            self.RPC.update(state = state, details=details, large_image=large_image, large_text='Cat', small_image='cloudrpc_logo', small_text='CloudRPC')


        logger.info('Updated RPC')