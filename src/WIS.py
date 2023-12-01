'''
Author: LHY 黎享卓越科创工作室
Date: 2023-11-28
LatestEditDate: 2023-12-1
name: 谁是卧底WhoIsTheSpy package

'''

import requests
import json
import random

class player():
    def __init__(self,name):

        #玩家名称
        self.name=name

        #关键词
        self.word=""

        #上下文
        self.context = ""

    def setWord(self,word):
        self.word = word
        #以下自定义关键词接口

    def send(self,content):
        #自定义发送信息接口
        return "投票给玩家2"
    
class game():
    def __init__(self,config):

        #比赛名称
        self.name=config["name"]

        #比赛简介
        self.description = config["description"]

        #卧底人数
        self.spyNum = config["spyNum"]

        #关键词列表
        self.words = config["words"]
        
        #最大回合数
        self.maxRound = config["maxRound"]

        #投票箱
        self.votes = []

        #比赛上下文
        self.context = ""

        #结束语
        self.ending=""

        #回合数
        self.round = 0

        #玩家列表
        self.players = []

        #间谍序号
        self.spyIndex = []

    def addPlayer(self,newPlayer):
        #添加玩家
        self.players.append(newPlayer)
        self.log(f"新玩家入场! 欢迎{newPlayer.name}!")

    def start(self):
        #开始游戏
        self.log(f"欢迎各位来到本次'谁是卧底',本场比赛名称为：{self.name}, {self.description},下面由我来介绍一下本次比赛的各位选手：")
        for index,p in enumerate(self.players):
            self.log("玩家"+str(index+1)+":"+p.name)
            self.players[index].setWord(self.words["civilian"])
            
            #初始化投票箱
            self.votes.append(0)

        self.log("好的,以上就是本次游戏的全部玩家了,接下来我会为每位玩家分配关键词")


        #指定卧底
        for i in range(0,self.spyNum):
            randindex = random.randint(0,len(self.players)-1)
            if not randindex in self.players:
                self.spyIndex.append(randindex)
                self.players[randindex].setWord(self.words["spy"])

        self.log("分配完成! 游戏正式开始! ")

        self.ending = f"卧底的关键词是{self.words['spy']},平民的关键词是{self.words['civilian']}"


        self.gameLoop()

        


    def gameLoop(self):
        #游戏循环

        #重置投票箱
        for index,vote in enumerate(self.votes):
            self.votes[index] = 0

        self.round+=1

        self.log(f"第{self.round}回合开始!")

        #发言环节
        for index,p in enumerate(self.players):
            self.log(f"下面有请玩家{p.name}进行发言!")

            result = self.broadcast(index,f"主持人:下面有请玩家{p.name}进行发言!")

            self.log(f"{self.players[index].name}:{result}")

        #投票环节
        for index,p in enumerate(self.players):
            self.log(f"下面有请玩家{p.name}进行投票!")

            result = self.broadcast(index,f"主持人:下面有请玩家{p.name}进行投票,请说出所投玩家的完整名称!")

            self.log(result)

            aimPlayer = -1

            for ind,i in enumerate(self.players):
                if i.name in result and i.name!=p.name:
                    if aimPlayer==-1:
                        aimPlayer = ind
                    elif len(self.players[aimPlayer].name)<len(i.name):
                        aimPlayer = ind

            if aimPlayer!=-1:
                self.log(f"{p.name}投票给{self.players[aimPlayer].name}")
                self.broadcast(-1,f"{p.name}投票给{self.players[aimPlayer].name}")
                self.votes[aimPlayer]+=1
            else:
                self.log(f"{p.name}投票无效!")
                self.broadcast(-1,f"{p.name}投票无效!")

        self.broadcast(-1,"投票结束!")
        self.log("投票结束!")

        #检票环节
        loser = -1
        maxVote = 0
        for index,vote in enumerate(self.votes):
            self.broadcast(-1,f"{self.players[index].name}得票{vote}票")
            self.log(f"{self.players[index].name}得票{vote}票")
            if vote>maxVote:
                maxVote = vote
                loser = index
            elif vote == maxVote:
                loser = -1

        #胜负判定
        if loser == -1:
            self.broadcast(-1,f"本回合无人出局!")
            self.log("本回合无人出局!")
            if self.round==self.maxRound:
                self.log("卧底获胜! 游戏结束!")
                self.log(self.ending)
            else:
                self.gameLoop()

        else:
            self.broadcast(-1,f"{self.players[loser].name}被投票出局!")
            self.log(f"{self.players[loser].name}被投票出局!")

            self.players.pop(loser)
            try:
                self.spyIndex.remove(loser)
            except:
                pass

            if len(self.spyIndex)==0:
                self.log("平民获胜! 游戏结束!")
                self.log(self.ending)

            elif len(self.spyIndex)>=len(self.players)/2 or self.round==self.maxRound:
                self.log("卧底获胜! 游戏结束!")
                self.log(self.ending)
            else:
                self.gameLoop()

        

    def broadcast(self,playerIndex,content):
        #广播信息

        self.context+=f"{content}\n"

        if playerIndex != -1:
            response = self.players[playerIndex].send(self.context)

            self.context+=f"{self.players[playerIndex].name}:{response}\n"

            return response
        

    def log(self,content):
        #标准输出函数,方便日后更换为web api
        print("[LOG] "+content)



if __name__ == '__main__':

    player1 = player("玩家1")
    player2 = player("玩家2")
    player3 = player("玩家3")

    testGame = game({
        "name":"测试比赛",
        "description":"本场比赛用于测试程序逻辑的完备性",
        "spyNum":1,
        "words":{
            "civilian":"苹果",
            "spy":"橙子"
        },
        "maxRound":10
    })

    testGame.addPlayer(player1)
    testGame.addPlayer(player2)
    testGame.addPlayer(player3)

    testGame.start()