'''
decimal to binary converter

logic
given a number n, find the highest power of two that divides it
for i in range(0, 100):
if 2**i < n,
binary_num = 10^(i+1)
subtract 2**i from n
check the highest power of two that divides THAT number
etc...

48
2^5+
48-32=16
so, 2^5+2^4=110000
'''

def bin():
    n=int(input('Enter a number:')
    for i in range(1,10):
          if 2**i > n:
              binary_num=10^i
              n=n-2**(i-1)
          continue
    print(binary_num)

'''

def convertToBinary(n):
   # Function to print binary number for the input decimal using recursion
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')
# decimal number
dec = 34
convertToBinary(dec)
'''
