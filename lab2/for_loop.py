fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) # apple


for x in range(2, 6):
  print(x)     #from 2 to 5


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)    
    '''red apple
       red banana
       red cherry
       big apple
       big banana
       big cherry
       tasty apple
       tasty banana
       tasty cherry'''