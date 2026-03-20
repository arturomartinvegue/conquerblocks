# Validar acceso de los usuarios a un sitio web.


# Lista de listas con usuario y contraseña.
users_passwords = [["manolo75", "1234abc"], ["gaitaner", "surmano123"], ["amparo32", "spicygirls40"]]
broma = "¿Creías que iba a poner la contraseña?"


# Bucle con doble condición con ifs anidados.
user_found = False
pass_found = False
while user_found == False or pass_found == False:
    user_name = input("Introduzca el nombre de usuario: ")
    user_password = input("Introduzca la contraseña: ")

    for name_pass in users_passwords:
        if name_pass[0] == user_name:
            user_found = True
            if name_pass[1] == user_password:
                print(f"Acceso concedido {user_name} su contraseña es: {broma}")
                pass_found = True
            break
