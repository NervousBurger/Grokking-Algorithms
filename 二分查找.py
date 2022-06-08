def binary_search(target, aList):
    high = len(aList)
    low = 0
    while low <= high:
        mid = (low + high) // 2
        guess = aList[mid]
        
        if guess == target:
            return mid
        if guess < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(binary_search(17, [1,3,5,7,9]))
