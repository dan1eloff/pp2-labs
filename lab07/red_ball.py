import pygame as pg 

pg.init()

screen = pg.display.set_mode((700, 700))

x = 25
y = 25
radius = 25
speed = 20

clock = pg.time.Clock()

done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    keys = pg.key.get_pressed()

    # X ось
    if keys[pg.K_RIGHT]:
        if x + speed + radius > 700:  # Правый край
            continue
        else:
            x += speed

    if keys[pg.K_LEFT]:
        if x - speed - radius < 0:  # Левый край
            continue
        else:
            x -= speed

    # Y ось
    if keys[pg.K_UP]:
        if y - speed - radius < 0:  # Верхний край
            continue
        else:
            y -= speed

    if keys[pg.K_DOWN]:
        if y + speed + radius > 700:  # Нижний край
            continue
        else:
            y += speed

    # Фон
    screen.fill((255, 255, 255)) # белый

    # Круг рисовка
    pg.draw.circle(screen, (255, 0, 0), (x, y), radius)

    pg.display.flip()

    # FPS
    clock.tick(60)

pg.quit()