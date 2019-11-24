#hallar la raiz cuadrada de un numero
import os
x=int(os.sys.argv[1])
while x<0:
    print("no se puede obtener una raiz cuadrada de un un numero negativo")
    x=int(input("ingrese de nuevo el numero"))
rais_cuadrada=x**(1/2)
print("la raiz cuadrada es",rais_cuadrada)
#fin_bucle
