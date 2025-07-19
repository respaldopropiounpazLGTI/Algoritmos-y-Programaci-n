#47.  Desarrollar un algoritmo que lea una lista de 10 números y determine cuantos son 
# positivos, y cuantos son negativos.
mi_lista=[]
positivos=0
negativos=0
ceros=0
for i in range(10):
    carga=int(input(f"ingrese numero {i+1} :"))
    if carga>0:
        positivos+=1
    elif carga==0:
        ceros+=1
        continue
    else:
        negativos+=1
print(f"cantidad de numeros positivos: {positivos}")
print(f"cantidad de numeros negativos: {negativos}")
print(f"cantidad de 0 :{ceros}")


