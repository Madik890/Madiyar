a = "Hello, World!"
print(a[1])     #e

for x in "banana":
  print(x)   

a = "Hello, World!"
print(len(a))    #13

txt = "The best things in life are free!"
print("free" in txt)   #True

b = "Hello, World!"
print(b[2:5])   #llo

b = "Hello, World!"
print(b[-5:-2])   #orl

a = "Hello, World!"
print(a.upper())

a = " Hello, World! "
print(a.strip())   # returns "Hello, World!"

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello"
b = "World"
c = a + b
print(c)

'''f-string'''
age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)        #The price is 59.00 dollars

txt = "We are the so-called \"Vikings\" from the north."
print(txt)   #We are the so-called "Vikings" from the north.

