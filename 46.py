#45. Diseñar un algoritmo que permita ingresar por pantalla 70 números naturales. Calcular el
# promedio de los números pares. Luego mostrar por pantalla el resultado

pares=0
for i in range(70):
    numero=int(input(f"ingrese numero {i+1} "))
    if numero%2==0:
        pares+=numero
promedio=pares/70       

print(f" la suma de sumeros pares es : {pares} y el promedio es : {promedio }")        