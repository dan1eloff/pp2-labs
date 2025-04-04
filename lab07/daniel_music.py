import pygame
import sys
import random

pygame.init()

window = pygame.display.set_mode((720, 480))
pygame.display.set_caption("Music Player")

# Песни
songs = [
    'c:/Users/eradi/Desktop/pp2/pp2-labs/lab07/musics/song1.mp3', 
    'c:/Users/eradi/Desktop/pp2/pp2-labs/lab07/musics/song2.mp3',
]

# Для старта
is_playing = False
current_song = random.choice(songs)
pygame.mixer.music.load(current_song)
pygame.mixer.music.play()

# Управление
def play_next_song(): # Следующяя
    global songs, current_song
    songs = songs[1:] + [songs[0]]
    current_song = songs[0]
    pygame.mixer.music.load(current_song)
    pygame.mixer.music.play()

def play_previous_song(): # Предыдущяя
    global songs, current_song
    songs = songs[-1:] + songs[:-1]
    current_song = songs[0]
    pygame.mixer.music.load(current_song)
    pygame.mixer.music.play()

# Интерфейс
button_size = (128, 128)
button_surface = pygame.Surface(button_size)
button_play_img = pygame.image.load('c:/Users/eradi/Desktop/pp2/pp2-labs/lab07/images/play.jpg')
button_stop_img = pygame.image.load('c:/Users/eradi/Desktop/pp2/pp2-labs/lab07/images/stop.jpg')
button_next_img = pygame.image.load('c:/Users/eradi/Desktop/pp2/pp2-labs/lab07/images/next.jpg')
button_previous_img = pygame.image.load('c:/Users/eradi/Desktop/pp2/pp2-labs/lab07/images/past.jpg')

def draw_button(image, x, y):
    window.blit(image, (x, y))

# Обработчик кликов
def button_clicked(x, y, width, height, mx, my):
    return x <= mx <= x + width and y <= my <= y + height

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:  # Проверка на клик
            mx, my = pygame.mouse.get_pos()

            # Play/pause
            if 300 <= mx <= 300 + button_size[0] and 50 <= my <= 50 + button_size[1]:
                if is_playing:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                is_playing = not is_playing

            # Next
            if 500 <= mx <= 500 + button_size[0] and 50 <= my <= 50 + button_size[1]:
                play_next_song()

            # Past
            if 100 <= mx <= 100 + button_size[0] and 50 <= my <= 50 + button_size[1]:
                play_previous_song()

    window.fill((255, 255, 255))

    draw_button(button_previous_img, 100, 50)
    draw_button(button_next_img, 500, 50)
    if is_playing:
        draw_button(button_stop_img, 300, 50)
    else:
        draw_button(button_play_img, 300, 50)

    pygame.display.flip()

pygame.quit()
sys.exit()