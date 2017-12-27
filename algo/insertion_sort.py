# 插入排序
def swap(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp

def insertionSort(list, n):
    for i in range(1, n):
        for j in range(i, 0, -1):
            if list[j] < list[j - 1]:
                swap(list, j, j - 1)

test = [3, 5, 2, 1, 7, 4, 9]
print(test)
insertionSort(test, 7)
print(test)


