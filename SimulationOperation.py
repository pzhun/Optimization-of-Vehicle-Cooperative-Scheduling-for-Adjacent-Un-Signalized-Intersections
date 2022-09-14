import pygame

def drawLine(cars,screen):
    for car in cars:
        car.LINES_LIST.append((car.rect.centerx, car.rect.centery))
        pygame.draw.lines(screen, (0, 255, 0), 0, car.LINES_LIST)