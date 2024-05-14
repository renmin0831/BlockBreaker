import pygame
import sys
from block import Block


def check_events(paddle,setting):
    # 检查输入事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            check_key_down(event,paddle,setting)
        if event.type == pygame.KEYUP:
            check_key_up(event,paddle)

def check_key_down(event,paddle,setting):
    # 检测键盘按键按下
    if event.key == pygame.K_RIGHT :
        paddle.moving_right = True
    elif event.key == pygame.K_LEFT:
        paddle.moving_left = True
    elif event.key == pygame.K_SPACE:
        setting.game_stared = True

def check_key_up(event,paddle):
    # 检测键盘按键弹起
    if event.key == pygame.K_RIGHT:
        paddle.moving_right = False
    elif event.key == pygame.K_LEFT:
        paddle.moving_left = False

def check_ball_edge_collision(ball,setting):
    # 撞击到屏幕地高端 则相反方向移动
    if ball.ball_position[1] == 0 :
        ball.speed_y *= -1
        ball.ball_position = (ball.ball_position[0],ball.ball_position[1] - ball.speed_y)

    # ball从底部掉落，游戏结束
    if ball.ball_position[1] == ball.screen_rect.bottom:
        setting.game_avtive = False

    # 撞击到左侧屏幕，则相反方向移动
    if ball.ball_position[0] == 0 :
        ball.speed_x *= -1
        ball.speed_y *= 1
        ball.ball_position = (ball.ball_position[0] - ball.speed_x ,ball.ball_position[1] + ball.speed_y)
    # 撞击到右侧屏幕，则相反方向移动
    if ball.ball_position[0] == ball.screen_rect.right :
        ball.speed_x *= -1
        ball.speed_y *= 1
        ball.ball_position = (ball.ball_position[0] - ball.speed_x ,ball.ball_position[1] + ball.speed_y)

def check_ball_paddle_collison(ball,paddle):
    # 获得ball 的外接矩形
    ball_rect = pygame.Rect(ball.ball_position[0] - ball.radius, ball.ball_position[1] - ball.radius,
                            ball.radius * 2, ball.radius * 2)
    paddle_rect = paddle.rect

    # 获取ball和paddle中间坐标
    ball_centerx = ball.ball_position[0]
    paddle_centerx = paddle.rect.centerx
        
    # 如果ball和paddle碰撞
    if ball_rect.colliderect(paddle_rect):
        # 球在碰撞时，首先反转Y方向的速度
        ball.speed_y *= -1

        # 计算球与挡板中心的相对位置,ball与paddle的差值
        centre = ball_centerx - paddle_centerx

        # 根据偏移量调整X方向的速度
        # 如果差值大于0 则在右侧
        if centre > 0:
            # 球落在挡板的右侧
            ball.speed_x = abs(ball.speed_x)
        # 如果差值小于0 则在左侧
        elif centre < 0:
            # 球落在挡板的左侧
            ball.speed_x = -abs(ball.speed_x)
        # 如果差值 ==0 则在中间，这种可能性不太可能有
        elif centre == 0:
            ball.speed_y = -abs(ball.speed_y)
            
        # 最后更新球的位置
        ball.ball_position = (ball.ball_position[0], paddle_rect.top - ball.radius)
    
def create_blocks(blocks,screen):
    block = Block(screen)
    #计算一行能放置多少个block
    availiable_space_x = block.screen_rect.width - block.rect.width
    number_x = availiable_space_x / block.rect.width
    # 计算能放置多少列
    availiable_space_y = block.screen_rect.height / 2 - block.rect.height * 2
    number_y = availiable_space_y / block.rect.height
    # block之间的间隔
    space = 10
    # 将block一行一列的搞出来
    for block_y in range(int(number_y)):
        for block_x  in range(int(number_x)):
            block = Block(screen)
            block.x = (block.rect.width + space) * block_x 
            block.y = (block.rect.height + space) * block_y
            block.rect.x = block.x
            block.rect.y = block.y
            blocks.add(block)
     
def ball_block_collision(ball,blocks):
    # 获得rect属性时为什么会提示没有？？？？
    ball_rect = pygame.Rect(ball.ball_position[0] - ball.radius, ball.ball_position[1] - ball.radius,
                                ball.radius * 2, ball.radius * 2)
    for block in blocks.copy():
        if block.rect.colliderect(ball_rect):
            blocks.remove(block)
            # 碰撞后改变改变方向
            ball.speed_y *= -1
            break

def update_screen(paddle,setting,screen,ball,blocks):
    # 填充背景颜色
    screen.fill(setting.bg_color)
    # 绘制paddle
    paddle.draw_paddle()
    # 绘制ball
    ball.draw_ball()
    # # 绘制精灵组中的block
    for block in blocks.sprites():
        block.draw_block()
    # 绘制可见
    pygame.display.flip()