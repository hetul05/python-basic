# take  user input and check for the greater among all 
a=int(input("Enter your marks : "))
b=int(input("Enter your marks : "))
c=int(input("Enter your marks : "))
d=int(input("Enter your marks : "))

if(a>b) and (a>c) and (a>d):
    print("greater is",a)
elif(b>a) and (b>c) and (b>d):
    print("greater is",b)
elif(c>a) and (c>b) and (c>d):
    print("greater is",c)
elif(d>a) and (d>b) and (d>c):
    print("greater is",d)
