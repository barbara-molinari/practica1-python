import random
categorias = {
    "programacion": ["variable", "bucle", "funcion", "algoritmo", "codigo"],
    "python": ["listas", "diccionario", "tupla", "indentacion", "import"]
}

print("¡Bienvenido al Ahorcado!")
print()
print("Categorías disponibles: programacion, python")
seleccion = input("Elegí una categoría: ").lower()

# Buscamos la palabra dentro de la lista 
word = random.choice(categorias[seleccion])
guessed = []
attempts = 6
letras_incorrectas = 0



while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)
    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        puntaje = 6 - letras_incorrectas
        print(f"¡Ganaste! Tu puntaje es {puntaje}")
        break

    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    letter = input("Ingresá una letra: ")
    
    if len(letter) != 1 or not letter.isalpha():
        print("Entrada no válida")
        continue

    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        letras_incorrectas += 1
        print("Esa letra no está en la palabra.")

    print()
else:
    print(f"¡Perdiste! La palabra era: {word}. Tu puntaje es: 0")