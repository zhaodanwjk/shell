#!/usr/bin/python
import re
import redis

redis_auth='xxx'
redis_server_list=[
#'10.33.4.171',
'10.33.4.172',
#'10.33.4.173',
'10.33.4.174',
#'10.33.4.175',
#'10.33.4.176',
#'10.33.4.177',
#'10.33.4.178',
#'10.33.4.179',
#'10.33.4.180',
'10.33.4.181',
'10.33.4.182',
'10.33.4.183',
'10.33.4.184',
'10.33.4.185',
]
def redis_use_status(host_name,password=redis_auth,redis_port=6379):
    m_redis=redis.StrictRedis(host=host_name,password=redis_auth,port=redis_port)
    used_db=[]
    result_used=[]
    result_free=[]
    for each_key in m_redis.info().keys():
        m_pattern=re.compile(r'db\d{1,2}')
        match = m_pattern.match(each_key)
        if match:
            each_key_num=each_key.replace('db','')
            used_db.append(int(each_key_num))
    max_db_num = max(used_db)
    for each_db_num in range(1,max_db_num+1):
        if each_db_num in used_db:
            result_used.append('db'+str(each_db_num))
        else:
            result_free.append('db'+str(each_db_num))
    print 'Redis %s have used: %s' %(host_name,result_used)
    print 'Redis %s can use: %s' %(host_name,result_free)
if __name__ == '__main__':
    for each_host in redis_server_list:
        redis_use_status(each_host)
