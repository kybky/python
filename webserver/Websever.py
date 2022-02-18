# 导入套接字模块
from socket import * 

# 创建TCP服务器套接字
#(AF_INET 用于IPv4协议)
#(SOCK_STREAM 用于TCP)

serverSocket = socket(AF_INET, SOCK_STREAM)

# 分配端口号
serverPort = 6789

# 将套接字绑定到服务器地址和服务器端口
serverSocket.bind(("192.168.140.1", serverPort))

# 一次最多听一个连接
serverSocket.listen(1)

# 服务器应该已启动并正在运行，并且正在侦听传入的连接

while True:
	print('Ready to serve...')

	# 从客户端建立新连接
	connectionSocket, addr = serverSocket.accept()

	# 如果在try子句执行期间发生异常
	# 该子句的其余部分被跳过
	# 如果异常类型与except后面的单词匹配
	# except子句已执行
	try:
		# 从客户端接收请求消息
		message = connectionSocket.recv(1024).decode()
		# 从消息中提取请求对象的路径
		# 路径是HTTP头的第二部分，由[1]标识
		filename = message.split()[1]
		# 因为HTTP请求的提取路径包括
		# 一个字符“\”，我们从第二个字符读取路径 
		f = open(filename[1:])
		# 将请求文件的整个contenet存储在临时缓冲区中
		outputdata = f.read()
		# 将HTTP响应头行发送到连接套接字
		connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode()) 
		connectionSocket.send("<html><head></head><body><h1>hello! this is webserver</h1></body></html>\r\n".encode())
 
		# 将请求文件的内容发送到连接套接字
		for i in range(0, len(outputdata)):  
			connectionSocket.send(outputdata[i].encode())
		connectionSocket.send("\r\n".encode()) 
		
		# 关闭客户端连接套接字
		connectionSocket.close()

	except IOError:
			# 为找不到的文件发送HTTP响应消息
			connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
			connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
			# 关闭客户端连接套接字
			connectionSocket.close()

serverSocket.close()  
