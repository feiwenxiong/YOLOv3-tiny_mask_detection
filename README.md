# yolo_mask_detection: How to deploy in Google Lab


### Load everything in repo to google drive

### mount your google drive to your colab notebook

### Because a white space in the path of "My Drive", this will cause "could not open file " error
>>so we need to use 

Deal with the My Drive space sucks issue
!ln -s /content/drive/My\ Drive /content/mydirver 

ln是linux中又一个非常重要命令，请大家一定要熟悉。 它的功能是为某一个文件在另外一个位置建立一个同步的链接，这个命令最常用的参数是-s，具体用法是：ln –s 源文件 目标文件

``!ln -s /content/drive/My\ Drive /content/mydirver ``

### ``%cd path`` to darknet, and then use make code

Before make please modify Makefile to adapt config for gpu, cudnn, opencv

``!make``

### Remember use gloabel path
``%cd [path]``

``import os ``

``os.sys.path.append(path)``

### Prepare your cfg files

cfg/mask.data       --> decription where the train_test_valid data text and (.data, .name) files path  are.

cfg/mask.names      -> classificaiton classes names



### modify your detection.py default parser agargument


### modify your darknet.py to pin point your file path



### prepare your VOC dataset
voc_label.py    --> to create box label(.txt) and train, test.txt

MakeText.py      --> to create 2007_train.txt ,2007_test.txt which contains abs path to images!!  And these will in the path "darknet/scripts"


### If you r using windows please, use ``dos2unix [file path]`` to convert so that it will not throw out 'could not open file' error

### Remember to use cv2_imshow(_) instead of cv2.imshow(_,_)



