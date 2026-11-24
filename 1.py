
Recalled Basics of Testing and Python and solved the problem of
sorting an array of 0s, 1s, and 2s using the Dutch National Flag algorithm. The code initializes three pointers: low, mid, and high. It iterates through the array, swapping elements to ensure that all 0s are at the beginning, all 1s are in the middle, and all 2s are at the end. The final sorted array is printed at the end.


arr = [ 2,0,1,2,0,1]
low = 0
mid = 0
high = len(arr) - 1
while mid < high:
    if arr[mid] == 0:
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        mid += 1
    elif arr[mid] == 1:
        mid += 1
    else:
        arr[mid], arr[high] = arr[high], arr[mid]
        high -= 1
print(arr)     


Given an array & an integer k rotate the arr to the right by k steps efficiently.

arr = [1,2,3,4,5,6,7]
k = 3
n = len(arr)
k = k % n
arr.reverse()
arr[:k] = reversed(arr[:k])
arr[k:] = reversed(arr[k:])
print(arr)