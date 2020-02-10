from bullet import Bullet
from car import Car
from collections import deque
from enemy import Enemy
from geometry import *
import pygame

FPS = 25

class Game:
    def __init__(self):
        """ Констуктор класса """
        pygame.init()
        self.screen = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)
        self.car = Car('car1.png', 100, 100)
        self.enemy = Enemy('car2.png', 200, 200)
        self.bullets = deque()
        self.clock = pygame.time.Clock()
        self.running = True

    def gameLoop(self):
        """ Основной цикл событий """
        while self.running:
            self.clock.tick(FPS)
            self.screen.fill((255,255,255))
            pygame.time.delay(30)

            # Обработка событий
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False

            # с наведением
            bullet = Point2D(self.car.x, self.car.y)
            enemy_speed = Vector2D(self.enemy.vel_x, self.enemy.vel_y)
            enemy = Point2D(self.enemy.x, self.enemy.y)
            aim = calc_aim(bullet, enemy_speed, enemy, 40)
            aim = (int(aim[0]), int(aim[1]))
            pygame.draw.circle(self.screen, (30,30,30), aim, 3, 3)
            vel_x = aim[0] - self.car.x
            vel_y = aim[1] - self.car.y
            self.bullets.append(Bullet(self.car.x, self.car.y, vel_x, vel_y))
            pygame.draw.line(self.screen, (0,255,0), (int(self.car.x), int(self.car.y)), aim, 4)

            # # без наводки
            # vel_x = self.enemy.x - self.car.x
            # vel_y = self.enemy.y - self.car.y
            # self.bullets.append(Bullet(self.car.x, self.car.y, vel_x, vel_y))


            self.enemy.handle_keys(self.screen)
            self.enemy.update()
            self.car.handle_keys(self.screen)
            self.car.update()
            i = 0
            for bullet in self.bullets:
                bullet.update()
                if bullet.get_ttl() < 0:
                    i += 1
            for _ in range(i):
                self.bullets.popleft()

            self.enemy.draw(self.screen)
            self.car.draw(self.screen)
            for bullet in self.bullets:
                bullet.draw(self.screen)

            pygame.display.update()


game = Game()
game.gameLoop()