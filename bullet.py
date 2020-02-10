import pygame

class Bullet():
    def __init__(self, x, y, vel_x, vel_y):
        v = 40
        s = abs(vel_x) + abs(vel_y)
        self.x = x
        self.y = y
        self.vel_x = v * vel_x / s
        self.vel_y = v * vel_y / s
        self.ttl = 30
    
    def update(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.ttl -= 1

    def get_ttl(self):
        return self.ttl

    def draw(self, surface):
        pygame.draw.circle(surface, (20,20,30), (int(self.x), int(self.y)), 3, 3)