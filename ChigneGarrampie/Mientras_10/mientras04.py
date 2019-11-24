#mostrar la divison entre dos numeros
import os
l=int(os.sys.argv[1])
k=int(os.sys.argv[2])
division=0
while k==0:
    print("no es posible dividir entre cero")
    k=int(input("ingrese numero divisor:"))
division=(l/k)
print("la division es:",division)

#fin_while
