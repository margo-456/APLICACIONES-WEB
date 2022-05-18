# Ingresar dos ángulos de un triángulo y encontrar el tercer ángulo.

anguloA= int(input("ingrese el primer angulo: "))
anguloB= int(input("ingrese el segundo angulo: "))
total=180
suma=anguloA+anguloB
AnguloC=total-suma
print("EL RESULTADO DEL TERCER ANGULO ES: "+ str(AnguloC))
