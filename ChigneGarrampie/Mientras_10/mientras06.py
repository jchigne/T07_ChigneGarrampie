#crear una una cuenta de credito
import os
limete=False
nombre=os.sys.argv[1]
dni=int(os.sys.argv[2])
edad=int(os.sys.argv[3])
limete=(edad>18)
while edad<18:
    print("edad no permitida")
    nombre=input("ingrese el nombre:")
    dni=int(input("ingrese el numero de dni:"))
    edad=int(input("ingrese la edad:"))
    limete=(edad>18)
print("edad permitida")
print("cuenta creada")

#fin_while
