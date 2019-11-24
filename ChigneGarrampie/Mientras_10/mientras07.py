#la suma de dos numeros solo si son pares
import os
a=int(os.sys.argv[1])
b=int(os.sys.argv[2])
suma=(a+b)
while a%2!=0 or b%2!=0:
    print("no son pares")
    a=int(input("ingrese primer numero par:"))
    b=int(input("ingrese segundo numero par:"))
    suma=a+b
print("la suma es:",suma)
print("fin del bucle")
#fin_while
