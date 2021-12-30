# 实现图片镜像对称
from PIL import Image
i1_another = Image.open('tree/1.png')
i1_another.transpose(Image.FLIP_LEFT_RIGHT).save('tree/11.png')
i2_another = Image.open('tree/2.png')
i2_another.transpose(Image.FLIP_LEFT_RIGHT).save('tree/22.png')
i3_another = Image.open('tree/3.png')
i3_another.transpose(Image.FLIP_LEFT_RIGHT).save('tree/33.png')