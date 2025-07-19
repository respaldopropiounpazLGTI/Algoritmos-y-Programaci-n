#26. Hacer un algoritmo que se ingresan 100 números enteros, mostrar por pantalla la
# cantidad de números pares que se ingresaron.
par=0
inpar=0
for i in range(3):
    numero=int(input("ingrese numero "))
    if numero%2==0:
        par+=1
    else:
        inpar+=1

print("cantidad numero pares ",par)
print("cantidad numero inpares ",inpar)        