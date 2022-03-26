from itertools import product
import rarfile
import s_lib

rar_file = input("Enter the file name: ")
location = input("Enter the destination path: ")

#Instructions
print()
print("*" * 12,
      "PRESS d(lowercase) IF YOU CAN'T REMEMBER OR DON'T KNOW WHAT TO ANSWER",
      "*" * 12)
print()

#Password length, default is 1
length = input("Do you atleast remember the length of your password? [y/n]: ")
if length == "y":
    r = int(input("Enter the length(integer/number form): "))
else:
    r = 1

#Character constraints
#Python string library can also be used
spaces = input("Does your password contains SPACES? [y/n]: ")
symbols = input("Does your password contains SYMBOLS? [y/n]: ")
numbers = input("Does your password contains NUMBERS? [y/n]: ")
letters = input(
    "Does your password contains LETTERS? [upper, lower, both, none]: ")
constraints = ""

if spaces == "y" or spaces == "d":
    constraints += s_lib.space()

if symbols == "y" or symbols == "d":
    constraints += s_lib.symbols()

if numbers == "y" or numbers == "d":
    constraints += s_lib.numbers()

if letters == "upper":
    constraints += s_lib.upper()

elif letters == "lower":
    constraints += s_lib.lower()

elif letters == "both" or letters == "d":
    constraints += s_lib.up_low()

for password in product(constraints, repeat=r):
  #Need to join because product returns list
  pw = "".join(password)
  try:
    with rarfile.RarFile(rar_file) as rf:
      rf.extractall(location, pwd=pw)
      print(f"Successfully extracted at {location}")
      break
      
  except:
    print(f"not: {pw}")
    
      
  

