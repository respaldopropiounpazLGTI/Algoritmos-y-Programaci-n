#44. Realizar un algoritmo para calcular el cuadrado de un número. El número debe ser mayor
# que cero. Si es menor que cero mostrar por pantalla el mensaje "ERROR, el Número
# debe ser mayor que cero". Si no mostrar el resultado de dicho calculo. El programa
# finaliza cuando se ingresa cero
numero=int(input("ingrese numero "))
cuadrado=numero*numero
if numero<0:
    print(" el numero debe ser mayor a 0 ")
else: 
    print(f" el numero { numero} al cuadrado es {cuadrado} ")

