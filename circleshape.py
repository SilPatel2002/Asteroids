import pygame


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):  # in main.py create your groups first. then this will check if it has containers. 
            super().__init__(self.containers)
        
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        # sub class must override
        pass


    def is_colliding(self, other_obj):
        distance = pygame.math.Vector2.distance_to(self.position, other_obj.position)
        if self.radius + other_obj.radius > distance:
            return True
        
        return False