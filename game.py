from bullet import Bullet
from car import Car
from collections import deque
import pygame

FPS = 60

class Game:
    def __init__(self):
        """ Констуктор класса """
        pygame.init()
        self.screen = pygame.display.set_mode((1080, 720))
        self.car = Car('car1.png', 100, 100)
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

            pos = pygame.mouse.get_pos()
            pygame.draw.circle(self.screen, (255,0,0), pos, 3, 3)
            self.bullets.append(Bullet(self.car.x, self.car.y, (pos[0] - self.car.x), (pos[1] - self.car.y)))

            self.car.handle_keys(self.screen)
            self.car.update()
            i = 0
            for bullet in self.bullets:
                bullet.update()
                if bullet.get_ttl() < 0:
                    i += 1
            for _ in range(i):
                self.bullets.popleft()

            self.car.draw(self.screen)
            for bullet in self.bullets:
                bullet.draw(self.screen)

            pygame.display.update()


game = Game()
game.gameLoop()