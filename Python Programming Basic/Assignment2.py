#Q1

def test1(km):
    return 0.621371*km

test1(10)

#Q2

def test2(cel):
    return (cel*9/5)+32

test2(37)

#Q3

import calendar
print(calendar.month(2021,7))

#Q4
#ax2 + bx + c = 0
import math

def test3(a,b,c):
    try:
        x1= (-b + math.sqrt(b**2-4*a*c))/2*a
        x2= (-b - math.sqrt(b**2-4*a*c))/2*a
    except:
        return "Imaginary number"
    else:
        return (x1,x2)    
    
    
    
a = float(input("Enter value of a "))
b = float(input("Enter value of b "))
c = float(input("Enter value of c "))
test3(a,b,c)

#Q5

a,b=5,10
b,a=a,b


