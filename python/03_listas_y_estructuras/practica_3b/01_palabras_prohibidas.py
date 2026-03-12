# Script que filtra las palabras en función de letras prohibidas en listas


# Definir lista con las palabras aleatorias.
words_list = ["aleatorio", "palabra", "contraseña", "supercalifragilísticoespialidoso", "numeros"]
letters_banned = ["z", "p", "ñ"]


# Recorrer la lista de palabras y hacer la comparación con las letras que las filtran
# Declarar variable antes del bucle dónde se almacenan las palabras permitidas
words_allowed = []

for word in words_list:
    prohibida = False  # Puerta de entrada que determina si la palabra se añade o no
    for letter in letters_banned:
        if letter in word:
            prohibida = True
    if not prohibida:
        words_allowed.append(word)

print(f"""Las palabras permitidas
      de la lista: {words_list}
      son: {words_allowed}""")

