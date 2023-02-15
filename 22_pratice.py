#take input for user for fruit name and put them in list
f1=input("enter fruit 1")
f2=input("enter fruit 2")
f3=input("enter fruit 3")
f4=input("enter fruit 4")
f5=input("enter fruit 5")
f6=input("enter fruit 6")
f7=input("enter fruit 7")
list=[]
list.append(f1)
list.append(f2)
list.append(f3)
list.append(f4)
list.append(f5)
list.append(f6)
list.append(f7)
print(list)

#question---write a program to accept marks of 6 students and display in themsorted manner
f1=int(input("Enter mark of 1st number:"))
f2=int(input("Enter mark of 2nd number:"))
f3=int(input("Enter mark of 3rd number:"))
f4=int(input("Enter mark of 4th number:"))
f5=int(input("Enter mark of 5th number:"))
f6=int(input("Enter mark of 6th number:"))
f7=int(input("Enter mark of 7th number:"))
list=[]
list.append(f1)
list.append(f2)
list.append(f3)
list.append(f4)
list.append(f5)
list.append(f6)
list.append(f7)
list.sort()
print(list)


# show that tuple is immutable
tuple=(14,15,12,35)
tuple.append(14)
print(tuple)
