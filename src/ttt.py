# -*- coding: utf-8 -*-
"""
Created on 2017-11-15 14:08:14
@author: Joy yx
"""

import os
import cv2
from glob import glob
import numpy as np

# def get_img_info(img_path):
#     """
#     Desc:
#         获取指定路径的图片的信息(B,G,R 三个通量的平均值)
#     Args:
#         img_path --- 图片所在路径
#     Returns:
#         means --- B,G,R 三个通量的平均值
#     """
#     # os.listdir(path) 返回指定路径下的文件和文件夹列表 
#     images = os.listdir(img_path)
#     # np.zeros(shape, dtype=float, order='C') 返回给定形状和类型的新数组，用 0 填充
#     means = np.zeros((3,))
#     i = 0
#     for img in images:
#         # os.path.join() 将多个路径组合后返回，例如 os.path.join("D:\","test.txt")结果是D:\test.txt
#         img_path = os.path.join(img_path,img)
#         # cv2.imread() 读入图片
#         im_array = cv2.imread(img_path)
#         # 图片的像素每个通量的加和值
#         # B
#         means[0] += np.mean(im_array[:,:,0])
#         # G
#         means[1] += np.mean(im_array[:,:,1])
#         # R
#         means[2] += np.mean(im_array[:,:,2])
#         i += 1
#     # 计算平均值
#     means = means/i
#     # 返回平均值
#     return means


def extract_frame_from_video(src_path,dst_path,spacing=0.1,write=True):
    """
    Desc:
        
    Args:
    Returns:
    """
    # 获得视频的格式
    vidcap = cv2.VideoCapture(src_path)
    # success,image = vidcap.read()
    # return success,image
    # # 获得视频的码率以及尺寸
    # fps = vidcap.get(cv2.CAP_PROP_FPS)
    # size = (int(vidcap.get(cv2.CAP_PROP_FRAME_WIDTH)), 
    #     int(vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    # return fps,size
    # # 获得视频的码率，即 fps
    # framgerate = vidcap.get(cv2.CAP_PROP_FPS)
    # count = 0
    # while True:
    #     success,image = vidcap.read()
        
    #     print('Read New frame:',success)
    #     if not success:
    #         break
    #     if not (count % (framgerate* spacing)):
    #         dst_img = dst_path +'/'+ 'frame_' + str(count).rjust(4,'0') + '.jpg'
    #         print('writing to:',dst_img)
    #         cv2.imwrite(dst_img,image)
    #     count += 1


if __name__=='__main__':
    # 解析图片
    # img_path = 'D:/jd/test/'
    # means = get_img_info(img_path)
    # print ("means==>", means)
    
    # 解析视频
    video_path = 'D:/jd/test/vedio/1.mp4'
    dst_path = 'D:/jd/test/extract_images/'
    success,image = extract_frame_from_video(video_path, dst_path)
    print ("success, images===>", success, image)