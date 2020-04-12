"""
使用Pillow来处理图像
"""
# 图片相关
from io import BytesIO
from PIL import Image
import requests as req
from PIL import Image,ImageFilter
# 系统相关
import os
#打开图片，打印其格式、大小、图片类型
img = Image.open('./pythonLearn/res/img/1.jpg')
print(img.format,img.size,img.mode)

#打开图片，打印其格式、大小、图片类型
Image.open('./pythonLearn/res/img/1.jpg').save('./pythonLearn/res/img/1-1.jpg')

#用thumbnail()方法为其生成原尺寸1/3大小的缩略图
w, h =img.size
img.thumbnail((w//3,h//3))
img.save('./pythonLearn/res/img/缩略.jpg','jpeg')

#使用filter()滤镜，此处使用模糊效果
img = Image.open('./pythonLearn/res/img/1.jpg')
img1 = img.filter(ImageFilter.BLUR)
img1.save('./pythonLearn/res/img/模糊.jpg','jpeg')

#翻转
img = Image.open('./pythonLearn/res/img/1.jpg')
img1 = img.transpose(Image.FLIP_LEFT_RIGHT)
img1.save('./pythonLearn/res/img/左右翻转.jpg',"JPEG")
img1 = img.transpose(Image.FLIP_TOP_BOTTOM)
img1.save('./pythonLearn/res/img/上下翻转.jpg',"JPEG")
img1 = img.transpose(Image.ROTATE_90)
img1.save('./pythonLearn/res/img/旋转90度.jpg',"JPEG")
img1 = img.transpose(Image.ROTATE_180)
img.save('./pythonLearn/res/img/旋转180度.jpg',"JPEG")
#学习遍历目录和文件
list = os.listdir('./pythonLearn/res/img')
print(list)
# 此处仅遍历的是根目录
# 使用os.path.spliext(file)[0]可获得主文件名
# 使用os.path.spliext(file)[-1]可获得以.结尾的文件后缀名
for file in list:
    if os.path.splitext(file)[-1] == '.jpg':
        print(os.path.splitext(file)[0])

# 处理网络图片
resp = req.get('https://wx3.sinaimg.cn/mw690/006eXSq0ly1gd5vp6db1cj305k05kmx6.jpg')
image = Image.open(BytesIO(resp.content))
image.save('./pythonLearn/res/img/download.png')