#Ejercicio 7

print("Ingresa los siguientes datos")
print("                             ")

peso = input("Peso en kg: ")
estatura = input("Estatura en metros: ")
indice = round(float(peso)/float(estatura)**2,2)

print("                             ")
print("Tu índice de masa corporal es " + str(indice))