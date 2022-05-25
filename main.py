from PIL import Image
import os
import numpy as np
from tqdm import trange
import argparse

#参数解析器
parser = argparse.ArgumentParser("将众多小图按色块拼接为大图")
parser.add_argument('--i',type=str,default=r'D:/Project/example.jpg',help=r'输入图片绝对路径(默认为"D:/Project/example.jpg")')
parser.add_argument('--o',type=str,default=r'D:/Project/out.jpg',help=r'输出图片路径(默认为"D:/Project/out.jpg")')
parser.add_argument('--s',type=str,default=r'D:/Project/source/',help=r'源图库文件夹路径(默认为"D:/Project/source/")')
parser.add_argument('--M',type=int,default=50,help='像素块大小(每个像素放大M倍)(默认大小50)')
parser.add_argument('--N',type=int,default=3,help='输入图片缩放倍数(原图如果尺寸大于500*500将会缩放)(默认缩小为1/3)')
parser.add_argument('--n',type=int,default=3,help='源图库图片缩放倍数(默认缩小为1/3)')
args = parser.parse_args()

#重要参数
inImg = args.i
outImg = args.o
sourceDir = args.s
N = args.N
n = args.n
M = args.M

#缩放并获取图像的平均颜色值
def colorAvg(imgPath):
    img = Image.open(imgPath)
    img = img.convert("RGB")

    # 缩放源图库图片,高度、宽度均变为原来的1/n
    img = img.resize(tuple([size//n for size in img.size]))  
    #数组存储每个像素点的RGB值
    imArray = np.array(img)      
    
    #获取所有R、G、B的平均值
    R = np.mean(imArray[:,:, 0])
    G = np.mean(imArray[:,:, 1])
    B = np.mean(imArray[:,:, 2])

    return (R, G, B)

#返回缩放图片路径及对应平均RGB值      
def getImgList():
    imgList = []
    for pic in os.listdir(sourceDir):

        imgPath = sourceDir + pic
        imgRGB = colorAvg(imgPath)
        imgList.append({
            "imgPath": imgPath,
            "imgRGB": imgRGB
        })

    return imgList

def color_Dvalue(color1, color2):
    dis=0
    #计算两张图的颜色差(色彩空间距离)
    for i in range(len(color1)):
        dis+= (color1[i] - color2[i]) ** 2
    dis = dis ** 0.5
    return dis

def create_image(inImg):
    imgList = getImgList()
    img = Image.open(inImg)
    if ((img.size[0] >500) or (img.size[1]>500)):
        img = img.resize((img.size[0] // N, img.size[1] // N)) 
    imgArray = np.array(img)

    #创建空白的新图(宽度、高度为img的M倍)
    newImg = Image.new('RGB',(img.size[0] * M, img.size[0] * M))

    #循环填充图
    for x in trange(imgArray.shape[0]):
        for y in range(imgArray.shape[1]): 
            #找到距离最小的图片
            minDis = 10000
            index = 0
            for img in imgList:
                dis = color_Dvalue(img['imgRGB'],imgArray[x][y])
                if dis < minDis:
                    index = img['imgPath']
                    minDis = dis
            #循环完毕，index就是存储了色彩最相近的图片路径,minDis为最小色彩差值
            minImg = Image.open(index)
            #调整图片大小
            minImg = minImg.resize((M,M))
            #填充
            newImg.paste(minImg,(y * M , x * M))

    #保存图片
    newImg.save(outImg) # 最后保存图片
   
create_image(inImg)
