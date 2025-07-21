"""51. Desarrollar un programa que permita ingresar números reales mayores que 0 (cero),
finalizar el ingreso cuando no se cumpla esta condición e informar el valor menor y el
valor mayor del conjunto."""
mayor=0
menor=float(0)
while True:
    numero=float(input(" ingrese numero "))
    if numero<=0:
        break
    if numero<menor:
        menor=numero
    if numero>mayor:
        mayor=numero    
print(f"el numero de mayor valor es {mayor}")  
print(f"el numero de menor valor es {menor}")  
