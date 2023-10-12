import random
import logging

# Logger
logger = logging.getLogger('CloudRPC')
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO) 

formatter = logging.Formatter('[%(name)s] (%(asctime)s) - %(message)s', datefmt='%d/%b/%Y %H:%M:%S')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
# ---

version = '1.1'

logo = f'''
   ____ _     ___  _   _ ____    ____  ____   ____ 
  / ___| |   / _ \| | | |  _ \  |  _ \|  _ \ / ___|
 | |   | |  | | | | | | | | | | | |_) | |_) | |    
 | |___| |__| |_| | |_| | |_| | |  _ <|  __/| |___ 
  \____|_____\___/ \___/|____/  |_| \_\_|    \____|
                                          {version}                               
'''

class Cats:
    randomWords = [
        'the developer loves cats',
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