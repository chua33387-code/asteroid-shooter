import pygame as pg

from constants import *
from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pg.Vector2(x, y)

    def draw(self, screen):
        pg.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def move(self, dt):
        self.position += self.velocity * dt

    def update(self, dt):
        self.move(dt)