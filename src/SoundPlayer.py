from pygame import mixer

class SoundPlayer:
    def __init__(self):
        mixer.init()
    def play(self, filepath):
        sound = mixer.Sound("../res/audio/" + filepath)
        sound.play()
