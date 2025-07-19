#19. Hacer un algoritmo que se ingresa tres número. Mostrar por pantalla si están ordenados
# de menor a mayor
numero1=int(input("ingrese primero numero "))
numero2=int(input("ingrese segundo numero "))
numero3=int(input("ingrese tercer valor "))
if numero1<numero2 and numero1<numero3:
    print("los numeros",numero1,numero2,numero3,"estan ordenados ")
elif numero2<numero3:
    print(numero2,numero1,numero3,"estan ordenados ")
else:
    print("los nuumeros",numero3,numero2,numero1,"estan ordenados ")

