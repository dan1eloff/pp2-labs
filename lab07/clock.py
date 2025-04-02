import pygame
import time
import math

pygame.init()

width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mickey's Clock")

mickey_image = pygame.image.load('mickey_clock_face.png')

minute_hand = pygame.image.load('minute_hand.png')
second_hand = pygame.image.load('second_hand.png')

clock = pygame.time.Clock()

def rotate_image(image, angle, center):
    """ Rotates the image by the given angle around the center point """
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=center)
    return rotated_image, new_rect

def get_minute_angle(minutes):
    return (minutes / 60) * 360

def get_second_angle(seconds):
    return (seconds / 60) * 360

running = True
while running:
    screen.fill((255, 255, 255))

    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min

    center = (width // 2, height // 2)

    minute_angle = get_minute_angle(minutes) - 90
    second_angle = get_second_angle(seconds) - 90

    rotated_minute_hand, minute_rect = rotate_image(minute_hand, minute_angle, center)
    rotated_second_hand, second_rect = rotate_image(second_hand, second_angle, center)

    screen.blit(mickey_image, (0, 0))

    screen.blit(rotated_minute_hand, minute_rect)
    screen.blit(rotated_second_hand, second_rect)

    pygame.display.flip()

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
