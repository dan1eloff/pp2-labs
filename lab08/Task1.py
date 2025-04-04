import pygame
import random
import time
from itertools import chain

pygame.init()

# Colors
BLACK = pygame.Color((0, 0, 0))
WHITE = pygame.Color((255, 255, 255))
RED = pygame.Color((255, 0, 0))
BLUE = pygame.Color((0, 0, 255))
GREEN = pygame.Color((0, 255, 0))

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
speed = 5

score = 0
coin_score = 0

# Шрифт и текст
font = pygame.font.SysFont("Montserrat", 60)
font_small = pygame.font.SysFont("Montserrat", 20)
game_over_text = font.render("Game Over", True, BLACK)

# Фона
background = pygame.image.load("c:/Users/eradi/Desktop/pp2/pp2-labs/lab08/images/Street.png")

# Настройка экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(WHITE)
pygame.display.set_caption("Racer Game")
clock = pygame.time.Clock()
loop = True

# Классы
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("c:/Users/eradi/Desktop/pp2/pp2-labs/lab08/images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -20)

    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if self.rect.top > SCREEN_HEIGHT:
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -20)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("c:/Users/eradi/Desktop/pp2/pp2-labs/lab08/images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self, enemy):
        super().__init__()
        self.image = pygame.image.load("c:/Users/eradi/Desktop/pp2/pp2-labs/lab08/images/coin.png")
        self.rect = self.image.get_rect()
        coord_range = list(chain(range(22, enemy.rect.center[0] - 24 - 22), range(enemy.rect.center[0] + 24 + 22, SCREEN_WIDTH - 22)))
        self.rect.center = (random.choice(coord_range), 0)

    def move(self, enemy):
        self.rect.move_ip(0, speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            coord_range = list(chain(range(22, enemy.rect.center[0] - 24 - 22), range(enemy.rect.center[0] + 24 + 22, SCREEN_WIDTH - 22)))
            self.rect.center = (random.choice(coord_range), 0)

P1 = Player()
E1 = Enemy()
coin = Coin(E1)

# Группы спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)

coins_group = pygame.sprite.Group()
coins_group.add(coin)

car_sprites = pygame.sprite.Group()
car_sprites.add(P1, E1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, coin)

inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 1000)

# Основной игровой цикл
while loop:
    for event in pygame.event.get():
        if event.type == inc_speed:
            speed += 1  # Скорость врагов и монет

        if event.type == pygame.QUIT:
            loop = False

    # Фон
    screen.blit(background, (0, 0))

    # Количество очков и монет
    score_display = font_small.render(str(score), True, BLACK)
    coin_score_display = font_small.render(f"Coins: {coin_score}", True, BLACK)
    screen.blit(score_display, (10, 10))
    screen.blit(coin_score_display, (SCREEN_WIDTH - 100, 10))

    for entity in car_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    screen.blit(coin.image, coin.rect)
    coin.move(E1)

    # Столкновение с врагами
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound("c:/Users/eradi/Desktop/pp2/pp2-labs/lab08/sounds/crash.wav").play()
        time.sleep(5)

        screen.fill(RED)
        screen.blit(game_over_text, (30, 250))
        pygame.display.update()

        # Удаление объектов
        for entity in all_sprites:
            entity.kill()

        time.sleep(2)
        pygame.quit()

    # Столкновение с монетами
    if pygame.sprite.spritecollide(P1, coins_group, dokill=True):
        pygame.mixer.Sound("c:/Users/eradi/Desktop/pp2/pp2-labs/lab08/sounds/getcoin.mp3").play()
        coin_score += 1
        coin = Coin(E1)
        coins_group.add(coin)
        all_sprites.add(coin)

    try:
        pygame.display.flip()
    except:
        print("Game Over!")
        loop = False

    # FPS
    clock.tick(60)

pygame.quit()