step = 2  # 每帧移动的像素
class Sprite:
    """
    用于绘制精灵图的工具类
    """
    @staticmethod
    def draw(dest, source, x, y, cell_x, cell_y, cell_w=128, cell_h=128):
        """
        绘制精灵图中，指定x,y的图像
        :param dest: surface类型，要绘制到的目标surface
        :param source: surface类型，来源surface
        :param x: 绘制图像在dest中的坐标
        :param y: 绘制图像在dest中的坐标
        :param cell_x: 在精灵图中的格子坐标
        :param cell_y: 在精灵图中的格子坐标
        :param cell_w: 单个精灵的宽度
        :param cell_h: 单个精灵的高度
        :return:
        """
        dest.blit(source, (x, y), (cell_x * cell_w, cell_y * cell_h, cell_w, cell_h))


class CharWalk:
    """
    人物行走类 char是character的缩写
    """
    DIR_DOWN = 0
    DIR_RIGHT = 1
    DIR_UP = 2
    DIR_LEFT = 3
    DIR_DANCE = 4
    DIR_FAINT = 5  # 晕倒

    def __init__(self, hero_surf, dir, mx, my,step=2):
        """
        :param hero_surf: 精灵图的surface
        :param dir: 角色方向
        :param mx: 角色所在的小格子坐标
        :param my: 角色所在的小格子坐标
        """
        self.hero_surf = hero_surf
        self.dir = dir
        self.mx = mx
        self.my = my
        # 相对
        self.is_walking = False  # 角色是否正在移动
        self.frame = 0  # 角色当前帧
        # 角色下一步需要去的格子
        self.next_mx = 0
        self.next_my = 0
        # 步长
        self.step = step  # 每帧移动的像素

    def draw(self, screen_surf):
        cell_x = int(self.frame)
        cell_y = self.dir
        Sprite.draw(screen_surf, self.hero_surf, self.mx, self.my, cell_x, cell_y)


    def goto(self, x, y):
        """
        :param x: 目标点
        :param y: 目标点
        """
        self.next_mx = x
        self.next_my = y

        # 设置人物面向
        if self.next_mx > self.mx:
            self.dir = CharWalk.DIR_RIGHT
        elif self.next_mx < self.mx:
            self.dir = CharWalk.DIR_LEFT

        elif self.next_my > self.my:
            self.dir = CharWalk.DIR_DOWN
        elif self.next_my < self.my:
            self.dir = CharWalk.DIR_UP

        self.is_walking = True

    def move(self):
        if not self.is_walking:
            return
        dest_x = self.next_mx
        dest_y = self.next_my

        # 向目标位置靠近
        if self.mx < dest_x:
            self.mx += self.step
            if self.mx >= dest_x:
                self.mx = dest_x
                self.goto(self.next_mx, self.next_my)
        elif self.mx > dest_x:
            self.mx -= self.step
            if self.mx <= dest_x:
                self.mx = dest_x
                self.goto(self.next_mx, self.next_my)

        elif self.my < dest_y:
            self.my += self.step
            if self.my >= dest_y:
                self.my = dest_y
        elif self.my > dest_y:
            self.my -= self.step
            if self.my <= dest_y:
                self.my = dest_y

        # 改变当前帧
        self.frame = (self.frame + 0.1) % 4
        """此种方法控制帧数更新速度"""

        # 到达了目标点
        if self.mx == dest_x and self.my == dest_y:
            self.frame = 0
            self.is_walking = False
