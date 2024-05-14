import pygame
from settings import Settings
from paddle import Paddle
import game_functions as gf
from ball import Ball 
from block import Block
from pygame.sprite import Group


def rungame():
    # 初始化pygame模块
    pygame.init()
    clock = pygame.time.Clock()
    #创建屏幕
    pygame.display.set_caption('Block Breaker Game')
    setting = Settings()
    screen = pygame.display.set_mode((setting.screen_width,setting.screen_height))
    paddle = Paddle(screen)
    ball = Ball(screen,paddle,setting)
    # 将block改成精灵组
    blocks = Group()
    # 创建blocks
    gf.create_blocks(blocks,screen)

    while True:
        # 设置帧率 
        clock.tick(60)

        # 事件和碰撞检测
        gf.check_events(paddle,setting)
        gf.ball_block_collision(ball,blocks)
        gf.check_ball_edge_collision(ball,setting)
        gf.check_ball_paddle_collison(ball,paddle)
        
        # 更新paddle、ball、blocks位置
        paddle.update()
        ball.update()
      
        # 屏幕内容更新
        gf.update_screen(paddle,setting,screen,ball,blocks)

rungame()


