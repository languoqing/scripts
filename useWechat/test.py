import itchat

itchat.login()
itchat.send(u'hello','fliehelp')
friends = itchat.get_friends(update=True)[0:]
print(friends)
male = female = NoneMale = 0
#微信第一个是自己
for i in friends[1:]:
    sex = i['Sex']
    nickname = i['NickName']
    RemarkName = i['RemarkName']
    if sex == 1:
        male += 1
        print(nickname,RemarkName)
    elif sex == 0:
        female += 1
        print(nickname, RemarkName)
    else:
        NoneMale += 1
        print(nickname, RemarkName)
print('男性好友：%s  女性好友：%s     ,其他：%s  ' % (male,female,NoneMale))
