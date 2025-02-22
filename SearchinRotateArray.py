# Search in Rotate array 

# binary search 

def binarySearch(arr, lo, hi, x):
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == x:
            return mid
        if arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

#function for find pivot
#  
def findPivot(arr,lo,hi) :
    
    while lo < hi:

        # The current subarray is already sorted,
        # the minimum is at the low index
        if arr[lo] <= arr[hi]:
            return lo

        mid = (lo + hi) // 2

        # The right half is not sorted. So
        # the minimum element must be in the
        # right half.
        if arr[mid] > arr[hi]:
            lo = mid + 1

        # The right half is sorted. Note that in
        # this case, we do not change high to mid - 1
        # but keep it to mid. The mid element
        # itself can be the smallest
        else:
            hi = mid

    return lo

def search(arr,key):
    n = len(arr)

    pivot = findPivot(arr,0,n-1)

    if arr[pivot] == key :
        return pivot 
    
    elif pivot == 0 :
        return binarySearch(arr,0,n-1,key)
    
    if arr[0] <= key:
        return binarySearch(arr, 0, pivot - 1, key)
    return binarySearch(arr, pivot + 1, n - 1, key)

arr = [4,5,6,2,3] 
result = search(arr,2)  
print(result)


        



        




        