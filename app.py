"""
    Group Chat Robot v0.1
"""
# coding: utf-8

import itchat, re
from itchat.content import *
import random
import json

"""
    Constants
"""
REPLY = {'apply_first':['你好我是小丽，省人民医院的一名护士！',
               '你离我很近啊！',
               '我是小丽，你呢！'],
         'apply_info':['我是从通讯录加的你。','我认识你的一个朋友！',
               '我也不知道怎么就把你加上了这就是缘分吧！'],
         'default': ['太棒了','真不错','好开心','嗯嗯','我在忙哦']}

@itchat.msg_register([TEXT], isGroupChat=True)
def text_reply(msg):

    if msg['User']['NickName'] == '老地方':
        print('Message from: %s' % msg['User']['NickName'])
        # 发送者的昵称
        username = msg['ActualNickName']
        print('Who sent it: %s' % username)

        match = re.search('你好', msg['Text']) or re.search('你是', msg['Text'])
        if match:
            print('-+-+' * 5)
            print('Message content:%s' % msg['Content'])
            print('工作、加班 is: %s' % (match is not None))
            randomIdx = random.randint(0, len(REPLY['apply_first']) - 1)
            itchat.send('%s\n%s' % (username, REPLY['apply_first'][randomIdx]), msg['FromUserName'])

        match = re.search('在吗', msg['Text']) or re.search('约吗', msg['Text'])
        if match:
            print('-+-+' * 5)
            print('Message content:%s' % msg['Content'])
            print('apply_first or apply_info dic is: %s' % (match is not None))
            randomIdx = random.randint(0, len(REPLY['apply_info']) - 1)
            itchat.send('%s\n%s' % (username, REPLY['apply_info'][randomIdx]), msg['FromUserName'])

        print('isAt is:%s' % msg['isAt'])

        if msg['isAt']:
            randomIdx = random.randint(0, len(REPLY['default']) - 1)
            itchat.send('%s\n%s' % (username, REPLY['default'][randomIdx]), msg['FromUserName'])
            print('-+-+'*5)

itchat.auto_login(enableCmdQR=True, hotReload=True)
itchat.run()