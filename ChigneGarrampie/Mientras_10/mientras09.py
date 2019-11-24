#el area de una casa y si se le considera una gran area o pequeña area
import os
a=int(os.sys.argv[1])
b=int(os.sys.argv[2])
area=a*b
print("el area de una casa es",area)
while area<80:
    print("area pequeña")
    a=int(input("ingrese primer dato:"))
    b=int(input("ingrese segundo dato:"))
    area=a*b
print("el area es:",area)
#fin_while


