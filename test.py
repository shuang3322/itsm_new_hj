#!/usr/bin/envpython

# coding:utf-8

import os
import subprocess
import time
from multiprocessing import Pool
i = 0
def cont ():
    global i
    i = i + 1

def ping_call(num):
    fnull = open(os.devnull, 'w')
    ipaddr = 'ping 10.77.40.' + str(num)
    # result = subprocess.call(ipaddr + ' -c 1', shell=True, stdout=fnull, stderr=fnull)
    result = subprocess.call(ipaddr + ' -n 1', shell=True, stdout=fnull, stderr=fnull,)
    current_time = time.strftime('%Y%m%d-%H:%M:%S', time.localtime())
    print(result)
    if result:
        fnull.close()
        # print('时间:{} ip地址:{} ping fall'.format(current_time, ipaddr))
    else:
        print('时间:{} ip地址:{} ping ok'.format(current_time, ipaddr))
        fnull.close()
        return 1




if __name__ == '__main__':
    aaa = 0
    start_time = time.time()
    p = Pool(20)
    res_l = []
    for i in range(1, 20):
        res = p.apply_async(ping_call, args=(i,))
        res_l.append(res)
    for res in res_l:
        sss = res.get()
        aaa = aaa + sss
    i = []
    print('程序耗时{:.2f}'.format(time.time() - start_time))
    print("输出人数：%s"%(str(aaa)))
