#Ingresar P, T, R y calcular el interés simple.

P= float(input("ingrese el capital: "))
R= float(input("ingrese la taza de interes: "))
T= int(input("ingrese tiempo: "))
intsimple= P* (R/100)*T
print ("EL INTERES COMPUESTO ES: " + str (intsimple))

