# __知识点__ #
## __数据结构__ ##
1. 链表
2. 栈
3. 队列
4. 树
## __算法__ ##
## __网络__ ##
1. IPv6
2. TCP/IP
3. HTTP
4. TLS
## __存储__ ##
1. Ceph
2. 文件系统
## __操作系统__ ##
### 1. 用户态和内核态区别 ###
(1) CPU有Ring 0 1 2 3四种运行级别，不同级别能够运行不同的指令集合  
(2) 用户态和内核态是操作系统的两种运行级别，内核态运行在Ring 0，用户态运行在Ring 3  
(3) 用户态是普通用户进程运行的特权级别，是最低的特权级别  
(4) 当程序需要进行特权操作时，需要切换到内核态，如操作硬件  
(5) 程序处于用户态时，能访问的内存空间和对象受到限制，其所处于占有的处理器是可被抢占的  
(6) 程序处于内核态时，则能访问所有的内存空间和对象，且所占有的处理器是不允许被抢占的  
### 2. 关于poll epoll和select的区别 ###
(1) select，poll，epoll都是IO多路复用的机制  
(2) select通过轮询的方式，有最大连接数的限制  
(3) poll通过轮询的方式，没有最大连接数限制  
(4) epoll通过事件通知的方式，支持水平触发和边缘触发，最大连接数上限高，使用mmap的方式传递消息  
### 3. 水平触发和边缘触发的区别 ###
(1) 水平触发：当可读写事件发生时，如果此次没有把数据一次性全部读写完，会一直通知  
(2) 边缘触发: 当可读写事件发生时，如果此次没有把数据一次性全部读写完，不会重复通知，直到有下一次事件发生  
### 3. 进程间通信方式 ###
(1) 信号  
(2) 管道和命名管道，普通管道只能在父子进程或者兄弟进程中使用  
(3) 消息队列  
(4) socket  
(5) 信号量  
(6) 共享内存  
### 4. 进程线程区别 ###
(1) 进程是操作系统资源分配的基本单位  
(2) 线程是任务调度和执行的基本单位  
(3) 一个进程由一个或多个线程组成，线程是一个进程中代码的不同执行路线  
(4) 进程之间相互独立，同一进程下的各个线程之间共享程序的内存空间及资源  
(5) 线程上下文切换比进程上下文切换要快得多  
(6) 线程间可以通过直接读写同一进程中的数据进行通信，但是进程通信需要借助IPC  
### 5. 线程切换过程 ###
(1) 切出：一个线程被剥夺处理器的使用权而被暂停运行，操作系统会将线程的进度信息保存到内存  
(2) 切入：一个线程被系统选中占用处理器开始或继续运行，操作系统需要从内存中加载线程的上下文  
### 6. 什么是僵尸进程 ###
(1) 进程已经退出，而其父进程并没有调用 wait() 或 waitpid()，那么该进程的进程描述符仍然保存在系统中，这种进程称之为僵尸进程  
(2) 僵尸进程通过 ps 命令显示出来的状态为 Z(zombie)  
(3) 大量僵尸进程将占用大量PID导致系统不能产生新的进程  
(4) 消灭僵尸进程，只需要将其父进程杀死，此时僵尸进程就会变成孤儿进程，从而可以被init进程结束  
### 7. 什么是孤儿进程 ###
(1) 进程的父进程退出，但还在运行的进程  
(2) 孤儿进程会被init进程接管，所以孤儿进程不会对系统造成危害  
### 8. 死锁的必要条件 ###
(1) 互斥：每个资源要么已经分配给了一个进程，要么就是可用的  
(2) 占有和等待：已经得到了某个资源的进程可以再请求新的资源  
(3) 不可抢占：已经分配给一个进程的资源不能强制性地被抢占，它只能被占有它的进程显式地释放  
(4) 环路等待：有两个或者两个以上的进程组成一条环路，该环路中的每个进程都在等待下一个进程所占有的资源  
### 9. 死锁检测 ###
(1) 检测环路  
### 10. 死锁恢复 ###
(1) 利用抢占恢复  
(2) 利用回滚恢复  
(3) 通过杀死进程恢复  
### 11. 死锁预防 ###
(1) 破坏互斥条件：例如假脱机打印机技术允许若干个进程同时输出，唯一真正请求物理打印机的进程是打印机守护进程  
(2) 破坏占有和等待条件  
(3) 破坏不可抢占条件  
(4) 破坏环路等待：给资源统一编号，进程只能按编号顺序来请求资源  
### 12. 死锁避免 ###
(1) 安全状态：如果没有死锁发生，并且即使所有进程突然请求对资源的最大需求，也仍然存在某种调度次序能够使得每一个进程运行完毕，则称该状态是安全的
(2) 银行家算法  
### 13. ###