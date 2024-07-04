#!/usr/bin/python2
# -*- coding: UTF-8 -*-
from json import load
from urllib2 import urlopen
from datetime import datetime
import BaiduSDK

def diffIp(domain):
  ts = '[%s] ' % datetime.now()
  #获取本机实时公网IP
  my_ip = urlopen('https://checkip.amazonaws.com/').read().strip()

  #调用百度云的域名sdk,获取域名对应的解析记录ID和解析IP地址
  rid,rdata = BaiduSDK.getRecord(domain)

  #SDK调用失败
  if rdata == "error":
    print ts + 'Failed to connect Dns service'
    return False
  #当前域名没有解析记录，使用当前主机公网IP，创建一条新的解析记录
  elif rdata == "none":
    print ts + 'No such DNS record, creating a new one'
    BaiduSDK.addRecord(domain,my_ip)
    return True
  #公网IP发生了变化，和DNS解析记录的IP地址不同，更新解析记录
  elif rdata != my_ip:
    print ts + "The ip has changed: %s -> %s" % (rdata,my_ip)
    BaiduSDK.updateRecord(domain,my_ip,rid)
    return True
  #公网IP没发生变化，不需要更新DNS
  else:
    print ts + "Not change: %s" % my_ip
    return True

if __name__ == '__main__':
  diffIp('example.domain.com')
