import pygame
import math
import Textures

WHITE = (255, 255, 255)
DARK_GREY = (28, 28, 28)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


def fill_rect(x, y, w, h, color):
    image = pygame.Surface((w - x, h - y))
    image.fill(color)
    image.get_rect().top = y
    image.get_rect().bottom = y + h
    image.get_rect().left = x
    image.get_rect().right = x + w
    return image


class RenderScreen:
    def __init__(self, level, camera):
        self.frame = 0
        self.level = level
        self.camera = camera
        self.font = pygame.sysfont.SysFont("System",16, False, False)
        self.time = pygame.time.Clock()

    def update(self, *args):
        self.time.tick()
        screen = self.camera.screen
        camera = self.camera
        width = screen.get_width()
        height = screen.get_height()

        screen.fill(BLACK)
        pygame.draw.rect(screen, DARK_GREY, (0, height//2, width, height//2), 0)
        self.frame += 1
        for x in range(width):
            width = screen.get_width()
            height = screen.get_height()

            cameraX = 2 * x / width - 1.0

            rayDirX = camera.xDir + camera.xPlane * cameraX
            rayDirY = camera.yDir + camera.yPlane * cameraX

            mapX = int(camera.xPos)
            mapY = int(camera.yPos)

            if rayDirX != 0:
                deltaDistX = math.sqrt(1 + (rayDirY * rayDirY) / (rayDirX * rayDirX))
            else:
                deltaDistX = math.sqrt(1 + (rayDirY * rayDirY) / (rayDirX * rayDirX + 0.001))
            if rayDirY != 0:
                deltaDistY = math.sqrt(1 + (rayDirX * rayDirX) / (rayDirY * rayDirY))
            else:
                deltaDistY = math.sqrt(1 + (rayDirX * rayDirX) / (rayDirY * rayDirY + 0.001))

            sideDistX, sideDistY = 0, 0
            stepX, stepY = 0, 0
            hit = False
            side = 0

            if rayDirX < 0:
                stepX = -1
                sideDistX = (camera.xPos - mapX) * deltaDistX
            else:
                stepX = 1
                sideDistX = (mapX + 1.0 - camera.xPos) * deltaDistX

            if rayDirY < 0:
                stepY = -1
                sideDistY = (camera.yPos - mapY) * deltaDistY
            else:
                stepY = 1
                sideDistY = (mapY + 1.0 - camera.yPos) * deltaDistY


            while not hit:
                if (sideDistX < sideDistY):
                    sideDistX += deltaDistX
                    mapX += stepX
                    side = 0
                else:
                    sideDistY += deltaDistY
                    mapY += stepY
                    side = 1

                if self.level.map[mapX][mapY] > 0:
                    hit = True

            perpWallDist = 0
            if side == 0:
                perpWallDist = math.fabs((mapX - camera.xPos + (1 - stepX) / 2) / rayDirX)
            else:
                perpWallDist = math.fabs((mapY - camera.yPos + (1 - stepY) / 2) / rayDirY)

            lineHeight = height
            if perpWallDist > 0:
                lineHeight = math.fabs(int(height / perpWallDist))

            drawStart = int(-lineHeight / 2 + height / 2)
            drawEnd = int(lineHeight / 2 + height / 2)

            #Texture picking here
            pixel = (0,0,198)

            wallX, wallDeltaX, wallDeltaY = 0, 0, 0

            if side == 1:
                wallX = camera.xPos + ((mapY - camera.yPos + (1 - stepY) / 2) / rayDirY) * rayDirX
                wallDeltaX = wallX - math.floor(wallX)
                wallDeltaY = 1 if stepY == -1 else 0
            else:
                wallX = (camera.xPos + ((mapX - camera.xPos + (1 - stepX) / 2) / rayDirX) * rayDirY)
                wallDeltaY = wallX - math.floor(wallX)
                wallDeltaX = 1 if stepX == -1 else 0

            wallX -= math.floor(wallX)


            # pygame.draw.line(screen, color, (x, drawStart), (x, drawEnd))
            # line = pygame.transform.scale(Textures.wall.get_col(5), (x, drawEnd - drawStart))
            # screen.blit(line, pygame.Rect(x, drawStart, x, drawEnd))

            texX = int(Textures.wall.image.get_width() * wallX)

            y = drawStart
            #for y in range(drawStart, drawEnd):
            while y < drawEnd:
                # ''' Texture stuff here
                # texY = int(((int(y * 2 - height + lineHeight) << 6) // lineHeight) // 2)
                texY = int(((y - drawStart) / lineHeight) * Textures.wall.image.get_height())
                if x == width // 2:
                    print("x:", x, "\twallX:", wallX, "\ttexX:", texX, "\ttexY:", texY)
                #
                try:
                    color = Textures.wall.image.get_at((texY, texX))
                except:
                    color = (255, 0, 0)
                # if side == 1:
                #     color = (color[0] // 2, color[1] // 2, color[2] // 2)

                screen.set_at((x, y), color)
                y+=1
                #pygame.draw.circle(screen, color, (x,y), 2, 0)
                #pygame.draw.line(screen, color, (x,y), (x,y))



        text = self.font.render(str(self.time.get_fps()),False, WHITE)
        screen.blit(text, (10,10))

        # status = "xPos: %0.4f yPos: %0.4f xDir: %0.4f yDir: %0.4f" % (self.camera.xPos,
        #                                                               self.camera.yPos,
        #                                                               self.camera.xDir,
        #                                                               self.camera.yDir)
        # print(status)


        pygame.display.flip()
