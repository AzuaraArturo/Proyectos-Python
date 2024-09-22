import tkinter as tk
import messagebox


def mostrar_error():
    messagebox.showerror("Error", "Intenta con otra cantidad")


def valor_de_boton(item):
    clic = var_texto_de_entrada.get()
    var_texto_de_entrada.set(clic + str(item))


def limpiar_pantalla():
    var_texto_de_entrada.set("")


def resultado_operacion():
    try:
        resultado = str(eval(var_texto_de_entrada.get()))
        var_texto_de_entrada.set(resultado)
    except Exception:
        var_texto_de_entrada.set("Error")
        mostrar_error()


root = tk.Tk()
root.title("Calculadora")
root.geometry("250x400")
tamanio_fuente = ("Arial", 20)

var_texto_de_entrada = tk.StringVar()

entrada_frame = tk.Frame(root)
entrada_frame.pack()

entrada_de_datos = tk.Entry(entrada_frame, textvariable=var_texto_de_entrada, font=tamanio_fuente)
entrada_de_datos.grid(row=0, column=0)
entrada_de_datos.pack()

botones_frame = tk.Frame(root)
botones_frame.pack()

boton_num_nueve = tk.Button(botones_frame, text="9", padx=10, pady=10, font=tamanio_fuente,
                            command=lambda: valor_de_boton(9))
boton_num_ocho = tk.Button(botones_frame, text="8", padx=10, pady=10, font=tamanio_fuente,
                           command=lambda: valor_de_boton(8))
boton_num_siete = tk.Button(botones_frame, text="7", padx=10, pady=10, font=tamanio_fuente,
                            command=lambda: valor_de_boton(7))
boton_num_seis = tk.Button(botones_frame, text="6", padx=10, pady=10, font=tamanio_fuente,
                           command=lambda: valor_de_boton(6))
boton_num_cinco = tk.Button(botones_frame, text="5", padx=10, pady=10, font=tamanio_fuente,
                            command=lambda: valor_de_boton(5))
boton_num_cuatro = tk.Button(botones_frame, text="4", padx=10, pady=10, font=tamanio_fuente,
                             command=lambda: valor_de_boton(4))
boton_num_tres = tk.Button(botones_frame, text="3", padx=10, pady=10, font=tamanio_fuente,
                           command=lambda: valor_de_boton(3))
boton_num_dos = tk.Button(botones_frame, text="2", padx=10, pady=10, font=tamanio_fuente,
                          command=lambda: valor_de_boton(2))
boton_num_uno = tk.Button(botones_frame, text="1", padx=10, pady=10, font=tamanio_fuente,
                          command=lambda: valor_de_boton(1))
boton_num_cero = tk.Button(botones_frame, text="0", padx=10, pady=10, font=tamanio_fuente,
                           command=lambda: valor_de_boton(0))

boton_div = tk.Button(botones_frame, text="/", padx=10, pady=10, font=tamanio_fuente,
                      command=lambda: valor_de_boton("/"))
boton_mult = tk.Button(botones_frame, text="x", padx=10, pady=10, font=tamanio_fuente,
                       command=lambda: valor_de_boton("*"))
boton_rest = tk.Button(botones_frame, text="-", padx=10, pady=10, font=tamanio_fuente,
                       command=lambda: valor_de_boton("-"))
boton_sum = tk.Button(botones_frame, text="+", padx=10, pady=10, font=tamanio_fuente,
                      command=lambda: valor_de_boton("+"))
boton_resu = tk.Button(botones_frame, text="=", padx=10, pady=10, font=tamanio_fuente, command=resultado_operacion)
boton_borrar_pantalla = tk.Button(botones_frame, text="AC", padx=10, pady=10, font=15, command=limpiar_pantalla)

boton_num_nueve.grid(row=2, column=0)
boton_num_ocho.grid(row=2, column=1)
boton_num_siete.grid(row=2, column=2)
boton_num_seis.grid(row=3, column=0)
boton_num_cinco.grid(row=3, column=1)
boton_num_cuatro.grid(row=3, column=2)
boton_num_tres.grid(row=4, column=0)
boton_num_dos.grid(row=4, column=1)
boton_num_uno.grid(row=4, column=2)
boton_num_cero.grid(row=5, column=1)

boton_borrar_pantalla.grid(row=1, column=0)
boton_div.grid(row=1, column=3)
boton_mult.grid(row=2, column=3)
boton_rest.grid(row=3, column=3)
boton_sum.grid(row=4, column=3)
boton_resu.grid(row=5, column=3)

root.mainloop()
