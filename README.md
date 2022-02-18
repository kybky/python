# **基于UDP进行通信的Ping程序**

## **一、目的**

编程实现一个简单的， 非标准的，基于 UDP 进行通信的 Ping 程序。客户
端程序发送一个 ping 报文，然后接收一个从已经提供的服务器上返回的对应 ping
报文，并计算出从该客户发送 ping 报文到接收到 ping 报文为止的往返时延（Round-Trip
Time，RTT），进行10次操作，对于每个报文，当对应的 ping
报文返回时，客户端程序要确认并打印输出 RTT
值；在整个执行过程中，客户端程序需要考虑分组丢失情况，客户端最多等待 1
秒，超过该 时长则打印丢失报文

## **二、原理**

UDP
作为一种传输层协议，只提供了无连接通信，且不对传送的数据包进行可靠性保证，因此
只适合于一次传输少量数据的应用场景，如果在传输过程中需要保证可靠性，则这种可靠性应该由
应用层负责。本实验创建的 Ping
程序正是一种不需要保证可靠性的程序，并需要利用这种不可靠性
来测量网络的联通情况。

虽然 UDP 不保证通信的可靠性，包到达的顺序，也不提供流量控制。但正是因为 UDP
的控制选
项较少，所以在数据传输过程中延迟小、数据传输效率高，一些对可靠性要求不高，但对性能等开销
更敏感的应用层协议会选择基于 UDP 进行实现，常见的使用 UDP 的应用层协议包括
TFTP、SNMP、 NFS、DNS、BOOTP 等，通常占用
53（DNS）、69（TFTP）、161（SNMP）等端口

基于 UDP 的无连接客户/服务器在 Python 实现中的工作流程如下：

1\. 首先在服务器端通过调用 socket() 创建套接字来启动一个服务器；

2\. 服务器调用 bind() 指定服务器的套接字地址，然后调用 recvfrom() 等待接收数据。

3\. 在客户端调用socket() 创建套接字，然后调用 sendto() 向服务器发送数据。

4\. 服务器接收到客户端发来的数据后，调用sendto() 向客户发送应答数据，

5\. 客户调用 recvfrom() 接收服务器发来的应答数据。

6\. 一旦数据传输结束，服务器和客户通过调用 close() 来关闭套接字。

注意在不同的计算机语言实现中，上述调用的名字和具体工作流程可能略有不同。基于
Python 的 UDP 程序工作详细流程如图2.1–1所示。

