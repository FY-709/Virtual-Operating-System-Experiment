### 项目简介

​		本项目为《操作系统》的虚拟实验系统，结合操作系统中的理论知识设计了两类实验：动画演示实验和学生交互实验。采用交互的方式让学生在线编程，再用图形化方式直观形象地展示程序的动态执行过程。本项目以 Vue 实现《操作系统》中的各种算法，使用 CreateJS 实现实验演示动画，并基于 Docker 编写了在线编译器。共包含四个实验，分别为进程调度模拟实验、银行家算法实验、动态分区模拟实验和页面置换算法实验。

​		**此项目为多人合作完成，本人只负责了部分内容的编写。**

![虚拟实验系统](https://s2.loli.net/2022/03/13/g4AE1wQ8cFlyOPI.png)



### 进程调度模拟实验

![进程调度模拟实验](https://s2.loli.net/2022/03/13/iOxXgR435dS2IZk.png)

​		该实验平台提供了四种算法（FCFS，SJF，RR，HRRN）：![四种算法](https://s2.loli.net/2022/03/13/RIxTk7Nr4Qucfe3.png)

​		选择FCFS算法，开始实验，添加四个进程：![FCFS算法](https://s2.loli.net/2022/03/13/RBA4qQrHY68MJwV.png)

​		FCFS算法是按照进程就需的先后顺序来调度进程的，越早到达的进程越先执行，点击“添加”按钮添加进程（最多添加四个），四个进程P1，P2，P3，P4的到达时间（数值只能是整数）分别设置为0，1，3，5，分配的要求执行时间（数值只能是整数）分别为3，7，2，1。按照FCFS算法的要求，第一个运行的程序为最先到达的进程，因此P1第一个执行，P1执行完成后，P2处于就绪队列，故P2先执行。按照此规律，进程运行的顺序为P1->P2->P3->P4。点击“运行”按钮，运行过程及运行结果如下图所示：

![运行过程](https://s2.loli.net/2022/03/15/maCQEv7MWkVLGnS.png)![运行结果](https://s2.loli.net/2022/03/13/1dPEQVslnRH5Cxj.png)

​		平均周转时间及平均带权周转时间：![平均周转时间及平均带权周转时间](https://s2.loli.net/2022/03/13/KnoCkAtQ84MuIOw.png)

​		刷新界面，重新选择进程算法，完成剩下三个算法，观察动态图像化过程，对四个算法进行比较，讨论优缺点。

![重新选择进程算法](https://s2.loli.net/2022/03/13/r4573pNJIKynzCU.png)



### 银行家算法实验

![银行家算法实验](https://s2.loli.net/2022/03/13/nwKToYVaRrZegzs.png)

​		点击“添加”按钮添加三类资源R1，R2，R3，设置最大资源数，设置R1，R2，R3的最大资源数分别为8，3，6。![添加三类资源](https://s2.loli.net/2022/03/13/ocgyjVe9LrlbS8F.png)

​		点击“输入”按钮，进入进程资源分配界面，点击“添加”添加进程P1，P2，P3，并添加进程的资源分配数和资源需求总量。

![进程资源分配](https://s2.loli.net/2022/03/13/hv52XO8bYCq6xrf.png)![进程资源分配](https://s2.loli.net/2022/03/13/x1CViEyacLXrekN.png)

​		判断系统是否处于安全状态，在此次此实验中，能够找到一个安全序列，所以可以进行资源分配。点击“运行”按钮，生成安全序列P3=>P2=>P1。存在安全序列即表示系统安全。

![判断系统是否处于安全状态](https://s2.loli.net/2022/03/13/I71jfnavPxy2YJm.png)

​		刷新界面，重新添加资源数和进程数，观察动态图像化过程，判断如何添加才能使进程处于安全状态。

![重新添加资源数和进程数](https://s2.loli.net/2022/03/13/Kg6zVhX32JpTBHx.png)



### 动态分区模拟实验

![动态分区模拟实验](https://s2.loli.net/2022/03/13/mQ9cRzFuHMV1vLN.png)

​		点击“初始化”按钮，初始化已分区表，系统给定一部分已经被使用的分区：![初始化已分区表](https://s2.loli.net/2022/03/13/7q2RNunPOatmdse.png)![已经被使用的分区](https://s2.loli.net/2022/03/13/pf7sO8juyd3KTY2.png)

​		此时可以看到已经有四个部分已经分区，分别是作业1，起始地址为0K，作业大小为10K；作业2，起始地址为35K，作业大小为10K；作业3，起始地址为55K，作业大小为12K；作业4，起始地址为80K，作业大小为10K。

​		此时需要使用空闲分区。操作系统接纳用户作业后，必须从空闲分区表或空闲分区链中按照一定的算法分配算法并分配空闲分区给用户作业。点击“添加作业”按钮，添加作业5，作业大小为11K（必须逐一添加作业，且最多添加3个）。![image-20220313235227865](https://s2.loli.net/2022/03/13/WdvTcPpyMDXfnoC.png)

​		实验中共有三种算法供选择，分别是最先适应算法，最佳适应算法以及最差适应算法。以最佳适应算法为例，选择“最佳适应算法”，此时空闲区表中按地址递增，分配作业5，空闲区表如图所示。此时有限分配低地址空闲分区，故该作业占据了15K-26K空闲分区：

![三种算法](https://s2.loli.net/2022/03/13/YeAB8Uw7jTlHsIk.png)![空闲区表](https://s2.loli.net/2022/03/13/1UJ6kKp2IhdR9mS.png)

​		再添加一个作业6，作业大小为10K，此时空闲分区26K-35K不满足，按照优先分配低地址空闲分区原则，故分配45K-55K给作业6：![优先分配低地址空闲分区](https://s2.loli.net/2022/03/13/e5cE4oyzjLCVIaJ.png)

​		按上述步骤添加作业7，作业大小为2K，分配结果如图所示：

![分配结果](https://s2.loli.net/2022/03/13/Svx7TDsnKUIiZ5M.png)

​		刷新界面，重新选择动态分区算法，完成剩下两个算法，观察动态图像化过程，对三个算法进行比较。



### 页面置换算法实验

![页面置换算法实验](https://s2.loli.net/2022/03/13/DXirvVY5gtePEfN.png)

​		当进程产生缺页中断时，若内存已无空闲空间，为保证该进程能正常运行，系统必须依据一定的算法从内存中选择某页程序或数据送到磁盘的交换区中，所采用的算法称为页面置换算法。以最佳置换算法为例，选择Optimal算法，输入页面访问串1,2,3,4,2,6,2,1,2,3,7,6，物理块设置为4个，点击“运行”按钮，此时缺页次数，置换次数等数据会显示在运行结果上。

![Optimal算法](https://s2.loli.net/2022/03/13/C9RrapfP8BnFvA2.png)![运行结果](https://s2.loli.net/2022/03/13/n1BRZU2O8z9VEae.png)

​		刷新界面，重新选择页面置换算法，完成剩下两个算法，观察动态图像化过程，对三个算法进行比较。根据图像化实验及原理完成代码部分实验。

![image-20220314000016402](https://s2.loli.net/2022/03/14/yQXT2tUKgOcZfB3.png)