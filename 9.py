#Ejercio 9

print("Ingresa los siguientes datos")
print("                             ")

cantidad = float(input("Cantidad a Invertir: "))
interes = float(input("Interés Anual: "))
años = int(input("Número de Años: "))

print("Capital Obtenido: " + str(round(cantidad * (interes / 100 + 1) ** años, 2)))