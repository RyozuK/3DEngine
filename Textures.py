import pygame\

class Texture:
    def __init__(self, file):
        self.image = pygame.image.load(file)

    def get_col(self, x):
        return self.image.subsurface(pygame.Rect(x, 0, x+1, self.image.get_height()))




wall = Texture("res/brick.png")

