import random

version = '1.0 ALPHA'

logo = f'''
   ____ _     ___  _   _ ____    ____  ____   ____ 
  / ___| |   / _ \| | | |  _ \  |  _ \|  _ \ / ___|
 | |   | |  | | | | | | | | | | | |_) | |_) | |    
 | |___| |__| |_| | |_| | |_| | |  _ <|  __/| |___ 
  \____|_____\___/ \___/|____/  |_| \_\_|    \____|
                                          {version}                               
'''

class Komaru:
    randomWords = [
        'Komaru cat the best!',
        'dest4590 loves komaru!',
        'Komaru cute cat!'
    ]

    randomGifs = [
        'https://media.tenor.com/xsEFsXZOxM4AAAAd/komaru-cat.gif',
        'https://media.tenor.com/lStgaNc7YHAAAAAd/komaru-cat.gif',
        'https://media.tenor.com/9xdMw3Ui1V8AAAAd/komaru-cat.gif',
        'https://media.tenor.com/GjTiMKDJbAMAAAAd/komaru-cute.gif'
    ]

    def getRandom(self):
        return [random.choice(self.randomWords), random.choice(self.randomGifs)]