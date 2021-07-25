#Q1

def test1(num):
    f=1
    for i in range(1,num+1):
        f=f*i
    return f

test1(6)

#Q2

def test2(num):
    for i in range(1,11):
        print("{} * {} = {}".format(num,i,num*i))

num=int(input("Enter the input "))        
test2(num)

#Q3

def test3(num):
    a,b=0,1
    while True:
        print(a)
        a,b=b,a+b
        if a>num:
            break
        
test3(19)

#Q4

def test4(num):
    s=0
    temp=num
    while(temp!=0):
        d=temp%10
        s=s+d**3
        temp=int(temp/10)
    if s==num:
        return "Armstrong"
    else:
        return("Not Armstrong")
    
test4(153)

#Q5

x=int(input("Starting number "))
y=int(input("Ending number "))

for i in range(x,y+1):
    if test4(i)=="Armstrong":
        print(i)
        
#Q6
num = int(input("Limit "))
s=0
for i in range(1,num+1):
    s=s+i
print(s)



    














