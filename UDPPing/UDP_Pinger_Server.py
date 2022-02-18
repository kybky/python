from socket import *
import random
#设置服务器地址和端口号
ip_port=('127.0.0.1',12000)
#创建一个UDP套接字（SOCK_DGRAM）
serverSocket = socket(AF_INET, SOCK_DGRAM)
#服务器调用 bind() 指定服务器的套接字地址和端口
serverSocket.bind( ip_port)
#服务器启动信息
print("Started UDP server on port 12000")
while True:
    #生成一个指定范围内的整数
    rand = random.randint(0,10)
    #recvfrom() 等待接收数据
    message, address = serverSocket.recvfrom(1024)
    #将字符串中的小写字母转为大写字母
    message = message.upper()
    #模拟 30% 的数据包丢失
    if rand<4:
        continue
    #关闭套接字
    serverSocket.sendto(message, address)
