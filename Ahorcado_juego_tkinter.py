import tkinter as tk
from random import choice
from palabras_juego import modo_argento, normal_niveles

modo_actual = None
nivel_actual = None
palabra_actual = None


def centrar_ventana(ventana, ancho, alto):
    ventana.update_idletasks() 
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()

    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)

    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

def mostrar_frame(frame):
    frame_inicio.place_forget()
    frame_modos.place_forget()
    frame_niveles.place_forget()
    frame_juego.place_forget()
    frame.place(relwidth=1, relheight=1)

ventana=tk.Tk()
ventana.title('Juego del AHORCADO')
ventana.config(bg="tomato")

centrar_ventana(ventana, 600, 450)
ventana.resizable(False, False)

frame_inicio = tk.Frame(ventana, bg="tomato")
frame_inicio.place(relwidth=1, relheight=1)

def ir_a_modos():
    mostrar_frame(frame_modos)

btn_jugar = tk.Button(
    frame_inicio,
    text="JUGAR",
    font=("Arial", 25, "bold"),
    width=12,
    height=2,
    bg="#2ecc71",
    fg="white",
    activebackground="#27ae60",
    activeforeground="white",
    command=ir_a_modos,
    cursor="hand2"
)
btn_jugar.place(relx=0.5, rely=0.5, anchor="center")

frame_modos = tk.Frame(ventana, bg="tomato")

menu_centrado = tk.Frame(frame_modos, bg="tomato")
menu_centrado.place(relx=0.5, rely=0.4, anchor="center")


lbl = tk.Label(
    menu_centrado,
    text="Elegí el modo de juego",
    font=("Arial", 18, "bold"),
    bg="tomato",
    fg="white"
)
lbl.pack(pady=20)

estilo_boton = {
    "font": ("Arial", 15, "bold"),
    "width": 20,
    "bg": "#f39c12",
    "fg": "white",
    "activebackground": "#e67e22",
    "activeforeground": "white",
    "cursor": "hand2"
}

btn_normal = tk.Button(menu_centrado, text="Modo Normal", **estilo_boton)
btn_normal.pack(pady=10)

btn_argento = tk.Button(menu_centrado, text="Modo Argento 🇦🇷", **estilo_boton)
btn_argento.pack(pady=10)

frame_niveles = tk.Frame(ventana, bg="tomato")

def ir_a_modo_normal():
    global modo_actual
    modo_actual = "normal"
    mostrar_frame(frame_niveles)


btn_normal.config(command=ir_a_modo_normal)

menu_niveles = tk.Frame(frame_niveles, bg="tomato")
menu_niveles.place(relx=0.5, rely=0.4, anchor="center")

lbl_niveles = tk.Label(
    menu_niveles,
    text="Elegí el nivel",
    font=("Arial", 18, "bold"),
    bg="tomato",
    fg="white"
)
lbl_niveles.pack(pady=20)

estilo_nivel = {
    "font": ("Arial", 15, "bold"),
    "width": 20,
    "bg": "#3498db",
    "fg": "white",
    "activebackground": "#2980b9",
    "activeforeground": "white",
    "cursor": "hand2"
}

btn_facil = tk.Button(menu_niveles, text="Fácil", **estilo_nivel)
btn_facil.pack(pady=10)

btn_intermedio = tk.Button(menu_niveles, text="Intermedio", **estilo_nivel)
btn_intermedio.pack(pady=10)

btn_dificil = tk.Button(menu_niveles, text="Difícil", **estilo_nivel)
btn_dificil.pack(pady=10)

btn_volver = tk.Button(
    frame_niveles,
    text="⬅ Volver",
    font=("Arial", 11),
    bg="#bdc3c7",
    command=ir_a_modos,
    cursor="hand2"
)
btn_volver.place(x=20, y=20)

frame_juego = tk.Frame(ventana, bg="tomato")

def ir_a_modo_argento():
    global modo_actual, palabra_actual

    modo_actual = "argento"
    palabra_actual = choice(list(modo_argento.keys()))

    print("Modo:", modo_actual)
    print("Palabra elegida:", palabra_actual)

    mostrar_frame(frame_juego)

btn_argento.config(command=ir_a_modo_argento)

btn_volver = tk.Button(
    frame_juego,
    text="⬅ Volver",
    font=("Arial", 11),
    bg="#bdc3c7",
    command=ir_a_modos,
    cursor="hand2"
)
btn_volver.place(x=20, y=20)


mostrar_frame(frame_inicio)
ventana.mainloop()