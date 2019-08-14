#!/usr/bin/python
# -*- coding: UTF-8 -*-
from json import load
from urllib2 import urlopen
import BaiduSDK

def diffIp(domain):
  #获取本机实时公网IP
  my_ip = load(urlopen('http://jsonip.com'))['ip']

  #调用百度云的域名sdk,获取域名对应的解析记录ID和解析IP地址
  rid,rdata = BaiduSDK.getRecord(domain)

  #SDK调用失败
  if rdata == "error":
    print 'Failed to connect Dns service'
    return False
  #当前域名没有解析记录，使用当前主机公网IP，创建一条新的解析记录
  elif rdata == "none":
    print 'No such DNS record, creating a new one'
    BaiduSDK.addRecord(domain,my_ip)
    return True
  #公网IP发生了变化，和DNS解析记录的IP地址不同，更新解析记录
  elif rdata != my_ip:
    print "The ip has changed: %s -> %s" % (rdata,my_ip)
    BaiduSDK.updateRecord(domain,my_ip,rid)
    return True
  #公网IP没发生变化，不需要更新DNS
  else:
    print "Not change: %s" % my_ip
    return True

if __name__ == '__main__':
  diffIp('example.domain.com')
