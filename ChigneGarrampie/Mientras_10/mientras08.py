#muestra si se puede recaudar el suficiente monto para ir de paseo
import os
niño1=int(os.sys.argv[1])
niño2=int(os.sys.argv[2])
niño3=int(os.sys.argv[3])
monto=niño1+niño2+niño3
print("el monto es:",monto)
while monto<100:
    print("monto muy bajo")
    print("no podran ir de paseo")
    niño1=int(input("ingrese el primer monto:"))
    niño2=int(input("ingrese el segundo monto:"))
    niño3=int(input("ingrese el tercer monto:"))
    monto=niño1+niño2+niño3
print("El monto es el nesesario")
print("Viajaremos")

#fin_while
