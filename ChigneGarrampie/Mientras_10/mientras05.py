#hallar la fuerza
import os
m=int(os.sys.argv[1])
a=int(os.sys.argv[2])
f=m*a
print("la fuerza es",f)
while f<100:
    print("fuerza no es la minima para romper una tabla")
    m =int(input("ingrese primer dato:"))
    a = int(input("ingrese segundo dato:"))
    f=m*a
print("La fuerza usada es la ideal")
#fin_while
