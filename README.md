# yolo_mask_detection
How to deploy in Google Lab


## Load everything in repo to goggle drive

## Remember to use make code
Before make please modify Makefile to adapt config for gpu, cudnn, opencv

! make

## Remember use gloabel path
%cd [path]
import os 
os.sys.path.append(path)

## Prepare your cfg files

cfg/mask.data       --> decription where the train_test_valid data text and (.data, .name) files path  are.
cfg/mask.names      -> classificaiton classes names

## modify your detection.py default parser agargument


## modify your darknet.py to pin point your file path



## prepare your VOC dataset


## remember to use cv2_imshow(_) instead of cv2.imshow(_,_)

