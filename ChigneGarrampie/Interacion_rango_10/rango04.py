#lista de multiplos de a  hasta el b inclusive
import os
a=int(os.sys.argv[1])
b=int(os.sys.argv[2])
print("el listado de los multiplos desde;",a,"hasta:",b)
for multiplo_de_tres in range(a,b,3):
    print(multiplo_de_tres)
print("el listado crese de 3 en 3 en a y b")

#fin_iterador de rango
