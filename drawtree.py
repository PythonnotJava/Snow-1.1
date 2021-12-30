import sys
import pygame
import random
import os.path as path
from move_ren import Game


def main():
    # 初始化pygame
    pygame.init()
    width = 400
    height = 365
    SIZE = width * 2, height * 2
    screen = pygame.display.set_mode(SIZE, pygame.NOFRAME)

    # 根据背景图片的大小，设置屏幕长宽
    image = pygame.image.load('tree/sds.jpg')
    image.set_alpha(150)

    i1 = pygame.image.load('tree/1.png')
    i1.set_alpha(200)

    # i1的镜像翻转
    i11 = pygame.image.load('tree/11.png')
    i11.set_alpha(180)
    
    i2 = pygame.image.load('tree/2.png')
    i2.set_alpha(200)

    # i1的镜像翻转
    i22 = pygame.image.load('tree/22.png')
    i22.set_alpha(180)
    
    i3 = pygame.image.load('tree/3.png')
    i3.set_alpha(200)

    # i1的镜像翻转
    i33 = pygame.image.load('tree/33.png')
    i33.set_alpha(180)
    
    
    # 雪花列表
    snow_list = []


    # 初始化雪花：(x坐标, y坐标), x轴速度, y轴速度
    for i in range(200):
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
    music = pygame.mixer.Sound('tree/ddd.mp3')
    music.play(-1)

    # 动态人物
    ren = Game(screen, start_x=750, start_y=90, end_x=80, end_y=320, heroes='tree/6.png')
    ren1 = pygame.image.load('tree/7.png')
    # 引线--准时跳出图片
    x1 = -50
    y1 = 300

    # 游戏主循环
    while True:

        screen.fill((0, 0, 0))

        # 重影效果
        # screen.blit(pygame.transform.scale(image2, SIZE), (-width/2, 0))
        screen.blit(pygame.transform.scale(image, SIZE), (0, 0))
        screen.blit(image, (0, 0))
        screen.blit(i1, (430, 190))
        screen.blit(i11, (220, 350))
        screen.blit(i1, (500, 455))
        screen.blit(i2, (500, 650))
        screen.blit(i33, (610, 640))
        screen.blit(i22, [100, 650])
        screen.blit(i33, (350, 655))
        screen.blit(i3, (180, 620))
        
        # screen.blit()
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

        # 圣诞老人奔跑
        ren.role.move()
        ren.role.draw(screen)
        pygame.display.update()
        # 发放礼物
        if x1 < 60:
            x1 += 0.23
        else:
            screen.blit(ren1, (x1, y1))


        # 随机下雪
        for i in range(len(snow_list)):
            # a = (192, 192, 192)
            a = (255, 255, 255)
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