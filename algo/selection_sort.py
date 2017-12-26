# 选择排序
def swap(list, i, j):
    temp = list[i];
    list[i] = list[j]
    list[j] = temp
test_case = [1, 4, 5, 2, 0, 7, 5, 8]
print(test_case)

def sort(n, list):
    for i in range(n):
        minIndex = i
        for j in range(i + 1, n):
            if list[j] < list[minIndex]:
                minIndex = j

        swap(list, i, minIndex)

sort(7, test_case)
print(test_case)