![](https://github.com/kybky/python-software/blob/main/image/1.png)

基于 Python 进行 UDP 消息的接收操作时，Python
程序将工作在阻塞状态，即未收到数据包时， Python
程序将挂起等待而不会继续执行。如果程序运行中网络连接出现了问题，导致数据包无法ࣿ
时到达，这种阻塞式的工作模式将会严重的干扰程序的执行。为了解决这个问题，Python
的套接字通信库提供了一种“超时”机制来防止程序卡死。在 Python
套接字程序中，套接字对象提供了一个 settimeout() 方法来限制 recvfrom()
函数的等待时间，当 TGEXHTQO函数阻塞等待超过这个时
间（一般称为“超时时间”）后仍然没有收到数据时，程序将会抛出一个异常来说明发生了等待数据
接收超时事件。在编写 Python
网络通信程序时，可以利用这个机制来判断是否接收数据超时。

## **三、测试过程**

**启动服务端**

运行UDP_Pinger_Server.py

![](https://github.com/kybky/python-software/blob/main/image/2.png)

**启动客户端**

在终端输入**python UDP_Pinger_Client.py 127.0.0.1 12000** 回车

![](https://github.com/kybky/python-software/blob/main/image/3.png)

如图，第一次和第四次未在1秒内响应，打印了“Request timed
out.”,其他成功打印了响应消息，计算所有 ping
消息的最小minRTT为0.00000s、最大maxRTT为1.01426s和平均
avgRTT为0.20167s，并计算丢包率为20.00%。
****
# **简单Web服务器**

## **一、目的**

利用 Python 开发一个可以一次处理一个 HTTP 请求的 Web
服务器，该服务器可以接受并解析 HTTP 请求，然后从服务器的文件系统中读取被 HTTP
请求的文件，并根据该文件是否存在而向客 户端发送正确的响应消息

## **二、原理**

基于 TCP 的面向客户端/服务器在 Python 实现中的的工作流程是：

1.  首先在服务器端通过调用 sock() 创建套接字来启动一个服务器；

    2\. 服务器调用 bind() 绑定指定服务器的套接字地址（IP 地址 + 端口号）；

    3\. 服务器调用 listen() 做好侦听准备，同时规定好请求队列的长度；

    4\. 服务器进入阻塞状态，等待客户的连接请求；

    5\. 服务器通过 accept() 来接收连接请求，并获得客户的 socket 地址。

    6\. 在客户端通过调用 socket() 创建套接字；

    7\. 客户端调用connect() 和服务器建立连接。

    8\. 连接建立成功后，客户端和服务器之间通过调用 read() 和 write()
    来接收和发送数据。

    9\. 数据传输结束后，服务器和客户各自通过调用 close() 关闭套接字。

    注意在不同的计算机语言实现中，上述调用的名字和具体工作流程可能略有不同。基于
    Python 的 TCP 客户端/服务器具体工作流程如图2.2–1所示。

![](https://github.com/kybky/python-software/blob/main/image/4.png)

## **三、测试过程**

**1、本机测试**

在同一个文件夹下写一个hello.html

![](https://github.com/kybky/python-software/blob/main/image/5.png)

代码：

    \<html\>
    
    \<head\>
    
    \</head\>
    
    \<body\>
    
    \<h1\>hello,this is my Curriculum design!\</h1\>
    
    \</body\>
    
    \</html\>

回到webserver.py,点击运行：

显示Read to serve...启动成功

![](https://github.com/kybky/python-software/blob/main/image/6.png)

在浏览器中输入 <http://127.0.0.1:6789/hello.html>（同一文件夹中存在）

![](https://github.com/kybky/python-software/blob/main/image/7.png)

在浏览器中输入 <http://127.0.0.1:6789/no.html>（文件夹中不存在）,显示404

![](https://github.com/kybky/python-software/blob/main/image/8.png)

命令框继续，并没有因为访问一遍而关闭。

![](https://github.com/kybky/python-software/blob/main/image/9.png)

**2、多线程记录：**

将bing()中的‘’回环地址改为本机IP，打开两台虚拟机，一台win7,一台kali.

**处于同一网段下**，在虚拟机的浏览器中输入<http://192.168.140.1:6789/hello.html>

显示结果成功！两台虚拟机都能访问服务器，实现了能够同时处理多个请求的多线程服务器

serverSocket.bind(("192.168.140.1", serverPort))

![](https://github.com/kybky/python-software/blob/main/image/10.png)

![](https://github.com/kybky/python-software/blob/main/image/11.png)

服务器仍继续运行，并未因为一个访问导致关闭而其他主机无法访问的现象！

![](https://github.com/kybky/python-software/blob/main/image/12.png)
****
# **简单的 SMTP 客户端程序**

## **一、目的**

通过 Python
编写代码创建一个可以向标准电子邮件地址发送电子邮件的简单邮件客户端。该客
户端可以与邮件服务器创建一个 TCP 连接，并基于 SMTP
协议与邮件服务器交互并发送邮件报文， 完成邮件发送后关闭连接。

## **二、原理**

简单邮件传输协议（Simple Mail Transfer
Protocol，SMTP）是实现电子邮件收发的主要应用层 协议，它基于 TCP
提供的可靠数据传输连接，从发送方的邮件服务器向接收方的邮件服务器发送邮
件。注意，虽然一般情况下邮件总是从发送方的邮件服务器中发出，但是工作在发送方邮件服务器
上的发送程序是一个 SMTP 客户端，因此一个完整的 SMTP
程序总有两个部分参与工作：运行在发 送方邮件服务器的 SMTP
客户端和运行在接收方邮件服务器的 SMTP 服务器。

SMTP 是一个古老的应用层协议，1982 年在 RFC 文档 821 中首次被定义，然后在 2001 和
2008 年进行了两次更新，分别为 RFC 2821 和 RFC 5321。因此虽然 SMTP
拥有众多出色的性质，但也遗
留了一些陈旧特征，例如，它限制所有邮件报文的主体部分只能采用简单的 7 比特 ASCII
码表示。 所以在用 SMTP 传送邮件之前需要将二进制数据编码为 ASCII
码，在传输后再进行解码还原为二进制数据 1。

假设存在一个发送方邮件服务器，主机名为
company.com；而对应的接收方邮件服务器的主机 名为 network.net。SMTP
客户端要从地址 alice@company.com 向地址 bob@network.net 发送报文 \&Q [QW NKMG
MGVEJWR？\*QY CDQWV RKEMNGU？。以下流程展示了运行在发送方邮件服务器上的 SMTP 客
户端（C）和运行在接收方邮件服务器上的 SMTP 服务器（S）之间交换 SMTP
报文文本的实际通信 过程：

![](https://github.com/kybky/python-software/blob/main/image/13.png)

注意：以 %开头的 ASCII 码文本行是 SMTP 客户端通过 TCP 套接字发出的消息，而以 5
开 头的 ASCII 码则是 SMTP 服务器通过 TCP 套接字发出的消息。

在这个例子中，SMTP 客户端发送了 5 条命令：\*'.1（是 HELLO 的缩写）、/\#+.
(41/、4%26 61、\# 以ࣿ
37+6，这些命令都是自解释的，可以简单通过其英文含义理解。在具体消息内容部
分，客户端通过发送一个只包含一个句点的行向服务器指示消息内容的结束（注意，在实际传输时，
报文在结尾处会包含两个额外的不可打印字符：“0x0A”与“0x0D”。分别表示回车“CR”和换行
“LF”）。服务器对客户端发出的每条命令都做出了回答，其中每个回答含有一个回答码和一些英文
解释，其中的英文解释内容在实际使用时是可选的。

有一点需要注意，由于 SMTP 使用的是 TCP
连接，所以可以复用一个连接发送多封邮件。在
这种情况下，发送方在完成握手后会连续发送所有这些邮件，对每个邮件，客户端用一个新的
/\#+. (41/!!!"EQORCP[EQO
开始，并用一个独立的句点指示该邮件的结束，然后在所有邮件发送完后 才发送 QUIT
结束一次与服务器的连接

## **三、测试过程**

运行代码

![](https://github.com/kybky/python-software/blob/main/image/14.png)

邮件发送成功！

![](https://github.com/kybky/python-software/blob/main/image/15.png)

![](https://github.com/kybky/python-software/blob/main/image/16.png)

发到室友邮箱，成功！

![](https://github.com/kybky/python-software/blob/main/image/17.png)

如果没有输入授权码或未对授权码进行64位编码，则会导致如下情况，连接失败。

![](https://github.com/kybky/python-software/blob/main/image/18.png)
****
# **网易云音乐爬虫**

爬取后得到歌曲名称和歌曲href

![](https://github.com/kybky/python-software/blob/main/image/19.png)

![](https://github.com/kybky/python-software/blob/main/image/20.png)
