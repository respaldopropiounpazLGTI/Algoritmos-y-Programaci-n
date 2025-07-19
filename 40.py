# 40. Hacer un algoritmo que permita convertir calificaciones numéricas a letras, según la
# siguiente tabla:
# A=19 y 20, B=16, 17 y 18, C=13, 14 y 15, D=10, 11 y 12, E=1 hasta el 9. Se asume
# que la nota está comprendida entre 1 y 20.
while True:
    nota=int(input("ingrese nota"))
    if nota >=1 and nota<=9:
     print("E")
    elif nota >=10 and nota<=12:
     print("D")
    elif nota>=13 and nota<=15:
     print("C")
    elif nota>=16 and nota<=18:
     print("B")
    elif nota>=19 and nota<=20:
     print("A")
    else:
     print(" solo balores del 1 al 20")

