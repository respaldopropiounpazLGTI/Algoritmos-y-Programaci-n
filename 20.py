#20. Hacer un algoritmo que permita ingresar tres números enteros y, si el primero de ellos es
# negativo, calcular el producto de los tres, en caso contrario calcular la suma de ellos.


numero1=int(input("ingrese primer valor "))
numero2=int(input("ingrese segundo valor "))
numero3=int(input("ingrese tercer valor "))
if numero1<0:
    promedio=(numero1+numero2+numero3)/3
    print("como el numero 1 es negativo se hace promedio da como resultado ",promedio)
else:
    suma=numero1+numero2+numero3
    print(" la suma es ",suma)