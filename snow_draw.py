import sys

import pygame
import random
import os.path as path
# 一个读取初始化文件的模块
from configobj import ConfigObj

# 获得初始化ini文件内容
config = ConfigObj('initialize.ini', encoding='utf-8')

def main():
    # 初始化pygame
    pygame.init()
    width = int(config['width'])
    height = int(config['height'])
    SIZE = width * 2, height * 2
    screen = pygame.display.set_mode(SIZE, pygame.NOFRAME)

    # 根据背景图片的大小，设置屏幕长宽
    image = pygame.image.load(config['back_image'])
    # 图片透明度，为了制造下面重影效果，建议透明度偏向低值
    image.set_alpha(int(config['alpha']))
    image2 = pygame.image.load(config['back_image2']).convert()
    image2.set_colorkey((255, 255, 255))

    # 雪花列表
    snow_list = []


    # 初始化雪花：(x坐标, y坐标), x轴速度, y轴速度
    for i in range(int(config['num'])):
        x = random.randrange(0, SIZE[0])
        y = random.randrange(0, SIZE[1])
        # 让雪有两种下落趋势--左下或者右下
        speed_x = random.randint(-1, 1)
        speed_y = random.randint(1, 4)
        snow_list.append([x, y, speed_x, speed_y])
    # 刷新帧率，控制速度
    clock = pygame.time.Clock()

    # 背景音乐
    pygame.mixer.init()
    pygame.mixer.music.load(config['back_music'])
    pygame.mixer.music.play()
    # 游戏主循环
    while True:

        screen.fill((0, 0, 0))

        # 重影效果
        screen.blit(pygame.transform.scale(image2, SIZE), (-width/2, 0))
        screen.blit(pygame.transform.scale(image, SIZE), (0, 0))
        screen.blit(image, (0, 0))

        # 事件检测
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                # 按q键退出
                if event.key == event.key == pygame.K_q:
                    sys.exit()
                # 按s键截图
                if event.key == pygame.K_s:
                    list_file = []
                    list_ooo = list(range(1000))
                    for num_in in list_ooo:
                        if path.isfile('picture/picture' + str(num_in) + '.jpg'):
                            continue
                        else:
                            list_file.append(num_in)
                    pygame.image.save(screen, 'picture/picture' + str(list_file[0]) + '.jpg')

        # 随机下雪
        for i in range(len(snow_list)):
            a = config['snow_color']
            pygame.draw.circle(
                # 显示
                screen,
                # 颜色
                [int(f) for f in a],
                # 降落点
                snow_list[i][:2],
                # 雪花半径
                snow_list[i][3],
                # 充实雪花颗粒
                0
            )

            # 移动雪花位置（下一次循环起效）
            snow_list[i][0] += snow_list[i][2]
            snow_list[i][1] += snow_list[i][3]

            # 如果雪花落出屏幕，可以让雪不停的下
            if snow_list[i][1] > SIZE[1]:
                snow_list[i][1] = random.randrange(-50, -10)
                snow_list[i][0] = random.randrange(0, SIZE[0])

        # 刷新屏幕
        pygame.display.flip()
        clock.tick(20)

if __name__ == '__main__':
    main()