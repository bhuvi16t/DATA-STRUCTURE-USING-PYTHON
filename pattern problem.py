# 1. Right-Angled Triangle
# *
# * *
# * * *
# * * * *
# * * * * *
 # code for the pproblem 

def Right_angle(n):
    for i in range(n):
        for j in range(i+1):
            print('*', end=' ')
        print()


# 2. Inverted Right-Angled Triangle
# * * * * *
# * * * *
# * * *
# * *
# *
def Inverted_Right_angle(n):
    for i in range(n):
        for j in range(n-i):
            print('*', end=' ')
        print()

# 3. Pyramid Pattern
#     *    
#    * *   
#   * * *  
#  * * * * 
# * * * * *
def pyramiid(n):
    for i in range(n):
        for j in range(n-i):
            print('', end=' ')
        for  k in range(i+1):
            print('*',end=' ')
        print()


# 4. Diamond Pattern
#     *    
#    * *   
#   * * *  
#  * * * * 
# * * * * *
#  * * * * 
#   * * *  
#    * *   
#     *    
def diamond(n):
    for i in range(n):
        for j in range(n-i):
            print('', end=' ')
        for  k in range(i+1):
            print('*',end=' ')
        print()
    for i in range(n - 1, 0, -1):
      print(" " * (n - i) + " *" * i)

# 5. Hollow Square Pattern

# * * * * *
# *       *
# *       *
# *       *
# * * * * *
def hollowSquare(n):
    for i in  range(n):
        if i==0 or i==n-1:
            print("* " *n )
        else :
            print("* " + "  " * (n - 2) + "*")


# 6. Floyd’s Triangle
# 1
# 2 3
# 4 5 6
# 7 8 9 10

def floyds(row):
    n=1
    for i in range(1, row + 1):  # Loop for rows (1 to 4)
        for j in range(i):  # Loop for printing numbers in each row
            print(n, end=" ")  # Print the current number
            n += 1  # Move to the next number
        print()


# 7. Number Pyramid                                                                                                           
#     1    
#    2 2   
#   3 3 3  
#  4 4 4 4 
# 5 5 5 5 5
def  numberPyramid(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(' ',end='')
        for k in range(i):
            print(i,end=' ')
        print()

        
# 8. Pascal's Triangle
#        1
#       1 1
#      1 2 1
#     1 3 3 1
#    1 4 6 4 1

def pascal_triangle(n):
    for i in range(n):
        # Printing spaces for formatting
        print(" " * (n - i), end="")
        val = 1  # First value in every row is always 1
        for j in range(i + 1):
            print(val, end=" ")  # Print the value
            val = val * (i - j) // (j + 1)  # Update value using formula
        print()  # Move to the next line

# Call the function to print 5 rows of Pascal's Triangle
pascal_triangle(5)