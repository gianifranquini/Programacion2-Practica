listaImpar = []
listaPar = []

for i in range(9):
    numero = int(input("ingrese:"))
    if numero % 2 == 0:
        listaPar.append(numero)
    else:
        listaImpar.append(numero)

print(f"Los numeros pares son:  {len(listaPar)} {listaPar}")
print("Los numeros impares son: ", len(listaImpar), listaImpar)