#2.	Escribir un programa que almacene la cadena ¡Hola Mundo!  en una variable y luego muestre por pantalla el contenido de la variable al revés.
texto = "¡Hola Mundo!"
texto_invertido = "".join(reversed(texto))
print(texto_invertido)