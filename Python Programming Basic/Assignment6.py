#Q1

def test1(num):
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
        if a>num:
            break
gen=test1(20)

for i in gen:
    print(i)
    
#Q2

def fact(num):
    f=1
    for i in range(2,num+1):
        f=f*i
    return f

def test2(num):
    for i in range(1,num+1):
        yield fact(i)

num=int(input("Enter the number\n"))
for i in test2(num):
    print(i)
    
    
#Q3

h=float(input("Height in meters\n"))
w=float(input("Weight in kg\n"))
print("BMI = ",w/(h*w))


#Q4

import math

math.log(10)


#Q5

def test3(num):
    for i in range(1,num+1):
        yield i**3

n=int(input("Enter the number\n"))
for i in test3(n):
    print(i)

