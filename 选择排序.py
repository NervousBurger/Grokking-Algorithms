def findSmallest(arr):
    tmp = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < tmp:
            tmp = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest_item = arr[findSmallest(arr)]
        newArr.append(smallest_item)
        arr.pop(findSmallest(arr))
    return newArr
    

def selectionSort_1(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

print(selectionSort([5,3,6,2,10]))
print(selectionSort_1([5,3,6,2,10]))
