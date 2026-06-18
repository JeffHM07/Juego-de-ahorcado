#Tarea Juego de ahorcado
#Descripción:
#El programa selecciona una palabra aleatoria.
#El usuario debe adivinar la palabra letra por letra.

import random
import os

#Vector con las posibles palabras del juego
palabras = ["python","computadora", "programa", "almendra", "ahorcado", "amarillo", "cometa"]

#Se selecciona una palabra aleatoria del vector
palabra = random.choice(palabras)

#Lista donde se guardan las letras que el usuario ya ingresó
letras = []

#Variable para mostrar la palabra
mostrar = ""

#El ciclo continúa mientras la palabra no haya sido adivinada
while mostrar != palabra:
    os.system("cls")

#Reinicia la palabra mostrada
    mostrar = ""

#Construye la palabra visible
    for letra in palabra:
        if letra in letras:
            mostrar += letra
        else:
            mostrar += "_ "
    print("JUEGO DE AHORCADO")
    print("Palabra:", mostrar)

#Solicita una letra si aún no ha ganado
    if mostrar != palabra:
        usuario = input("Digite una letra: ")
        letras.append(usuario)

#Imprime la condición de victoria
print("Ganaste!")
print("La palabra era:", palabra)