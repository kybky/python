import sys, time
from socket import *

# 获取服务器主机名和端口作为命令行参数
argv = sys.argv                      
host = argv[1]
port = argv[2]
timeout = 1 # 以秒计
timeList = []  # 创建空列表，存放TTL
totalReq = 10  # 设置发送报文数
loseReq = 0    # 丢包数，为了后面计算丢包率
totalTime = 0  # 总时间，方便后面计算平均往返时间

# 创建UDP客户端套接字
# 注意对UDP数据包使用SOCK_DGRAM
clientsocket = socket(AF_INET, SOCK_DGRAM)
# 将套接字超时设置为1秒
clientsocket.settimeout(timeout)
# 命令行参数是字符串，请将端口改为整数
port = int(port)  
# ping消息的序列号
ptime = 0  

# Ping 10 次
while ptime < 10: 
	ptime += 1
	# 格式化要发送的消息
	data = "Ping " + str(ptime) + " " + time.asctime()
	sendTime = time.time()
	# 接收服务器响应  
    
	try:
	# 计算往返时间,往返时间是发送和接收时间之间的差
		TTL1 = time.time() - sendTime
	#发送带有ping消息的UDP数据包
		clientsocket.sendto(data.encode(),(host, port))
		# 接收服务器响应
		message, address = clientsocket.recvfrom(1024)
		# 将TTL放入列表，方便后面进行数据统计
		timeList.append(TTL1)  
		totalTime += TTL1
	# 将服务器响应显示为输出
		print("Reply from " + str(ptime) + ": " + message.decode())
		print('RTT: {:.5f} s'  .format(TTL1))
	except:
		# 计算往返时间
		TTL2 = time.time() - sendTime  
		# 将TTL放入列表，方便后面进行数据统计
		timeList.append(TTL2)  
		loseReq += 1
		totalTime += TTL2
		print ("Request timed out.")
		continue
# ping后显示最小，最大和平均RTT。另外，还需计算丢包率（百分比）
print('\n minRTT: %0.5fs\t maxRTT: %0.5fs\t avgRTT: %0.5fs'
      % (min(timeList), max(timeList), totalTime/len(timeList)))
print('\n packetLoss percent: {:.2%}'.format(loseReq/totalReq))

# 关闭客户端套接字
clientsocket.close()




