def comprobacion_numero_primo():
    try:
        numero_p = int(input("Introduce un numero primo: "))
        numero_primo = True
        if numero_p <= 1:
            numero_primo = False
        else:
            for i in range(2, numero_p):
                if numero_p % i == 0:
                    numero_primo = False
                    break
        if numero_primo:
            print("ES PRIMO")

        else:
            print("NO PRIMO")
    except ValueError:
        print("Eso no es un numero")
