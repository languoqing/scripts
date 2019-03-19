import redis
import logging
logging.basicConfig(level=logging.INFO,format='')
loger = logging.getLogger(__name__)
loger.setLevel(logging.INFO)

#建立连接
redisobj = redis.Redis(host='',port=6379,db=1,password='redis123')
loger.info('redis连接成功')
