# 插入排序
def swap(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp

def insertionSort(list, n):
    for i in range(1,n):
        pass