import pygame
from constants import *
from player import Player
from circleshape import CircleShape
from asteroid import Asteroid
from asteroidfield import AsteroidField



def main():
    pygame.init()  #initialize all pygame modules

    clock = pygame.time.Clock()  # initialize an internal clock

    dt = 0 

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()   # create two groups to manage objects
    asteroids = pygame.sprite.Group()  # container for all the asteroids

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)   # initialize a player object
    asteroid_field = AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # get a new GUI window


    

    while True:  # infinite game loop 


        for event in pygame.event.get(): #pygame.event.get() returns a list of inputs
           if event.type == pygame.QUIT: # clicking the x is pygame.QUIT
               return # return exits the main function effectively exiting the game

        screen.fill((0, 0, 0))  #fill the screen black



        updatable.update(dt)

        for obj in asteroids:
            if obj.is_colliding(player):
                print("Game Over!")
                return

        for obj in drawable:      # draw the player. pass the screen as the surface to print it on
            obj.draw(screen)
        
        pygame.display.flip()


        dt = clock.tick(60) / 1000
        # this will pause the game loop until 1/60th of a second passes
        # it also returns the milliseconds that have passed since the last time it was called. Divide by 1000 (ms to s) 











if __name__ == "__main__":
    main()