import pygame
import math


class Camera:
    MOVE_SPEED = 0.08
    ROTATION_SPEED = 0.045

    def __init__(self, x, y, xd, yd, xp, yp, level, screen):
        self.xPos = x
        self.yPos = y
        self.xDir = xd
        self.yDir = yd
        self.xPlane = xp
        self.yPlane = yp
        self.left, self.right, self.forward, self.back = False, False, False, False
        self.shooting = False
        self.level = level
        self.screen = screen
        # oldxDir = self.xDir
        # self.xDir = oldxDir * math.cos(-self.ROTATION_SPEED) - self.yDir * math.sin(-self.ROTATION_SPEED)
        # self.yDir = oldxDir * math.sin(-self.ROTATION_SPEED) + self.yDir * math.cos(-self.ROTATION_SPEED)
        # oldxPlane = self.xPlane
        # self.xPlane = oldxPlane * math.cos(-self.ROTATION_SPEED) - self.yPlane * math.sin(-self.ROTATION_SPEED)
        # self.yPlane = oldxPlane * math.sin(-self.ROTATION_SPEED) + self.yPlane * math.cos(-self.ROTATION_SPEED)

    def update(self, *args):
        key = pygame.key.get_pressed()
        self.left = key[pygame.K_LEFT]
        self.right = key[pygame.K_RIGHT]
        self.forward = key[pygame.K_UP]
        self.back = key[pygame.K_DOWN]
        map = self.level.map

        if self.forward:
            if map[int(self.xPos + self.xDir * self.MOVE_SPEED)][int(self.yPos)] == 0:
                self.xPos += self.xDir * self.MOVE_SPEED
            if map[int(self.xPos)][int(self.yPos + self.yDir * self.MOVE_SPEED)] == 0:
                self.yPos += self.yDir * self.MOVE_SPEED

        if self.back:
            if map[int(self.xPos - self.xDir * self.MOVE_SPEED)][int(self.yPos)] == 0:
                self.xPos -= self.xDir * self.MOVE_SPEED
            if map[int(self.xPos)][int(self.yPos - self.yDir * self.MOVE_SPEED)] == 0:
                self.yPos -= self.yDir * self.MOVE_SPEED

        if self.right:
            oldxDir = self.xDir
            self.xDir = oldxDir * math.cos(-self.ROTATION_SPEED) - self.yDir * math.sin(-self.ROTATION_SPEED)
            self.yDir = oldxDir * math.sin(-self.ROTATION_SPEED) + self.yDir * math.cos(-self.ROTATION_SPEED)
            oldxPlane = self.xPlane
            self.xPlane = oldxPlane * math.cos(-self.ROTATION_SPEED) - self.yPlane * math.sin(-self.ROTATION_SPEED)
            self.yPlane = oldxPlane * math.sin(-self.ROTATION_SPEED) + self.yPlane * math.cos(-self.ROTATION_SPEED)

        if self.left:
            oldxDir = self.xDir
            self.xDir = oldxDir * math.cos(self.ROTATION_SPEED) - self.yDir * math.sin(self.ROTATION_SPEED)
            self.yDir = oldxDir * math.sin(self.ROTATION_SPEED) + self.yDir * math.cos(self.ROTATION_SPEED)
            oldxPlane = self.xPlane
            self.xPlane = oldxPlane * math.cos(self.ROTATION_SPEED) - self.yPlane * math.sin(self.ROTATION_SPEED)
            self.yPlane = oldxPlane * math.sin(self.ROTATION_SPEED) + self.yPlane * math.cos(self.ROTATION_SPEED)

