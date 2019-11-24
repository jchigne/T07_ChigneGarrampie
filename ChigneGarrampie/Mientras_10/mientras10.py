#Que pida un número y diga si es par o impar .
import os
a=int(os.sys.argv[1])
print("el numero ingresado es:",a)
while a%2!=0:
    print("este numero ingresado es impar.")
    a=int(input("ingrese el numero nuevamente:"))
else:
    print("el numero es par")
#fin_while
