#Decodificador mensajes encriptado
import os

#declaracion de datos
MSG=""

#imput
MSG=os.sys.argv[1].upper()

#el mensaje es
print("El mensaje encriptado es:")
#bucle
for letra in MSG:
    if letra == "A":
        print("hola")
    if letra == "B":
        print("Como")
    if letra == "C":
        print("Estas")

#fin_interacion
print("Fin del bucle")
