# 谁是卧底-大模型版
# LLM-WhoIsTheSpy

#### 一、介绍
让AI大模型玩谁是卧底。

本程序包开发者：thestudent (黎享卓越科创工作室 AI开发组)

开发语言：Python

程序包版本：v0.1 最后编辑于2023-12-1 15:00

本程序包遵守MIT开源协议

#### 二、使用文档

0. 首先请给这个项目点个star :)
1. 下载安装：请下载本页面的文件，解压到任意可用目录下
2. 文件结构说明：所有代码文件均位于src目录下。src/main.py是游戏入口文件，包括比赛配置，玩家类配置等，大家测试时基本不需要更改，运行该文件即可开始游戏；src/WIS.py是本游戏的主要逻辑程序，负责调控游戏各环节，这部分代码请勿做改动；src/myPlayer文件夹下是自定义的玩家类文件，大家的改动主要集中在这个目录中，具体说明如下。
3. 编写自己的ai游戏玩家：myPlayer目录下已经包含一个示例文件testPlayer.py，点击打开，可以看到该程序编写了一个registPlayer类，并且继承了WIS.player类，如果你使用百度文心一言模型，【并且想偷懒:)】则只需更改程序中的prompt，如果你想适配其他ai模型比如科大讯飞或者通义千问，则可以按照指引自行编写，如果你还有其他创意想法，鼓励大家自行拓展，自由度极高。注意！示例文件制作的ai玩家十分拉跨，不建议使用该玩家进行游戏，推荐大家进行一定的拓展和更改，不然容易导致高血压。
4. 开始游戏：指令窗口运行main.py即可开始游戏，图形化界面还在紧锣密鼓地制作之中。当然，你可以自行修改游戏的配置，包括卧底人数，关键词(默认关键词为苹果和橙子)等等，也可以按照注释的指引，添加其他同学编写的玩家，来一场刺激的对战~

#### 三、反馈
如果有任何BUG或者疑问，请及时联系开发者。

测试过程中请勿暴露你自己的api key和secret key，以防流量被盗刷。