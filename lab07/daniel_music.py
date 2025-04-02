import pygame
import sys
import random

pygame.init()

window = pygame.display.set_mode((720, 480))
pygame.display.set_caption("Music Player")

# Песни/музыки
songs = [
    'musics/song1.mp3', 
    'musics/song2.mp3',
]

# Для старта
is_playing = False
current_song = random.choice(songs)
pygame.mixer.music.load(current_song)
pygame.mixer.music.play()

# Функции для управления песнями
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
button_size = (173, 173)
button_surface = pygame.Surface(button_size)
button_play_img = pygame.image.load('images/play.jpg')
button_stop_img = pygame.image.load('images/stop.jpg')
button_next_img = pygame.image.load('images/next.jpg')
button_previous_img = pygame.image.load('images/previous.jpg')

def draw_button(image, x, y):
    window.blit(image, (x, y))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Play/Pause
                if is_playing:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                is_playing = not is_playing

            elif event.key == pygame.K_n:  # -->
                play_next_song()

            elif event.key == pygame.K_b:  # <--
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