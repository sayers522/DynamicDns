#!/usr/bin/python
from json import load
from urllib2 import urlopen
import os,socket


def updateDns(domain,new_ip):
  print 'update Dns with API'
  #调用域名服务商的API接口，更新DNS解析记录

def getIpRecord(domain):
  try:
    addr = socket.getaddrinfo(domain, 'http')
    old_ip = addr[0][4][0]
  except:
    old_ip = 'null'
  return old_ip
  

def diffIp(domain):
  new_ip = load(urlopen('http://jsonip.com'))['ip']
  old_ip = getIpRecord(domain)
  print old_ip,new_ip
  if old_ip != new_ip:
    updateDns(domain,new_ip)

if __name__ == '__main__':
  diffIp('example.com')
