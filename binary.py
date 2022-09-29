def binarySearch(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + ((right - left) // 2)
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1

def binarySearchRecursive(arr, left, right, target):
    if left > right:
        return -1

    mid = left + ((right - left) // 2)
    if arr[mid] == target:
        return mid
    if arr[mid] > target:
        return binarySearchRecursive(arr, left, mid-1, target)
    else:
        return binarySearchRecursive(arr, mid+1, right, target)

data = [-1,0,3,5,9,12]
target = 9

index = binarySearch(data, target)
index2 = binarySearchRecursive(data, 0, len(data)-1, target)
print(index)
print(index2)