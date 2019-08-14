# DynamicDns
针对在百度云注册的域名，在动态公网IP环境下，通过python脚本定时检查公网IP，并通过百度云提供的域名API，将公网IP的变化，更新到域名服务的解析记录上。
针对在其他服务商注册的域名，可以自行实现域名服务API的调用，并替换guardDns.py中的BaiduSDK模块

使用方法：
1. 调用百度云的域名服务API，需要先提交工单申请开通
2. 开通API访问后，将BaiduSDK.py中第118行的YourAccessKey和YourSecretKey替换为自己的AccessKey和SecretKey
3. 将guardDns.py中diffIp函数调用的参数修改为自己的域名
4. 将guardDns.py添加到crontab定时任务，具体定时频率，可以根据动态公网IP的变化频率自行设置 
