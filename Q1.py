# -*- using:utf8 -*-

"""
* Question 1:
In this programming assignment you will implement one or more of the integer multiplication 
algorithms described in lecture.

To get the most out of this assignment, your program should restrict itself to multiplying only 
pairs of single-digit numbers. You can implement the grade-school algorithm if you want, but to get the most out of the assignment you'll want to implement recursive integer multiplication and/or Karatsuba's algorithm.

So: what's the product of the following two 64-digit numbers?

3141592653589793238462643383279502884197169399375105820974944592

2718281828459045235360287471352662497757247093699959574966967627

[TIP: before submitting, first test the correctness of your program on some small test cases of 
your own devising. Then post your best test cases to the discussion forums to help your fellow students!]

[Food for thought: the number of digits in each input number is a power of 2. Does this make 
your life easier? Does it depend on which algorithm you're implementing?]

The numeric answer should be typed in the space below. So if your answer is 1198233847, then just 
type 1198233847 in the space provided without any space / commas / any other punctuation marks.

* Solution:
8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184

* Trouble shooting
use python2.x to show full digits of result
"""

import math
import sys


def karatsuba(x,y):
    sx= str(x)
    sy= str(y)
    nx= len(sx)
    ny= len(sy)
    if ny<=2 or nx<=2:
        r = int(x)*int(y)
        return r
    n = nx
    if nx>ny:
        sy = sy.rjust(nx,"0")
        n=nx
    elif ny>nx:
        sx = sx.rjust(ny,"0")
        n=ny
    m = n%2
    offset = 0
    if m != 0:
        n+=1
        offset = 1
    floor = int(math.floor(n/2)) - offset
    a = sx[0:floor]
    b = sx[floor:n]
    c = sy[0:floor]
    d = sy[floor:n]
    print(a,b,c,d)

    ac = karatsuba(int(a),int(c))
    bd = karatsuba(int(b),int(d))

    ad_bc = karatsuba((int(a)+int(b)),(int(c)+int(d)))-ac-bd
    r = ((10**n)*ac)+((10**(n/2))*ad_bc)+bd

    return r


def main():
    # transform the integer into array
    num1_str = '3141592653589793238462643383279502884197169399375105820974944592\n'
    num2_str = '2718281828459045235360287471352662497757247093699959574966967627\n'

    # calculate num
    res = karatsuba(int(num1_str), int(num2_str))
    print('     result = ', res)
    print('True result = ', int(num1_str)*int(num2_str))


if __name__ == '__main__':
    main()