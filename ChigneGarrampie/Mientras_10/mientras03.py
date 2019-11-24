#muestra el promedio de un estudiante y ademas sale si da aprobado o reprobado
import os
a=int(os.sys.argv[1])
b=int(os.sys.argv[2])
c=int(os.sys.argv[3])
prom=(a+b+c)/3
print("el promedio es:",prom)
while prom<11.4:
    print("el alumno sale con resultado:DESAPROBADO")
    a=int(input("ingrese primer dato:"))
    b=int(input("ingrese segundo dato:"))
    c=int(input("ingrese tercer dato:"))
    prom=(a+b+c)/3
print("El el prmedio final es:",prom)
print("APROBADO")
#fin_while
