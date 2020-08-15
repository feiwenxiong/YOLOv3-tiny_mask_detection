# video detecting is written by my self 
import cv2
from google.colab.patches import cv2_imshow
import PIL
from PIL import Image
import argparse
import os 

from ctypes import *
import math
import random
import time
import numpy as np
import matplotlib.pyplot as plt


# def convertBack(x, y, w, h):
#     xmin = int(round(x - (w / 2)))
#     xmax = int(round(x + (w / 2)))
#     ymin = int(round(y - (h / 2)))
#     ymax = int(round(y + (h / 2)))
#     return xmin, ymin, xmax, ymax

def array_to_image(arr):
	# need to return old values to avoid python freeing memory
    arr = arr.transpose(2,0,1)
    c = arr.shape[0]
    h = arr.shape[1]
    w = arr.shape[2]
    arr = (arr/255.0).flatten()
    data = dn.c_array(dn.c_float, arr)
    im = dn.IMAGE(w,h,c,data)
    return im



########################################################################### Remember to change it 
import os
os.sys.path.append('/content/drive/My Drive/yolo/darknet/python')
from darknet import *
import darknet as dn

# OpenCV

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='yolo3-tiny? for detection')
    #parser.add_argument('--image', '-I', help='image 属性，非必要参数,但是有默认值', default=1)
    parser.add_argument('--out', help='out,输出视频的地址',default ="/content/drive/My Drive/yolo/darknet/video/video_out/out.mp4")
    parser.add_argument('--path',  help='path,输入需要detect地址', required=True)
    parser.add_argument('--cfg', help = 'such as yolov3.cfg',required=True)
    parser.add_argument('--weights', help = 'such as yolov3.weights',required=True)
    parser.add_argument('--meta', help = 'such as mask.data',required=True)
    args = parser.parse_args()


    # 注意一定要在路径前加上b， 由于c语言 remember to add b before string due to c format
    #net = dn.load_net(b"cfg/yolov3.cfg", b"weights/mask.weights", 0)
    net = dn.load_net(bytes(args.cfg, encoding='utf-8'), bytes(args.weights, encoding='utf-8'), 0)
    meta=dn.load_meta(bytes(args.meta, encoding='utf-8')) # the  .data doc records class and train test info



    #read video  all by myself 
    cap = cv2.VideoCapture(args.path)
    total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
    # Fourcc decoding type

    fourcc = cv2.VideoWriter_fourcc(*'mp4v') #or 'XVID'
    out = cv2.VideoWriter(args.out, fourcc, fps, (width, height))
    
    count=0
    while(1):
        count=count+1
        print(count)
        
        if count==1*fps:
            break
        
        ret, img = cap.read() ## 返回两个值，ret表示读取是否成功，frame/img为读取的帧内容
        #img = np.array(img)
        if ret: 
	    #change cv array to IMAGE object
            #print(type(img))
            
            im=dn.ndarray_to_image(img) # image structure

            r = dn.detect(net, meta, im)

            for i in range(len(r)):
                #print(r[i])
                x1 = r[i][2][0]-r[i][2][2]/2
                y1 = r[i][2][1]-r[i][2][3]/2
                x2 = r[i][2][0]+r[i][2][2]/2
                y2 = r[i][2][1]+r[i][2][3]/2
                label = r[i][0]
                score = r[i][1]
                print(label.decode())
      
                pt1 = (int(x1), int(y1))
                pt2 = (int(x2), int(y2))
                #print(label)
                #cv2.rectangle(img, pt1, pt2, (0, 255, 0), 1)
                cv2.rectangle(img,(int(x1),int(y1)),(int(x2),int(y2)),(0,255,0),2)
                cv2.putText(img, str(label.decode()), (int(x1),int(y1)),fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale =0.8, color=(0,255,255), thickness=2)
            
            # plt.imshow(img)
            # plt.show()
            out.write(img) # output video
            
            
        else: 
            break
        # k==cv2.waitKey(0)
        # if  k==27 & 0xFF == ord('q'):
        #     break
        

    cap.release()
    out.release()
    cv2.destroyAllWindows()



