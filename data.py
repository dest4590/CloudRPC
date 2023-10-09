import random

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