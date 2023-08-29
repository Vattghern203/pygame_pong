from pygame.mixer import Sound

class Sound:

    def __init__(self, path:str) -> None:
        
        self.sound = Sound(path)