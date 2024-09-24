from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    
    def __init__(self, x, y, radius, velocity = pygame.Vector2(0,0)):
        super().__init__(x,y,radius)
        self.velocity = velocity

    def draw(self, screen):
        return pygame.draw.circle(screen, 
                                  "white", 
                                  self.position, 
                                  radius= self.radius, 
                                  width= 2 )
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        old_radius = self.radius
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return None
        else:
            random_angle = random.uniform(20,50)
            vector_one = pygame.math.Vector2.rotate(self.velocity, random_angle)
            vector_two = pygame.math.Vector2.rotate(self.velocity, -random_angle)
            self.radius -= ASTEROID_MIN_RADIUS
            asteroid_new1 = Asteroid(self.position.x, self.position.y, radius= self.radius, velocity=vector_one)
            asteroid_new2 = Asteroid(self.position.x, self.position.y, radius= self.radius, velocity= vector_two * 1.2)


