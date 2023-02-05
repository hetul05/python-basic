a=10
b=5
c=a+b
d=a-b
e=a*b
f=a/b
# Arthimetic operators
print("the value of a+b =",c)
print("the value of a+b =",d)
print("the value of a+b =",e)
print("the value of a+b =",f)

#assignment operators
h=10
h +=5
h -=1
h *=2
h /=2
print(h)

# Comparison operators
i=2>5
j=2<5
k=(2>=5)
l=(2<=5)
m=(2!=5)# It will print true because 2 is not equal to 5,(!=)this symbol indicate not equal to
print(i,j,k,l,m)

# logical operators
n= 5>10
o= 10>5
# p=(n>o)
print(n and o )# It will print true only when both are true
print(n or o)# It will print true when one of them will be true
print(not o)# it will print the opposite (example : o is true , but it will print false)