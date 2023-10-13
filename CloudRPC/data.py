from datetime import datetime
import random

version = '1.2 BETA'

logo = f'''
   ____ _     ___  _   _ ____    ____  ____   ____ 
  / ___| |   / _ \| | | |  _ \  |  _ \|  _ \ / ___|
 | |   | |  | | | | | | | | | | | |_) | |_) | |    
 | |___| |__| |_| | |_| | |_| | |  _ <|  __/| |___ 
  \____|_____\___/ \___/|____/  |_| \_\_|    \____|                         
                                       
'''

dateFormat = f'[green bold][{datetime.now().strftime("%d.%m.%Y")}][/] [violet bold]({datetime.now().strftime("%H:%M:%S")})[/]'

class Cats:
    randomWords = [
        'developer loves cats',
        'cats are the cutest',
        'eepy cat'
    ]

    randomGifs = [
        'https://media.tenor.com/h69xkCxWLUIAAAAd/bentley-takeru.gif',
        'https://i.pinimg.com/originals/ca/08/db/ca08dbeee8a7605d1ddc41fb2517193e.gif',
        'https://media.tenor.com/mG5SWFMtHIkAAAAd/cat.gif',
        'https://media.tenor.com/uU_kvtDakbcAAAAd/bingus-cat.gif',
        'https://media.tenor.com/bWUeVRqW9-IAAAAi/fast-cat-cat-excited.gif'
    ]

    def getRandom(self):
        return [random.choice(self.randomWords), random.choice(self.randomGifs)]