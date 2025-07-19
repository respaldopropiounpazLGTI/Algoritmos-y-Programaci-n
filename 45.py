"""45. Diseñar un algoritmo que permita ingresar por pantalla 70 números naturales. Calcular el
promedio de los números pares. Luego mostrar por pantalla el resultado"""
sumando=0

for i in range(10):
    numero=int(input(f"ingrese numero {i+1} "))
    sumando+=numero
    promedio=sumando/10
print(f" la suma es {sumando}y el ppromedio es {promedio} ")    