a=int(input("enter your number: "))
if(a>18 and a<100):# here we uses (and) where it will onlu run true when both the bool. are true
    print("you can vote")
else:
    print("you can't vote")

if(a>18 or a>=18):#here we uses (or) where it will only run true when any one bool. statment is true 
    print("you can vote")
else:
    print("you can't vote'")