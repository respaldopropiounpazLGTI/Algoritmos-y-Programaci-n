#17. Hacer un algoritmo que se ingresa dos precios(numero decimal) Mostrar los precios
# ordenado de mayor a menor
precio1=int(input("ingrese primer precio "))
precio2=int(input("ingrese segundo precio "))
if precio1>precio2:
    print(precio2,precio1)
else:
    print(precio1,precio2)