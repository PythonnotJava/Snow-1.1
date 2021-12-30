# ---第1步---导出模块---
import pygame
import sys
import math
from pygame.locals import *
import random

# ---第2步---游戏初始化---
pygame.init()

# ---第3步---定义颜色---


# ---第4步---定义窗口大小、标题名称、字体设置、创建时钟---
info = pygame.display.Info()
size = width, height = info.current_w,info.current_h
screen = pygame.display.set_mode(size,pygame.NOFRAME)
pygame.display.set_caption("Surprising Cake")
# 字体
myfont=pygame.font.Font(r'C:\Windows\Fonts\Inkfree.ttf',60)
# 创建时钟对象 (可以控制游戏循环频率)---必须要---
clock = pygame.time.Clock()

# ---第5步---初始化相关定义---具体到各个游戏的定义---
#初始化位置
#5-1
#begin_location--depending on nums
nums = 50
begin_x_list,begin_y_list = [],[]
for x in range(50):
    begin_x = random.choice(list(range(width)))
    begin_x_list.append(begin_x)

for y in range(50):
    begin_y = random.choice(list(range(int(math.ceil(height*0.45)))))
    begin_y_list.append(begin_y)

#different speeds
speed_list = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,
              0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2,
              0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.4, 0.4, 0.4, 0.4, 0.4,
              0.5, 0.5, 0.5, 0.5, 0.5]

#different radius
r = [1,2,3,4]
# ---第6步---游戏循环---
while True:
    # ---6-1---首先---
    # 背景颜色为黑色
    screen.fill((0,0,0))
    # 屏幕上显示文字设置
    textImage = myfont.render("Waiting for good things happing!!!", True, (0,255,0))
    # 在屏幕坐标为100和100的位置显示
    screen.blit(textImage, (100, 100))
    #6-5-1

    for l in range(nums):
        begin_y_list[l] += speed_list[l]
        begin_x_list[l] += speed_list[l]
        pygame.draw.circle(screen, (
        random.choice(list(range(256))), random.choice(list(range(256))), random.choice(list(range(256))))
                               , (begin_x_list[l], begin_y_list[l]), random.choice(r), 0)


    #begin_y_list[5] += 1
    #begin_x_list[5] += 1
    #pygame.draw.circle(screen, (0,255,0),(begin_x_list[5], begin_y_list[5]), 10, 0)
    pygame.display.flip()
    # 数值越大刷新越快，小球运动越快
    clock.tick(40)
    # 检测事件之退出游戏
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_q:
                sys.exit()
