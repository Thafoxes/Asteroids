import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode(size = (SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH/2 , SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        #then draw players and obj
        for obj in updatable:
            obj.update(dt)

        for obj in drawable:
            obj.draw(screen)

        for obj in asteroids:
            if obj.is_collided(player):
                print("Game over")
                exit()
            
            for bullet in shots:
                if bullet.is_collided(obj):
                    bullet.kill()
                    obj.split()

        pygame.display.flip()

        

        dt = clock.tick(60) /1000

if __name__ == "__main__":
    main()