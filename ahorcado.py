from random import *

palabra = ["casa" , "carro" , "moto" , "mico"]
aleatorio= choice(palabra).upper()
opcion_correcta= set(aleatorio)
intentos =[]
vidas = 6

mensaje = ("Hola,Tienes 6 oportunidades para ganar en este juego")
print(mensaje)
letra = str(input("Ingresa la letra que creas que te pueda servir:   ")).upper()

while vidas >0:
    intentos.append(letra)

    if letra in opcion_correcta:
        opcion_correcta.remove(letra)
        if opcion_correcta == set():
            print(f"es correcto,Haz acertado en todas las letras GANASTE con la palabra {aleatorio}:)")
            break
        print(f"la letra {letra} si esta en la palabra que debes adivinar, te quedan {vidas} vidas :) ")
        letra = str(input("Ingresa la letra que creas que te pueda servir:   ")).upper()


    elif letra not in opcion_correcta:
        vidas= vidas -1
        print(f"Lo siento, la letra {letra} NO esta en la palabra que debes adivinar, te quedan {vidas} vidas :) ")
        letra = str(input("Ingresa la letra que creas que te pueda servir:   ")).upper()
        
        if vidas == 0:
            print(f"PERDISTE ! La palabra ganadora de hoy era {aleatorio}")
            
print("El juego ha terminado, Buena jugada.  :)   ¡Intentalo de nuevo!")