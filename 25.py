#25. Realizar un algoritmo que pida un número y saque por pantalla su tabla de multiplicar.
numero=int(input("ingrese numero "))
for i in range(1,11,1):
    print(numero,"x",i,"=",numero*i)