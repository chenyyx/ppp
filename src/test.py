# -*- coding: utf-8 -*-
"""
Created on 2017-11-15 14:08:14
@author: Joy yx
"""

import os
import cv2
from glob import glob
import numpy as np


def get_img_info(img_path):
    # 读入图像，cv2.IMREAD_UNCHANGED --- 读入原图 、 cv2.IMREAD_GRAYSCALE --- 以灰度模式读入原图、cv2.IMREAD_COLOR --- 读入彩色图像，图像的透明度将会被忽略
    # img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    # # 将读入的图片显示出来
    # cv2.namedWindow('leimu',cv2.WINDOW_AUTOSIZE)
    # cv2.imshow('leimu', img)
    # k = cv2.waitKey(0)

    # if k==27:
    #     cv2.destroyAllWindows()
    #     plt.close()
    # elif k==ord('s'):
    #     cv2.imwrite('lenagray.png',img)
    #     cv2.destroyAllWindows()
    # # print 读入的 img
    # print ("img==>", type(img), np.shape(img), img)

    # opencv 的像素是 BGR 顺序，然而 matplotlib 所遵循的是 RGB 顺序
    from matplotlib import pyplot as plt
    img=cv2.imread(img_path,cv2.IMREAD_COLOR)
    # plt.imshow(img)
    # plt.show()

    # 方法一
    # b, g, r = cv2.split(img)
    # print ("b==g==r",b,g,r)
    # img2 = cv2.merge([r, g, b])
    # plt.imshow(img2)
    # plt.show()

    # 方法二
    # img3 = img[:, :, ::-1]
    # plt.imshow(img3)
    # plt.show()

    # 方法三
    # img4 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # plt.imshow(img4)
    # plt.show()

    # ---------------
    # 上述方法二利用了 numpy 对数组的翻转，我们这里介绍一下
    # 我仿照图片的像素格式，建立一个2行3列的，每个像素有包含RGB3个元素。
    # 分别进行图中所示的4种运算。
    # 执行a[:-1]，移除了后面的一行。对于一维数组，后面的一行其实就是最后一个元素，所以这个运算就是移除最后一个元素。
    # 执行a[::-1]，上下两行交换了。同样的看成一维数组的话，一行就是一个元素，这个运算其实就是对一个一维数组内的元素前后对调。多维数组可以理解成对对第一个方括号内的每一个元素前后对调。
    # 执行a[:,::-1]，每一行中的元素前后交换了。简单理解就是对第二层反括号内的元素前后对调。
    # 执行a[:,:,::-1]，这样就好理解了，肯定是对第三层方括号内的元素对调。这也就解释了，对于一个24位深度的图像执行这个操作的话，是对每个像素的RGB进行对调。
    # 对于图像而言，a[::-1]，a[:,::-1]，a[:,:,::-1]上述的三种方法分别是X轴的镜像，Y轴的镜像，BGR转换为RGB的操作。

    a = np.arange(18).reshape(2,3,3)
    print("a===>", a)
    a1 = a[:-1]
    print("a1===>", a1)
    a2 = a[::-1]
    print("a2===>", a2)
    a3 = a[:,::-1]
    print("a3===>", a3)
    a4 = a[:,:,::-1]
    print("a4===>", a4)




if __name__=='__main__':
    img_path = 'D:/jd/test/leimu.jpg'
    means = get_img_info(img_path)