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
    """
    Desc:
        获取指定路径的图片的信息(B,G,R 三个通量的平均值)
    Args:
        img_path --- 图片所在路径
    Returns:
        means --- B,G,R 三个通量的平均值
    """
    # os.listdir(path) 返回指定路径下的文件和文件夹列表 
    images = os.listdir(img_path)
    # np.zeros(shape, dtype=float, order='C') 返回给定形状和类型的新数组，用 0 填充
    means = np.zeros((3,))
    i = 0
    for img in images:
        # os.path.join() 将多个路径组合后返回，例如 os.path.join("D:\","test.txt")结果是D:\test.txt
        img_path = os.path.join(img_path,img)
        # cv2.imread() 读入图片
        im_array = cv2.imread(img_path)
        # 图片的像素每个通量的加和值
        # B
        means[0] += np.mean(im_array[:,:,0])
        # G
        means[1] += np.mean(im_array[:,:,1])
        # R
        means[2] += np.mean(im_array[:,:,2])
        i += 1
    # 计算平均值
    means = means/i
    # 返回平均值
    return means


def extract_frame_from_video(src_path,dst_path,spacing=0.1,write=True):
    """
    Desc:
        从训练视频中截取视频帧，保存图片，作为训练数据
    Args:
        src_path --- 视频存储路径
        dst_path --- 截取的视频帧图片保存路径
        spacing=0.1 --- 自己设定的一个参数，瞎设置的
        write=True --- 是否要写入
    Returns:
        None
    """
    # 获得视频的格式
    vidcap = cv2.VideoCapture(src_path)
    #success,image = vidcap.read()
    # 获取视频的 fps 也就是码率
    framgerate = vidcap.get(cv2.CAP_PROP_FPS)
    count = 0
    while True:
        # VideoCapture 的 read() 方法是 grab() 方法和 retrieve() 方法的合并。读取视频文件或从解码中捕获数据并返回刚抓取帧的最方便的方法。
        # success 代表读取视频的正确与否状态
        # image 返回视频中被抓取的帧
        success,image = vidcap.read()
        
        print('Read New frame:',success)
        # 判断读取视频是否成功
        if not success:
            break
        if not (count % (framgerate* spacing)):
            dst_img = dst_path +'/'+ 'frame_' + str(count).rjust(4,'0') + '.jpg'
            print('writing to:',dst_img)
            # 保存截取下来的视频帧
            cv2.imwrite(dst_img,image)
        count += 1


def preprocess(video_path,data_path):
    """
    Desc:
        预处理数据，将视频数据抓取出来图片，存储下来
    Args:
        vedio_path --- 视频文件存储路径
        data_path --- 抓取帧的图片存储路径
    Returns:
        None
    """
    # 读取视频所在文件夹的所有视频文件
    # os.listdir(path) 返回指定路径下的文件和文件夹列表
    video_files = os.listdir(video_path)
    for video_file in video_files:
        # 处理视频文件名称，将 .mp4 去掉
        index = int(video_file.replace('.mp4',''))
        # 组合存储抓取视频帧的图片存储路径
        # os.path.join() 将多个路径组合后返回，例如 os.path.join("D:\","test.txt")结果是D:\test.txt
        dst_path = os.path.join(data_path,str(index))
        # 判断图片存储路径的目录是否存在，如果存在就不重复创建了，如果没有则新建文件夹
        if not os.path.exists(dst_path):
            os.mkdir(dst_path)
        src_path = os.path.join(video_path,video_file)
        # 逐个读取视频，从视频中抓取视频帧，存储
        extract_frame_from_video(src_path,dst_path)



if __name__=='__main__':
    #img_path = 'D:/visual_genome/VG_100K/'
    video_path = 'D:/jd/data/train/'
    dst_path = 'D:/jd/data/extracted_images/'
    preprocess(video_path,dst_path)
    #means = get_img_info(img_path)