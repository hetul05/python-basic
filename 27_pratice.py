# question from pratice set 5
dict={
    "panchayat":"parth",
    "nonsense":"yatharth",
}
a=input("enter your word:")#it will ask for input language
print("the meaning of your word is",dict[a])# it will throw an error 
# if the key is not present
print("the meaning of your word is",dict.get(a))# it will not throw error 
# if key is not present, it will just return NONE



# question from pratice set 5
s={4,"4",4.0}
print(type(s))
print(s)
print(len(s))

