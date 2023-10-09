from pypresence import Presence

class CloudRPC:
    client_id = 1140224106009206864
    RPC = Presence(client_id)

    def connectRPC(self):
        print('Connecting to Discord...')
        self.RPC.connect()
        print('Connected!')


    def updateRPC(self, state: str, details: str, large_image: str, link: str, end: int, playing: bool):
        if playing:
            self.RPC.update(state = state, details=details, large_image=large_image, buttons=[{'label': 'Listen', 'url': link}], end=end)
        
        else:
            self.RPC.update(state = state, details=details, large_image=large_image)
    
        print('Updated RPC')