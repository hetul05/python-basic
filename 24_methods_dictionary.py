mydict= {
    "fast":"speed",
    "hetul":"a boy",
    "marks":[1,5,4],
    "anotherdic":{"harry":"player"}
}
print((mydict.keys()))# if you print this then dict_keys will also print, so to avoid this we use list 
print(list(mydict.keys()))# print the keys but in a list
print(list(mydict.values()))# print the values but in a list
print((mydict.items()))# print the  keys and values in tuple but return them in form of list.
mydict.update({"hey":"rizz"})#update the dict 
print(mydict)
print(mydict.get("harry2"))# returns none
# print(mydict.["harry2"])# will throw an error as harry 2 iis not present