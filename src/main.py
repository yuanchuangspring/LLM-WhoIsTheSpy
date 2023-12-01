'''
main.py
游戏入口文件

'''
from WIS import game
import os
import sys

#导入目录下所有玩家类

sys.path.append("./myPlayer/")

players_dir = "myPlayer"
players_names = os.listdir(players_dir)

#玩家类列表
players_modules = []

for pn in players_names:
    if pn.endswith(".py"):
        pn_module_name = os.path.splitext(os.path.basename(pn))[0]
        pn_module = __import__(name=pn_module_name)
        players_modules.append(pn_module)

#以上代码不需要更改

#配置本场游戏信息

testGame = game({
    #比赛名称
    "name":"测试比赛",
    #比赛描述信息
    "description":"本场比赛用于测试程序逻辑的完备性",
    #比赛中的卧底人数，不能超过总玩家人数的一半
    "spyNum":1,
    #关键词表
    "words":{
        "civilian":"苹果",
        "spy":"橙子"
    },
    #最大回合数
    "maxRound":10
})

#添加玩家，这里是模拟只有一个自定义玩家的情况，多个玩共用一个自定义玩家类

testGame.addPlayer(players_modules[0].registPlayer("玩家1"))
testGame.addPlayer(players_modules[0].registPlayer("玩家2"))
testGame.addPlayer(players_modules[0].registPlayer("玩家3"))

#添加玩家，这里是正常比赛环境时，一个自定义玩家类对应一个玩家的情况
'''
for index,pm in enumerate(players_modules):
    testGame.addPlayer(pm.registPlayer("玩家"+(index+1)))
'''


testGame.start()





