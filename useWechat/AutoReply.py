import itchat
import time
@itchat.msg_register('Text')
def text_reply(msg):
    if not msg['FromUserName'] == myUserName:
        itchat.send_msg("%s 收到好友@ %s 的信息： %s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),msg['User']['NickName'],msg['Text']),'filehelp')
        return '我记下了你的消息，看到时给你回复，谢谢'

if __name__ == '__main__':
    itchat.auto_login()
    myUserName = itchat.get_friends(update=True)[0]["UserName"]
    itchat.run()