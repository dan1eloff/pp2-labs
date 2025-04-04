import pygame
import random

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 480

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
font = pygame.font.SysFont("Montserrat", 25)

snake_block = 10
snake_speed = 15
clock = pygame.time.Clock()

def message(msg, color, x, y):
    mesg = font.render(msg, True, color)
    screen.blit(mesg, [x, y])

# Счет
def display_score(score, level):
    score_text = font.render(f"Score: {score} Level: {level}", True, BLACK)
    screen.blit(score_text, [10, 10])

# Генерация еды
def generate_food(snake_body):
    food_x = random.randrange(0, SCREEN_WIDTH - snake_block, snake_block)
    food_y = random.randrange(0, SCREEN_HEIGHT - snake_block, snake_block)

    while (food_x, food_y) in snake_body:
        food_x = random.randrange(0, SCREEN_WIDTH - snake_block, snake_block)
        food_y = random.randrange(0, SCREEN_HEIGHT - snake_block, snake_block)

    return food_x, food_y

# Главная игровая функция
def gameLoop():
    game_over = False
    game_close = False

    x1 = SCREEN_WIDTH / 2
    y1 = SCREEN_HEIGHT / 2
    x1_change = 0
    y1_change = 0

    snake_body = []
    length_of_snake = 1

    # Генерация еды
    food_x, food_y = generate_food(snake_body)

    score = 0
    level = 1

    while not game_over:
        while game_close:
            screen.fill(WHITE)
            message("You Lost! Press Q-Quit or C-Play Again", RED, SCREEN_WIDTH / 6, SCREEN_HEIGHT / 3)
            display_score(score, level)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Управление
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= SCREEN_WIDTH or x1 < 0 or y1 >= SCREEN_HEIGHT or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(WHITE)

        pygame.draw.rect(screen, GREEN, [food_x, food_y, snake_block, snake_block])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_body.append(snake_head)
        if len(snake_body) > length_of_snake:
            del snake_body[0]

        # Столкновение с собой
        for block in snake_body[:-1]:
            if block == snake_head:
                game_close = True

        # Змея
        for segment in snake_body:
            pygame.draw.rect(screen, BLUE, [segment[0], segment[1], snake_block, snake_block])

        # Счет
        display_score(score, level)

        # Проверка на съеденную еду
        if x1 == food_x and y1 == food_y:
            food_x, food_y = generate_food(snake_body)
            length_of_snake += 1
            score += 10
            if score % 30 == 0:  # УУровень
                level += 1
                global snake_speed
                snake_speed += 5  # Скорость змеи

        pygame.display.update()

        # FPS
        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()