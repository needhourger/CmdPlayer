# Command Line MV Player

>## Introduction

* Address: [https://github.com/needhourger/CmdPlayer](https://github.com/needhourger/CmdPlayer)

* 基于某破站av的idea的python版实现。实现了在windows命令行下播放字符动画的功能，并做了些许优化

* 优化：

    * 实现了立刻播放。使用多进程使视频转字符画的过程与播放过程同步进行。缺陷，对cpu负载很大。
    * 实现了音频播放，~~竭尽全力做了音画同步，勉强达到要求~~
    * 可以指定播放视频，不局限于某个视频。但是毫无疑问 _badapple_ 的mv毫无疑问是最合适的
    * 可以指定视频播放长宽大小，但是建议以大尺寸播放，受限于控制台输出效率会导致字符画丢帧降速


>## Additional Requirements

* Opencv2 python
* Pywin32
* pydub & simpleaudio

>## Details

* 使用python的多进程（鉴于python的多线程是个笑话，在使用线程实现的时候无法处理好音画同步问题~~虽然后来也没处理的多好~~）
  
  主进程外，开设三个进程，分别进行视频转换处理，视频播放，以及背景音乐播放

* 利用python的ctypes调用c语言编写的动态链接库，高效实现某些操作，优化速度

> ## Usage

* 使用pip下载好相应依赖环境，将CmdDraw.dll以及CmdPlayer.py放在同级目录下。使用python3环境运行

* 命令
  
        python CmdPlayer.py <mv_name> <width> <height> <music on||off>

* 例子
  
        python CmdPlayer.py test.flv 128 64 on

### **未在非开发环境下运行测试，如有问题欢迎移步issues**



