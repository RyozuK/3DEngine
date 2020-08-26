import pygame
import Camera
import Screen
import Level

WIDTH = 640
HEIGHT= 480
FPS = 60

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.level = Level.Level()
        self.cam = Camera.Camera(12.0, 2.250, 1, 0, 0.0, -0.66, self.level, self.screen)
        self.renderer = Screen.RenderScreen(self.level, self.cam)
        self.running = True
        pass

    def events(self):
        # Game loop - Events
        for event in pygame.event.get():  # event loop
            if event.type == pygame.QUIT:  # check for window quit
                self.running = False

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.cam.update()
            self.renderer.update()






def main():
    game = Game()
    game.run()


if __name__ == '__main__':
    main()