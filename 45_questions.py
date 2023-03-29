# check if the given number is prime or not
a=int(input("Enter the number : "))
if (a%2 == 0):
    print("number is not prime number ")
else:
    print("number is prine")
    
    
    
# print the factorial number of input number
a=int(input("Enter the number : "))
factorial=1
for i in range(1,a+1):
    factorial=factorial*i
    print(f"the factorial of this number is {factorial}")
    