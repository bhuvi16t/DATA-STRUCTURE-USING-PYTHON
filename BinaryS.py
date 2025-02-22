class BinarySearch:

    def __init__(self, arr, key):
        self.arr = arr
        self.key = key
        self.search()

    def search(self):
        l = 0
        r = len(self.arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if self.key == self.arr[mid]:
                print('Found at index :', mid)
                return mid
            elif self.key > self.arr[mid]:
                l = mid + 1
            else:
                r = mid - 1
        print('Element not found')
        return -1

myarr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


bs = BinarySearch(sorted(myarr),10)

