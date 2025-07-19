#49.  Desarrollar un algoritmo que permita ingresar 10 números naturales, luego informar por 
# pantalla: 
# a) La sumatoria de los valores múltiplos de 3. 
# b) La cantidad de valores múltiplos de 5. 
# c) La sumatoria de los valores que se ingresan y son pa
sumatoriadetres=0
cantidadmultiplodecinco=0
sumatoria_total=0
numeros_par=0
for i in range(10):
    numero=int(input(f"ingrese numeros {i+1}:"))
    sumatoria_total+=numero
    if numero%2==0:
        numeros_par+=numero
    if numero%3==0:
        sumatoriadetres+=numero
    if numero%5==0:
        cantidadmultiplodecinco+=1

print(f"sumatoria total {sumatoria_total}")
print(f"sumatoria numeros par {numeros_par}")
print(f"sumatoria numeros multiplos de tres {sumatoriadetres}")
print(f"sumatoria numeros multplis de cinco {cantidadmultiplodecinco}")        

  