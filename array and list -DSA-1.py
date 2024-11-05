# python array :
# from array import *
# a1 = array('i',[1,2,3])
# print(type(a1))


# python list :
# l1= [1,2,3,3]
# l2 =[1,2,2,'bhupendra']
# print(l1,type(l1),l2,type(l2))

#  Data structure Assesment -1 

# 1.  Given an array with some integer type values. Write a python script to sort array values?

# l = [34,58,7,9,2,54,8,56]
# for i in range(len(l)):
#     for j in range(0,len(l)-1):
#         if l[i]<l[j]:
#             l[i],l[j]=l[j],l[i] 
# print(l)

# 2. Given a list of heterogenous elements. Write a python script to remove all the non int values from the list
# l=[2,7,6,2,'BHOOPENDRA',23,'harshit',53,326]
# for i in l:
#     if type(i) != int :
#         l.remove(i)
# print(l)

# 3. Write a Python script to calculate average of elements of a list.

# l = [34,58,7,9,2,54,8,56]
# sum = 0
# for i in l:
#     sum += i
    
# print(sum/len(l))
# print()

# 4. Write a Python script to create a list of first N prime numbers

# def primeNumber(n):
#     l=[]
#     for i in range(1,n+1):
#         fact =0
#         for j in range(2,n+1):
#             if i%j == 0:
#                 fact += 1
#         if fact == 1:
#             l.append(i)

#     print(l,len(l))

# primeNumber(100)
     
# 5.Write a Python script to create a list of first N terms of a Fibonacci series
def fibonacci(n):
     n1 ,n2= 0,1
     l=[]
     
     for i in range(2,n):
          n3 = n1+n2
          n1 = n2
          n2 = n3
          l.append(n3)
          
     print(l)    
        
    

n = int(input('enter a number here '))
fibonacci(n)



            
   
