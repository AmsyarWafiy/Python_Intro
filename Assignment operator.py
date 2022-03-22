#Assignment Operator
"""
There are various compound operators in Python like a += 5
that adds to the variable and later assigns the same
Various assignment operators used in Python are

Operator	Example	    Same As
+=	      x += 3	    x = x + 3
-=	      x -= 3	    x = x - 3
*=	      x *= 3	    x = x * 3
/=	      x /= 3	    x = x / 3
%=	      x %= 3	    x = x % 3
//=	      x //= 3	    x = x // 3
**=	      x **= 3	    x = x ** 3
&=	      x &= 3	    x = x & 3
|=	      x |= 3	    x = x | 3
^=	      x ^= 3	    x = x ^ 3
>>=	      x >>= 3	    x = x >> 3
<<=	      x <<= 3	    x = x << 3
"""
num1 = 5
num2 = 5
res = num1 + num2
print("Line 1 - Result of + is ", res)
# "10"
res += num2
print("Line 2 - Result of + is ", res)
#
res -= num2  # 15 - 5 ,
print("Line 3 - Result of + is ", res)
res *= num1
print("Line 4 - Result of * is ", res)
res /= num1
print("Line 5 - Result of / is ", res)

#      3 6 1
n1 = 10 # 8/2 = 4 Remainder = 0
       # 9/2 = 1 Remainder

#-------------
n2 = 2
n1 %= n2
#-------------
n2 = 2
n1 %= n2
print("Line 6 - Result of + is ", n1)
# It will store remainder of division on the LHS

n1 = 10
n2 = 2
n1 /= n2 # 5.0
print("Line 7 - Result of + is ", n1)
# By default it will be float value in result
n1 = 10
n2 = 2
n1 //= n2 # 5
print("Line 8 - Result of + is ", n1)
# Convert into whole number

n1 = 2
n2 = 3
n1 *= n2
print("Line 9 - Result of + is ", n1)
#2*2*2 - 2 to the power 3

n1 = 5
n2 = 3
n1 **= n2 # 5*5*5
print("Line 10 - Result of + is ", n1)

n1 = 8
n2 = 5
n1 >= n2 #
print("Line 11 - Result of + is ", n1)
print("Line 11A - Result of + is ", n1 >= n2) #Display true value
n1 = 6
n2 = 7
n1 >>= n2 #
print("Line 12 - Result of + is ", n1)

n1 = 3
n2 = 2
result = n1 > n2 # True
print("Line 13 - Result of + is ", result)

n1 = 30
n2 = 6
n1 >>= n2
result = n1
print("Line 14 - Result of + is ", result)