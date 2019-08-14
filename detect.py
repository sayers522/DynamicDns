#!/usr/bin/python
# -*- coding: UTF-8 -*-
from json import load
from urllib2 import urlopen
import os,socket
import BaiduSDK

#def getIpRecord(domain):
#  try:
#    addr = socket.getaddrinfo(domain, 'http')
#    old_ip = addr[0][4][0]
#  except:
#    old_ip = 'null'
#  return old_ip
  

def diffIp(domain):
  my_ip = load(urlopen('http://jsonip.com'))['ip']
  rid,rdata = BaiduSDK.getRecord(domain)
  if rdata == "error":
    print 'Failed Connect Dns Service'
    return False
  elif rdata == "none":
    BaiduSDK.addRecord(domain,my_ip)
  elif rdata != my_ip:
    print rdata,my_ip
    BaiduSDK.updateRecord(domain,my_ip,rid)

if __name__ == '__main__':
  diffIp('qnap1.sayers.top')
