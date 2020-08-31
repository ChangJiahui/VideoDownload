#coding:utf-8
import os
import time

base_url = "https://www.bilibili.com/video/BV1m7411R7CE?p="
for ii in range(65):
    video_url = base_url + str(ii+1)
    os.system("you-get " + video_url)
    time.sleep(60)