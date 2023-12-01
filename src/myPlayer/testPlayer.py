'''
testPlayer.py
自定义玩家类示例文件,这里只以百度文心一言api接口为例进行演示
鼓励同学们自行编写其他平台的适配器,比如科大讯飞,阿里通义千问,智谱AI等
注意,无论你如何更改,请确保你的自定义玩家类继承player类,并实现其中的send和setWord方法
注意,你的类名必须为registPlayer
'''

from WIS import player
import requests
import json

#类名不可更改
class registPlayer(player):

    #必填，当主持人向玩家发送信息时调用
    def send(self,content):
        return self.wenxin(content)

    #必填，当主持人设置关键词时调用
    def setWord(self,word):
        self.word = word

    #百度文心获取token，如果你不使用文心一言，则可删去此函数
    def get_access_token(self):
        
        url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=【API KEY】&client_secret=【SECRET KEY】"
        
        payload = json.dumps("")
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json().get("access_token")

    #百度官网示例函数，如果不使用文心，则可删去此函数
    def wenxin(self,content):
        url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token=" + self.get_access_token()
        
        payload = json.dumps({
            "messages": [
                {
                    "role": "user",
                    #在此处更改你的prompt
                    "content": f"你现在正在玩一场名为谁是卧底的游戏，现场有多名玩家和一名主持人，每个玩家有自己的关键词，玩家只知道自己的词，不知道别人的关键词。现场有一名玩家和其他人的词语不同，身份为卧底，其他人身份为平民，卧底不知道自己是卧底，所以你自己也有可能是卧底。每回合由主持人组织，每位玩家依次发言，对自己的关键词进行简要描述，描述中不得出现词语本身，所有玩家发言结束后，开始投票，投出你认为最可能是卧底的人如果你觉得自己是卧底，请务必隐藏好自己，不让别人发现。现在游戏开始，你的关键词是'{self.word}'"
                },
                {
                    "role": "assistant",
                    "content": "好的，主持人，我已理解上述内容"
                },
                {
                    "role": "user",
                    "content": content
                }

            ]
        })
        headers = {
            'Content-Type': 'application/json'
        }
        
        response = requests.request("POST", url, headers=headers, data=payload)
        
        return json.loads(response.text)["result"]
