
# rotate array :

class rotateArray:
    def __init__(self, arr, n, d):
        self.arr = arr
        self.rev(arr, 0, d - 1)  # Reverse the first d elements
        self.rev(arr, d, n - 1)  # Reverse the remaining n-d elements
        self.rev(arr, 0, n - 1)  # Reverse the whole array
        self.show()

    def rev(self, arr, i, j):
        while i < j:  # Corrected condition
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements
            i += 1
            j -= 1

    def show(self):
        print('Rotated Array is:', self.arr)


# Example usage
l = [2, 3, 4, 5, 6]
rot = rotateArray(l, 5, 3)  # Use len(l) instead of hardcoding '5'



   
    
   
    
           