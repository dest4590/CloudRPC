from datetime import datetime
import random

version = '1.3 BETA'
codename = 'CloudLink'

logo = f'''
 __             _  _  __
/   |  _     _||_)|_)/  
\__ | (_)|_|(_|| \|  \__                
'''

dateFormat = f'[green bold][{datetime.now().strftime("%d.%m.%Y")}][/] [violet bold]({datetime.now().strftime("%H:%M:%S")})[/]'

class Cats:
    # By ChatGPT
    randomWords = [
        'cute cat',
        'soft fur cat',
        'gentle purr cat',
        'mysterious eyes cat',
        'playful kittens cat',
        'cozy hideaways cat',
        'graceful agility cat',
        'content and relaxed cat',
        'soothing presence cat',
        'independent spirits cat',
        'bundles of joy cat',
        'affectionate companions cat',
        'warmth and comfort cat',
        'curious nature cat',
        'playful hunters cat',
        'loving company cat',
        'captured hearts cat',
        'loyal friends cat',
        'whiskers and whiskers cat',
        'purring peacefully cat'
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