#18. Hacer un algoritmo que se ingresa el tiempo registrado de dos autos que corrieron una
# carrera. El tiempo se guardó como número decimal. Mostrar por pantalla cual llego
# primero
auto1=float(input(" ingrese primer valor "))
auto2=float(input("ingrese segundo valor "))
if auto1<auto2:
    print(" auto 1 llego primero con el tiempo de ",auto1)
else:
    print("auto 2 llego primero con un tiepo de ",auto2)