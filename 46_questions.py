"""
pattern : pyramid

      *
    * * *
  * * * * *
* * * * * * *

"""

rows = int(input("Enter number of rows: "))

k = 0
#this loop is for managing the row
# rows+1 because in range it consider start to n-1
for i in range(1, rows+1):
    # this for loop is for managing the spaces.
    # spaces = total. rows - i; (spaces = 4 - 1 => 3)
    for space in range(1, (rows-i)+1):
        print(end="  ")
   
    # this loop is for managing the star (*)
    # stars = row * 2 - 1 (star = 2nd * 2 - 1 => 3)
    while k!=(2*i-1):
        print("*", end=" ")
        k += 1
   
    k = 0
    print()
