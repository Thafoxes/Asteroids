from circleshape import *
from constants import SHOT_RADIUS,PLAYER_SHOOT_SPEED 

class Shot(CircleShape):
    
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        return pygame.draw.circle(
            screen,
            "white",
            self.position,
            radius= self.radius,
            width= 2
        )
    
    def update(self, dt):
        self.position += self.velocity * dt

    
    