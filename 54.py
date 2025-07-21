"""54. Como resultado de una encuesta se recogen los siguientes datos: sexo, edad y altura. 
Se pide realizar un programa que informe 
el porcentaje de mujeres mayores de 25 años,
la cantidad de varones menores de 18 años 
el porcentaje de individuos mayores de 18 años cuya altura supera los 170 cm. 
Ingresar únicamente 40 encuestas."""
mujer_mayores_a_25=0
varones_menores_a_18=0
individuos_mayores_a_18_y_170_altura=0
for  i in range(40):
    sexo=input("ingrese sexo : ").lower()
    edad=int(input("ingrese edad :"))
    altura=float(input(" ingrese altura : "))
    if sexo=="mujer"or sexo=="m":
        if edad>25:
            mujer_mayores_a_25+=1
    if sexo=="varon"or sexo=="v":
        if edad<18:
            varones_menores_a_18+=1
    if edad>18 and altura>170:
        individuos_mayores_a_18_y_170_altura+=1  
print(f"mujeres mayores de 18 años {mujer_mayores_a_25}")        
print(f"varores manores de 18 años {varones_menores_a_18}")
print(f"total de individuos mayores de 18 años y que superen los 170 de altura {individuos_mayores_a_18_y_170_altura}")
porcentaje=(individuos_mayores_a_18_y_170_altura/40)*100
print(f" individuos mayores de 18 años cuya altura supera los 170 cm {porcentaje}   ")


