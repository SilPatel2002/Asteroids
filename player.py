import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):

    
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)

        self.rotation = 0
        self.shoot_timer = 0 

    
    def triangle(self):

        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5

        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right

        return [a, b, c]
    

    def draw(self, screen):
            # the screen, white, the postion of triangle, and width of the lines
        pygame.draw.polygon(screen, WHITE_COLOR, self.triangle(), 2)


    def rotate(self, dt): 
                # how fast the turn the player
        self.rotation += PLAYER_TURN_SPEED * dt


    def move(self, dt):
        
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1)
        shot.velocity = shot.velocity.rotate(self.rotation)
        shot.velocity *= PLAYER_SHOT_SPEED

        self.shoot_timer = PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        self.shoot_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:  # go left 
            self.rotate(-dt)

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:   # go right
            self.rotate(dt)


        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            if self.shoot_timer <= 0:
                self.shoot()

  
