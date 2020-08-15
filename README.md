# YOLOV3-tiny_mask_detection: How to deploy in Google Lab


### 1. Load everything in repo to google drive 把你的有数据和配置文件上传到谷歌硬盘

### 2. mount your google drive to your colab notebook 绑定硬盘和colab notebook

- Because a white space in the path of "My Drive", this will cause "could not open file " error

- ``Deal with the My Drive space issue sucks `` 他这个默认的My Drive（由于空格）在识别路径的时候总是出幺蛾子
- 解决办法如下：

```!ln -s /content/drive/My\ Drive /content/mydirver ```

ln是linux中又一个非常重要命令，请大家一定要熟悉。 它的功能是为某一个文件在另外一个位置建立一个同步的链接，这个命令最常用的参数是-s，具体用法是：ln –s 源文件 目标文件

``!ln -s /content/drive/My\ Drive /content/mydirver ``

### ``%cd path`` to darknet, and then use make code

Before make please modify Makefile to adapt config for gpu, cudnn, opencv

``!make``

### Remember use gloabel path
``%cd [path]``

``import os ``

``os.sys.path.append(path)``

### Prepare your cfg files  准备cfg文件，包括data文件和names文件和yolov3-tiny.cfg

cfg/mask.data       ==> decription where the train_test_valid data text and (.data, .name) files path  are.

cfg/mask.names     ==> classificaiton classes names



### modify your detection.py default parser agargument  修改parser的参数，方便训练网络


### modify your darknet.py to pin point your file path



### prepare your VOC dataset
voc_label.py    --> to create box label(.txt) and train, test.txt

MakeText.py      --> to create 2007_train.txt ,2007_test.txt which contains abs path to images!!  And these will in the path "darknet/scripts"


### If you are using windows please, use ``dos2unix [file path]`` to convert so that it will not throw out 'could not open file' error

### Remember to use cv2_imshow(_) instead of cv2.imshow(_,_) colab不支持直接使用opencv可以用cv2_imshow()代替



