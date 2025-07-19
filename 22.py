#22. Realizar un algoritmo que permita leer dos números, determinar cuál de los dos números
# es el menor y mostrarlo por pantalla con el mensaje “El numero N es menor al numero
# X”
numero1=int(input("ingrese primero numero "))
numero2=int(input("ingrese segundo numero "))
if numero1<numero2:
    print(" el numero ",numero1,"es el menor ")
else:
    print("el numero ",numero2,"es el menor ")