import pygame
from math import sin, cos, pi, radians


class Car(object):
    def __init__(self, file, x, y):
        """ Конструктор класса """
        self.original_image = pygame.image.load(file)
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.x = x                                          # координата x
        self.y = y                                          # координата y
        self.V = 0                                          # скорость
        self.max_V = 10
        self.angle = 0.0                                    # угол поворота
        self.vel_x = self.V * cos(radians(self.angle))      # скорость по оси x
        self.vel_y = self.V * sin(radians(self.angle))      # скорость по оси y


    def update(self):
        """ Обновление координат """
        self.vel_x = self.V * cos(radians(self.angle))
        self.vel_y = self.V * sin(radians(self.angle))
        self.x += self.vel_x
        self.y += self.vel_y
        self.image = pygame.transform.rotate(self.original_image, -self.angle)
        self.rect = self.image.get_rect()


    def handle_keys(self, surface):
        """ Обработка нажатых клавиш """
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            pygame.quit()
        elif key[pygame.K_s]:
            self.V = 0
        elif key[pygame.K_w]:
            if self.V < self.max_V:
                self.V += 1
        elif key[pygame.K_d]:
            self.angle = (self.angle + 10) % 360
        elif key[pygame.K_a]:
            self.angle = (self.angle - 10) % 360

    def draw(self, surface):
        """ Отрисовка машины """
        surface.blit(self.image, (self.x - self.rect[2] / 2, self.y - self.rect[3] / 2))
        pygame.draw.line(surface, (0,255,0), (int(self.x), int(self.y)), (int(self.x+self.vel_x), int(self.y+self.vel_y)), 4)
        pygame.draw.circle(surface, (20,20,30), (int(self.x), int(self.y)), 3, 3)