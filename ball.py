import pygame

class Ball:
    def __init__(self,screen,paddle,setting) :
        # 初始化必要属性
        self.screen  = screen
        self.screen_rect = self.screen.get_rect()
        self.paddle = paddle
        self.setting = setting
        # 设置ball的半径和颜色
        self.radius = 10
        self.ball_color = (165,42,42)  
        
        # 将ball放到paddle的中间上部
        self.ball_position = (self.paddle.rect.centerx, self.paddle.rect.top - self.radius)

        # 设置移动速度
        self.speed_x = 8
        self.speed_y = 8

        # 保存ball 和 paddle 的外接矩形
        self.ball_rect = pygame.Rect(self.ball_position[0] - self.radius, self.ball_position[1] - self.radius,
                                    self.radius * 2, self.radius * 2)
        self.paddle_rect = paddle.rect

        # 获取ball和paddle中间坐标
        self.ball_centerx = self.ball_position[0]
        self.paddle_centerx = paddle.rect.centerx


    def update(self):
        # 判断球是弹射出去还是跟随paddle移动
        if  self.setting.game_stared :
            # 必须有x，没有影响碰撞时改变移动方向
            self.ball_position = (self.ball_position[0] - self.speed_x, self.ball_position[1] - self.speed_y )        
        else:
            # 跟随paddle一起移动
            self.ball_position = (self.paddle.rect.centerx, self.paddle.rect.top - self.radius)

    def draw_ball(self):
        # 绘制实心圆
        pygame.draw.circle(self.screen,self.ball_color,self.ball_position,self.radius)




