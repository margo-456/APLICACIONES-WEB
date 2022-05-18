#Ingresar cualquier número y calcular su raíz cuadrada.

from math import sqrt
numero= int(input("INGRESE UN NUMERO: "))
if numero >=0:
 raizcuad=sqrt(numero)
 print ("la raiz cuadrada del número  es: " + str (raizcuad))
else:
 print ("número negativo no tiene raíz cuadrada " )