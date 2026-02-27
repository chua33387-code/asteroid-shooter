import sys
import pygame as pg

from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print(f"Starting Asteroids with pygame version: {pg.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    dt = 0
    clock = pg.time.Clock()

    updatable = pg.sprite.Group()
    drawable = pg.sprite.Group()
    asteroids  = pg.sprite.Group()
    shots = pg.sprite.Group()

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids , updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(x, y, PLAYER_RADIUS)
    asteroidfield = AsteroidField()


    while True:
        log_state()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        screen.fill("black")

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()

        for draw in drawable:
            draw.draw(screen)

        pg.display.flip()
        delta = clock.tick(60)
        dt = delta/1000


if __name__ == "__main__":
    main()
