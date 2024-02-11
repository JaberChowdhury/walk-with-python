"""
global variables 
"""

x = "marvellous !!"
y = str("and I like it.")

def myfunc():
  z = "Don't be ridiculous"
  global a 
  a = "This variable is global but z isn't a global variable"
  print("Python is " + x + " " + y + z)

myfunc()

print(a)