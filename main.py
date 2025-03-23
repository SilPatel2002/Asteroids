import pygame
from constants import *



def main():
    pygame.init()  #initialize all pygame modules

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # get a new GUI window

    while True:  # infinite game loop 


        for event in pygame.event.get(): #pygame.event.get() returns a list of inputs
           if event.type == pygame.QUIT: # clicking the x is pygame.QUIT
               return # return exits the main function effectively exiting the game

        screen.fill((0, 0, 0))
        pygame.display.flip()







if __name__ == "__main__":
    main()