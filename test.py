import pygame
import sys


pygame.init()

screen = pygame.display.set_mode((400, 400))
surf = pygame.Surface((100, 100))
surf.fill('white')
rect = surf.get_rect(center=(150, 150))
angle = 0
clock = pygame.Clock()
while True:
    clock.tick(60)

    angle += 1
    if angle == 90:
        angle = 0
    surf = pygame.transform.rotate(surf, angle)
    rect = surf.get_rect(center=(150, 150))
    screen.fill('black')
    screen.blit(surf, rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
