#coding=utf-8
import itchat
from itchat.content import *

@itchat.msg_register([PICTURE,TEXT])
def simple_reply(msg):
    ReplyContent='nice to meet you'
    if msg['Type'] == TEXT:
        ReplyContent = 'I received message: '+msg['Content']
    if msg['Type'] == PICTURE:
        ReplyContent = 'I received picture: '+msg['FileName']
    itchat.send_msg(ReplyContent,msg['FromUserName'])
itchat.auto_login()
itchat.run()
