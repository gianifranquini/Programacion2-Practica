import random
num_aleatorio = random.randint(1, 20)
intentos=0
numero_ingresado=0

while(numero_ingresado!=num_aleatorio):
    numero_ingresado = int(input("Ingrese un numero"))

    if(numero_ingresado<num_aleatorio):
        print("El numero es mayor")
    if(numero_ingresado>num_aleatorio):
        print("el numero es menor")
    intentos+=1

print(f"Adivinaste en {intentos} intentos")