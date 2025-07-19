#10. Hacer un algoritmo que ingrese dos números y determinar si alguno de los dos números
# es divisible por 3.
numero1=int(input("ingrese primer valor "))
numero2=int(input("ingrese segundo valor "))
if numero1%3==0 and numero2%3==0:
    print(numero1,numero2," ambos numero son divisibles por 3 ")
elif numero1%3==0:
    print(" el numero 1 valor ",numero1,"es divisible por 3")
elif numero2%3==0:
    print("el numero 2 valor ",numero2,"es divisible por 3 ")
else:
    print("ninguno de los 2 numeros es divisible ")