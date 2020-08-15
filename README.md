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





# 借助项目开源工具yolov3
there exists several path problem which should not be a problem, i will introduce in the code.
yolo/darknet

解压后，如果用gpu 就makefile里开头那修改GPU=1一下，如果是cpu那就直接make
eg:
GPU=0
CUDNN=0

1.数据集需求voc格式 和其他需求
cfg 文件夹中包含着不同版本网络的网络参数以及.data（类参数和地址） 和 .names（类名字）,本项目使用yolov3-tiny.clg， mask_set.data, mask_set.names

scripts 文件夹中需要添加你的VOC数据文件夹 和修改V0C_label.py（from .xml产生 label.txt 必备格式)以及MakeText.py

VOCdevkit里的VOC2007
（有 1.Annotations（xml格式）  2.Imagesets（/main中含有MakeText.py后的train test.text）  3.JPEGImages（纯图片）)

backup or results 用来存储 weights


2.detect函数输出格式解释：
eg:
 ```[('印章', 0.9983074069023132, (912.6295776367188, 395.174072265625, 213.7032928466797, 206.85720825195312)), ('国徽', 0.9921208024024963, (297.0399475097656, 1426.3948974609375, 222.11207580566406, 225.3359832763672)), ('印章', 0.9893943667411804, (740.3536376953125, 1396.102783203125, 212.9912109375, 202.95053100585938))]```

其中：
```r[0]=('狗', 0.9983074069023132, (912.6295776367188, 395.174072265625, 213.7032928466797, 206.85720825195312))```


3.预测视频就输入以下：
```./darknet det.py --help```


code:
```
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='yolo3-tiny? for detection')
    #parser.add_argument('--image', '-I', help='image 属性，非必要参数,但是有默认值', default=1)
    parser.add_argument('--out', help='out 属性，非必要参数，但是有默认值',default ="/home/linwu/Desktop/yolo/darknet/video/video_out")
    parser.add_argument('--path',  help='path 属性，必要参数,输入需要detect地址', required=True)
    parser.add_argument('--cfg', help = 'such as yolov3.cfg',required=True)
    parser.add_argument('--weights', help = 'such as yolov3.weights',required=True)
    parser.add_argument('--meta', help = 'such as mask.data',required=True)
    args = parser.parse_args()
```


4.预测图片：
```
/darknet detect [配置地址]  [权重地址]  [图片地址]

eg: ./darknet detect cfg/yolov3-tiny.cfg yolov3-tiny.weights data/dog.jpg
```
5. 如何训练：

主要修改cfg配置文件头部的 batch ,subdivision , leaning rate值
```./darknet detector train [cfg] [meta] [weights] ```

eg:``` /darknet detector train cfg/voc.data cfg/yolov3-voc.cfg darknet53.conv.74```

6. 要用GPU的话，在makefile最前面找到设为1



