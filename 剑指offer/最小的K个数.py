#题目:给定一个数组，找出其中最小的K个数。例如数组元素是4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。如果K>数组的长度，那么返回一个空的数组

#题解：堆排序：每一轮都是建最大堆，然后把最大数换到序列最后

def heapify(arr,n,i):
    #n:搜索界限
    largest = i
    l = 2*i+1
    r = 2*i+2

    if l<n and arr[i] < arr[l]:
        largest = l
    if r<n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        #换数字就要执行重新检查被换后的子节点是否比下面的大，防止小点的数值换过来后比子树小
        heapify(arr,n,largest)
    print(i,largest)

def heapSort(arr):
    n  = len(arr)
    #build maxheap,此时第一个数是最大的
    for i in range(n,-1,-1):
        heapify(arr,n,i)

    #change i each other
    for i in range(n-1,-1,-1):
        #第一个数和最后一个数互换
        arr[i],arr[0] = arr[0],arr[i]
        #去掉最后一个数（从n-1递减），继续循环：
        #这里选从0开始，是因为1,2节点已经确定比下面的大，用他们来代表最大的两个数
        heapify(arr,i,0)

arr = [ 4,5,1,6,2,7,3,8]
heapSort(arr)
n = len(arr)
print ("排序后")
for i in range(n):
    print ("%d" %arr[i])