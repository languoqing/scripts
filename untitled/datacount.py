"""
统计压测数据
"""
import os
import logging
logging.basicConfig(level=logging.INFO)
loger = logging.getLogger(__name__)
loger.setLevel(logging.INFO)

def oprateFlie(sourcefile,oprate):
    os.popen("grep {} {} > {}.log".format(oprate,sourcefile,oprate))
    return

def timeFile(oprate):
    loger.info('开始处理每个时间段数据')
    os.popen("egrep -w '\s+?[0-9][0-9]\.[0-9][0-9][0-9]ms$' {}.log > {}_99.log".format(oprate,oprate))#100以内
    os.popen("egrep -w '\s+?1[0-9][0-9]\.[0-9][0-9][0-9]ms$' {}.log > {}_100.log".format(oprate,oprate))#100-200
    os.popen("egrep -w '\s+?2[0-9][0-9]\.[0-9][0-9][0-9]ms$' {}.log > {}_200.log".format(oprate, oprate))#200-300
    os.popen("egrep -w '\s+?[3-9][0-9][0-9]\.[0-9][0-9][0-9]ms$' {}.log > {}_300.log".format(oprate, oprate))#300以上
    os.popen("egrep -w '\s+?[0-9][0-9][0-9][0-9]\.[0-9][0-9][0-9]ms$' {}.log > {}_1000.log".format(oprate, oprate))#1000以上
    os.popen("egrep -w '\s+?[0-9][0-9][0-9][0-9]\.[0-9][0-9][0-9]ms$' {}.log >> {}_300.log".format(oprate, oprate))#追加到300统计
    loger.info('处理完成')
    return
def countFile(oprate,time):
    file_count = 0
    if time == '0':
        loger.info('a统计每个操作的数量，当前操作为{},time为{}'.format(oprate,time))
        with open('{}.log'.format(oprate)) as f:
            loger.info('a{}{}开始统计'.format(oprate,time))
            for i in f.readlines():
                for line in i:
                    file_count += 1
            loger.info('a完成操作{}时间{}的统计'.format(oprate,time))
    else:
        loger.info('b开始统计每个时间段的数量，当前操作为{}时间段为{}'.format(oprate,time))
        print(time)
        with open('{}_{}.log'.format(oprate,time)) as f:
            loger.info('b{}{}开始统计'.format(oprate, time))
            for i in f.readline():
                for line in i:
                    file_count+=1
            loger.info('b完成操作{}时间{}的统计'.format(oprate, time))

    return file_count

if __name__ == '__main__':
    oprate = ['hit', 'peng', 'gang', 'pass', 'hu', 'take']
    time = ['0','99','100','200','300','1000']
    result = {}
    sourcefile = input("请输入你要取数据的文件：")
    for i in oprate:
        oprateFlie(sourcefile,i)
        loger.info('操作 {} 筛选完成'.format(i))
        timeFile(i)
        loger.info('每个时间段筛选完成')
        for x in time:
            if x == '0':
                loger.info('获取每个操作的数据 tiem是{}'.format(x))
                result[i] = countFile(i, x)
                loger.info('操作总数统计完成，开始写入')
                with open('result.log','a+') as f:
                    f.write('{}的总数为：{}\n'.format(i,result[i]))
                    loger.info('操作总数写入完成')
            else:
                loger.info('操作每个时间段的统计开始，当前操作为 {} ，时间段为 {}'.format(i,x))
                result['{}_{}'.format(i,x)] = countFile(i,x)
                loger.info('单个时间段统计结果开始写入，当前操作为 {} ,当前时间段为{}'.format(i,x))
                with open('result.log','a+') as f:
                    f.write('{}_{}的总数为:{},其中的占比为：{}\n'.format(i,x,result['{}_{}'.format(i,x)],result['{}_{}'.format(i,x)]/result[i]*100))
                    loger.info('写入完成')




