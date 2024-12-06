print("""
       **************************************
       *       'CIFRADO DE MENSAJES'        * 
       *         'FES Aragón UNAM'          *
       *      'Ingeniería en Computación'   *
       *     Azuara Ocotitla Arturo Ivan    *
       *    Monroy Quintero Eliezer Isaí    *
       *   Padron Cortes Monica Alessandra  *
       *       Villela Andrade Aksel        *
       **************************************
    """)


def comp_1er_num_primo(numero_p):
    numero_primo = True
    if numero_p <= 1:
        numero_primo = False
    else:
        for i in range(2, numero_p):
            if numero_p % i == 0:
                numero_primo = False
                break
    if not numero_primo:
        print("El 1er número no es primo, intentalo de nuevo.")
    return numero_primo


def comp_2nd_num_primo(numero_q):
    numero_primo = True
    if numero_q <= 1:
        numero_primo = False
    else:
        for i in range(2, numero_q):
            if numero_q % i == 0:
                numero_primo = False
                break
    if not numero_primo:
        print("El 2nd número no es primo, intentalo de nuevo.")
    return numero_primo


def num_iguales(numero_p, numero_q):
    if numero_q == numero_p:
        print("Los numeros no pueden ser los mismos, intenta nuevamente.")
        return True
    else:
        return False


def mcd(producto_de_phi, num):
    while num != 0:
        producto_de_phi, num = num, producto_de_phi % num
    return producto_de_phi


def son_coprimos(producto_de_phi, num):
    return mcd(producto_de_phi, num) == 1


def inverso_modular(mcd, producto_phi):
    resto_actual, resto_anterior = producto_phi, mcd
    coef_actual, coef_anterior = 0, 1
    while resto_anterior != 0:
        cociente = resto_actual // resto_anterior
        resto_actual, resto_anterior = resto_anterior, resto_actual - cociente * resto_anterior
        coef_actual, coef_anterior = coef_anterior, coef_actual - cociente * coef_anterior
    if resto_actual != 1:
        return None
    else:
        return coef_actual % producto_phi

def encriptar(mensaje, clave_publica):
    return [(ord(char) ** clave_publica[0]) % clave_publica[1] for char in mensaje]


def desencriptar(mensaje_encriptado, clave_privada):
    return ''.join([chr((char ** clave_privada[0]) % clave_privada[1]) for char in mensaje_encriptado])



while True:
    try:
        numero_p = int(input("Introduce 1er numero primo: "))
        while not comp_1er_num_primo(numero_p):
            numero_p = int(input("Introduce 1er numero primo: "))

        numero_q = int(input("Introduce 2nd numero primo: "))
        while not comp_2nd_num_primo(numero_q) or num_iguales(numero_p, numero_q):
            numero_q = int(input("Introduce 2nd numero primo: "))
        print("")
        print(f"Los numeros introducidos han sido, {numero_p} y {numero_q}.")
        print("")

        producto_n = numero_p * numero_q
        print("")
        print(f"El resultado del producto de 'n' es: {producto_n}")
        print("")
        producto_de_phi = (numero_p - 1) * (numero_q - 1)
        print("")
        print(f"El resultado del producto de 'phi' es: {producto_de_phi}")
        print("")

        while True:
            calculo_mcd = int(input("Introduce un numero coprimo con phi: "))
            if not son_coprimos(producto_de_phi, calculo_mcd):
                print(f"{calculo_mcd} no es coprimo con {producto_de_phi}.")
            else:
                print(f"{calculo_mcd} es coprimo con {producto_de_phi}.")
                print(f"MCD ({producto_de_phi}, {calculo_mcd})")
                inverso = inverso_modular(calculo_mcd, producto_de_phi)
                print("")
                print(f"El inverso modular de: ({calculo_mcd} y {producto_de_phi}) es = ", inverso)
                print("")
                break

        clave_publica = (calculo_mcd, producto_n)
        clave_privada = (inverso, producto_n)
        print("")
        print(f"Tu clave pública es: ({calculo_mcd},{producto_n})")
        print(f"Tu clave privada es: ({inverso},{producto_n})")
        print("")

        while True:
            mensaje = input("Introduce el mensaje a encriptar: ")
            mensaje_encriptado = encriptar(mensaje, clave_publica)
            print(f"Mensaje encriptado: {mensaje_encriptado}")
            mensaje_desencriptado = None
            desencriptado_exitoso = False
            while not desencriptado_exitoso:
                clave = input("Introduce la clave privada para desencriptar (separando los números por coma): ")
                clave_ingresada = tuple(map(int, clave.split(',')))
                if clave_ingresada == clave_privada:
                    mensaje_desencriptado = desencriptar(mensaje_encriptado, clave_privada)
                    print(f"Mensaje desencriptado: {mensaje_desencriptado}")
                    desencriptado_exitoso = True
                else:
                    print("Clave incorrecta, inténtalo nuevamente")
            break
    except ValueError:
        print("Error, intenta de nuevo")
    break

