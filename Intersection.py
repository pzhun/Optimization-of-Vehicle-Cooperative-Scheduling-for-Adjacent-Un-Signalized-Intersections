import pygame


class Intersection:
    def __init__(self, screen):
        # 初始化交叉口，并设置位置。
        self.screen = screen

        self.image = pygame.image.load('images/intersection3.0.bmp')
        self.rect = self.image.get_rect()  # 实例
        self.screen_rect = screen.get_rect()  # 实例

        # 将interscetion放在指定位置
        self.rect.center = self.screen_rect.center


    def blitme(self):
        # 在指定位置放置
        self.screen.blit(self.image, self.rect)
