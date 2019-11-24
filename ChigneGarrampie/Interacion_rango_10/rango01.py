import os
#declaracion de datos
m,n=0,0
#imprimir el numero que se encuentran en ciertos intervalos
#imput
m=int(os.sys.argv[1])
n=int(os.sys.argv[2])

#ouput
print("Mostrar el interbalo que inici en",m,"Y termine en",n)
print("Despues sumar +5 a estos numeros")
print("Resultado:")

#iterador_rang
resultado= []

for suma in range(m,n):
    suma_mas_cinco=(suma + 5)
    resultado.append(suma_mas_cinco)
print(resultado)

#fin_iterador de rango
