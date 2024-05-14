import pygame
from pygame.sprite import Sprite


class Block(Sprite):
    def __init__(self,screen) :
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # 设置砖块的大小
        self.width = 100
        self.height = 50
        self.block_color = (112,128,144)

        #创建第1个block并指定位置
        self.rect = pygame.Rect(self.width//2,self.width//2,self.width,self.height)

    def update(self):
        pass

    def draw_block(self):
        # 绘制block
        pygame.draw.rect(self.screen, self.block_color, self.rect)

