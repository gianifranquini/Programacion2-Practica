import math
monto_invertir = float(input(" Ingrese el monto a invertir "))
interes_anual = float(input("Ingrese el interes anual "))
anios = int(input("Ingrese los años "))

for i in range(1,anios +1):
    capital= monto_invertir *((1+interes_anual/100) **i)
    print(f"año {i} : ${capital}")

