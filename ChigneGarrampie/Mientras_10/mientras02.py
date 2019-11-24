#suma de los n primeros numeros
import os
n=int(os.sys.argv[1])
i=0
suma=0
while(i<=n):
       suma += i
       i += 2
print("la suma de los",n,"numeros es:",suma)
#fin_while

