import pygame

class Paddle():
    def __init__(self,screen) :
        # 初始化必要属性
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        
        # 设置paddle的大小
        self.width = 200
        self.height = 20
        self.paddle_color = (107,142,35)

        # 创建paddle的rect对象并设置在底部中间
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom -50

        # 设置连续移动标注
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # 更新paddle移动位置
        if self.moving_right and self.rect.right <self.screen_rect.right:
            self.rect.right += 10

        if self.moving_left and self.rect.left > 0:
            self.rect.left -= 10 

    def draw_paddle(self):
        # 绘制图像
        self.screen.fill(self.paddle_color,self.rect)

