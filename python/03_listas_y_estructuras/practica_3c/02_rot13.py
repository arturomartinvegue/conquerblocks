# Desarrollar un script con el método de encriptación rot 13.
alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


# Pedir la palabra al usuario que será encriptada.
user_word = input("Introduzca una palabra para encriptarla usando rot13: ")


# Realizar el cambio usando bucle para recorrer el alfabeto
word_encrypted = ""
for letter in user_word:
    for i in range(len(alfabeto)): 
        if alfabeto[i] == letter:
            word_encrypted += alfabeto[(i + 13) % len(alfabeto)]

        

print(f"""Palabra introducida: {user_word}
Palabra encriptada: {word_encrypted}""")


# Ampliación para comparar dos palabras y determinar si una es encriptación de la otra
print("Ahora se le pedirán dos palabras para determinar si una es encriptación de la otra.")
user_input_1 = input("Introduzca una palabra: ")
user_input_2 = input("Introduzca otra palabra: ")
word_encrypted_2 = ""
for j in range(len(user_input_2)):
    for i in range(len(alfabeto)):
        if alfabeto[i] == user_input_2[j]:
            word_encrypted_2 += alfabeto[(i + 13) % len(alfabeto)]

if word_encrypted_2 == user_input_1:
    print("Una es encriptación de la otra.")
else:
    print("No comparten encriptación.")
