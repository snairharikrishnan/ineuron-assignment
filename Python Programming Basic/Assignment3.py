#Q1

def test1(num):
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")
        
test1(5)
test1(-5)
test1(0)

#Q2

def test2(num):
    return "Even" if num%2==0 else "Odd"

test2(4)

#Q3

import calendar

def test3(year):
    if calendar.isleap(year):
        return "Leap Year"
    else:
        "Not leap year"

year=int(input("Enter the year "))
test3(year)

#Q4

def test4(num):
    for i in range(2,num):
        if num % i ==0:
            return "Not prime"
    return "Prime"

num=int(input("Enter the number "))
if num > 1:
    print(test4(num))
else:
    print("NA")


#Q5

for i in range(1,10001):
    if i==1:
        continue
    if test4(i) == "Prime":
        print(i)
    










