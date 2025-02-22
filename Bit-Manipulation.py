# What is Bit Manipulation?
# Bit manipulation is the process of using bitwise operators to perform operations directly on binary numbers (bits). Since computers store data in binary (0s and 1s), bit manipulation allows us to optimize algorithms for speed and memory efficiency.

# Why Use Bit Manipulation?
# ✅ Faster than arithmetic operations.
# ✅ Helps in solving problems like subsets, XOR operations, parity checks, and more.
# ✅ Reduces space complexity in some cases.

# Decimal to binary 
def decimaltobinary(n):
    result  = ''
    while n >0 :
        if n == 0:
            return 0
        rem = str(n%2)
        n = n//2
        result += rem
    return result[::-1]
decimaltobinary(25)

# Binary to decimal 
def decimaltobinary(binary):
    result = 0
    string  = str(binary)
    power = 0
    lenth = len(string)-1
    for i in range(lenth,-1,-1) :
        res = int(string[i])*(2**power)
        power += 1
        result += res
    return result 
decimaltobinary(10001)



# Operator	Symbol	
# AND	         &	
# OR	`	`	 |
# XOR	           ^	
# NOT	         ~	
# Left Shift	 <<	
# Shifts bits left   >>

print(5 & 4)
print(5  | 4)
print(5 ^ 4)
print(5  >> 4)
print(5 << 4)




 




    

