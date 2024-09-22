usuario = []
contrasenia = []
def login(user, password):

    for i in range(len(usuario)):
        if user == usuario[i]:
            print(f"El usuario: '{user}' es correcto")
            break
        else:
            print(f"El usuario: '{input_user}' NO es correcta")
    for j in range(len(contrasenia)):
        if password == contrasenia[j]:
            print(f"La clave: '{password}' es correcta")
            break
        else:
            print(f"La clave: '{password}' NO es correcta")


input_user = input("Ingresa usuario: ")
usuario.append(input_user)
input_password = input("Ingresa Password: ")
contrasenia.append(input_password)

confirmar_user = input("Confirma tu usuario: ")
confirmar_password = input("Confirma tu password: ")

login(confirmar_user, confirmar_password)
