#Ejercicio 10

print("Ingresa los siguientes datos del último pedido vendido")
print("                             ")

Ppayaso = 112
Pmuñeca = 75

payasos = int(input("Número de payasos vendidos: "))
muñecas = int(input("Número de muñecas vendidas: "))

peso_total = Ppayaso * payasos + Pmuñeca * muñecas

print("Peso total del paquete: " + str(peso_total) + " g ")