#Q1

import numpy as np
np.lcm(4,5)


def test1(a,b):
    big=max(a,b)
    while True:
        if big%a==0 and big%b==0:
            return big
        else:
            big+=1
    
test1(10,20)

#Q2

np.gcd(4,5)


def test2(a,b):
    small=min(a,b)
    for i in range(1,small+1):
        if a%i==0 and b%i==0:
            hcf=i
    return hcf
    
test2(10,20)

#Q3

def test3(num):
    b=bin(num)
    h=hex(num)
    o=oct(num)
    return(b,h,o)
        
test3(17)

    
#Q4

def test4(c):
    return ord(c)
    
test4('|')


#Q5

def cal(a,b,op):
    if op=='+':
        return a+b
    elif op=='-':
        return a-b
    elif op=='*':
        return a*b
    elif op=='/':
        return a/b
    else:
        return "Invalid operation"

while True:
    a=int(input("Enter 2 numbers followed by operation\nGive operation . to exit\n"))
    b=int(input())
    c=input()
    if c=='.':
        print("Thank You...")
        break
    print("{} {} {} = {}".format(a,c,b,cal(a,b,c)))

    
    