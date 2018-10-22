#count = 1
#
#while count <= 100:
 #   if count % 2 == 0:
  #      print(count)
   # count+=1

L  = []

while len(L) < 3:
    new_name = input("Please add a new name: ").strip().capitalize()
    L.append(new_name)

print("Sorry the list is full")
print(L)
