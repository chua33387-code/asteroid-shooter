import random
import pygame as pg

from constants import *
from circleshape import CircleShape
from logger import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pg.Vector2(x, y)
    
    def draw(self, screen):
        pg.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def move(self, dt):
        self.position += self.velocity * dt

    def update(self, dt):
        self.move(dt)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        random_angle = random.uniform(20, 50)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        first_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        second_asteroid = Asteroid(self.position.x, self.position.y, new_radius)

        first_asteroid.velocity = self.velocity.rotate(random_angle) * 1.2
        second_asteroid.velocity = self.velocity.rotate(random_angle) * 1.2
