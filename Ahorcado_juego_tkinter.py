import tkinter as tk

from random import choice

import logica_juego as lj

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

def ir_a_modos():
    mostrar_frame(frame_modos)

def ir_a_modo_normal():
    global modo_actual
    modo_actual = "normal"
    mostrar_frame(frame_niveles)   

def ir_a_modo_argento():
    global modo_actual, palabra_actual

    modo_actual = "argento"
    palabra_actual = choice(list(modo_argento.keys()))

    print("Modo:", modo_actual)
    print("Palabra elegida:", palabra_actual)

    mostrar_frame(frame_juego)
    lbl_info_actual.config(text=f'🔥 MODO {modo_actual.upper()} 🔥\n'\
                           'Palabras de la calle, del interior y bien de acá.')
    mostrar_palabra_oculta()
    ventana.bind("<Key>", tecla_presionada)


def iniciar_juego_normal(nivel):
    global nivel_actual, palabra_actual

    palabra_actual = choice(normal_niveles[nivel])

    if nivel=='facil':
        nivel_actual='fácil'
    elif nivel=='dificil':
        nivel_actual='difícil'
    else:
        nivel_actual=nivel

    print("Modo:", modo_actual)
    print("Nivel:", nivel_actual)
    print("Palabra:", palabra_actual)
    
    mostrar_frame(frame_juego)
    lbl_info_actual.config(text=f'Modo {modo_actual.capitalize()}\nNivel {nivel_actual.capitalize()}')
    resetear_partida()
    mostrar_palabra_oculta()
    ventana.bind("<Key>", tecla_presionada)

def mostrar_palabra_oculta():
    oculta = " ".join("_" for _ in palabra_actual)
    lbl_palabra.config(text=oculta)

def tecla_presionada(event):
    global vidas

    letra = event.char.lower()

    # Ignorar teclas que no sean letras
    if not letra.isalpha() or len(letra) != 1:
        return

    # Ignorar letras ya usadas
    if letra in letras_adivinadas:
        return

    letras_adivinadas.add(letra)

    if letra in palabra_actual:
        actualizar_palabra()
    else:
        vidas -= 1
        actualizar_vidas()

def actualizar_palabra():
    resultado = ""

    for letra in palabra_actual:
        if letra in letras_adivinadas:
            resultado += letra.upper() + " "
        else:
            resultado += "_ "

    lbl_palabra.config(text=resultado.strip())

def actualizar_vidas():
    corazones = "❤ " * vidas
    cruces= "❌ " * (7-vidas)
    lbl_vidas.config(text=f"Vidas: {cruces}{corazones}")

    if vidas <= 0:
        lbl_palabra.config(text=f"Perdiste 😢\nLa palabra era: {palabra_actual.upper()}")
        ventana.unbind("<Key>")

def resetear_partida():
    global vidas, letras_adivinadas
    vidas = 7
    letras_adivinadas.clear()
    actualizar_vidas()

ventana=tk.Tk()
ventana.title('Juego del AHORCADO')
ventana.config(bg="tomato")

centrar_ventana(ventana, 600, 450)
ventana.resizable(False, False)

frame_inicio = tk.Frame(ventana, bg="tomato")

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

btn_normal = tk.Button(menu_centrado, text="Modo Normal",command=ir_a_modo_normal, **estilo_boton)
btn_normal.pack(pady=10)

btn_argento = tk.Button(menu_centrado, text="Modo Argento 🇦🇷",command=ir_a_modo_argento, **estilo_boton)
btn_argento.pack(pady=10)

frame_niveles = tk.Frame(ventana, bg="tomato")

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

btn_facil = tk.Button(
    menu_niveles, 
    text="Fácil", 
    command=lambda: iniciar_juego_normal("facil"), 
    **estilo_nivel)
btn_facil.pack(pady=10)

btn_intermedio = tk.Button(
    menu_niveles, 
    text="Intermedio", 
    command=lambda: iniciar_juego_normal("intermedio"), 
    **estilo_nivel)
btn_intermedio.pack(pady=10)

btn_dificil = tk.Button(
    menu_niveles, 
    text="Difícil",
    command=lambda: iniciar_juego_normal("dificil"), 
    **estilo_nivel)
btn_dificil.pack(pady=10)

btn_volver = tk.Button(
    frame_niveles,
    text="⬅ Volver",
    font=("Arial", 11),
    bg="#bdc3c7",
    command=ir_a_modos,
    cursor="hand2"
)
btn_volver.place(x=10, y=10)

frame_juego = tk.Frame(ventana, bg="tomato")

# --- Sub-frames del juego ---
frame_volver_vidas=tk.Frame(frame_juego,bg="tomato")
frame_volver_vidas.pack(fill="x",pady=10)

frame_actual=tk.Frame(frame_juego, bg="tomato")
frame_actual.pack(pady=8)

frame_palabra = tk.Frame(frame_juego, bg="tomato")
frame_palabra.pack(pady=50)

btn_volver = tk.Button(
    frame_volver_vidas,
    text="⬅ Volver",
    font=("Arial", 11),
    bg="#bdc3c7",
    command=ir_a_modos,
    cursor="hand2"
)
btn_volver.pack(anchor="w", padx=10)

letras_adivinadas = set()
vidas = 7

lbl_vidas = tk.Label(
    frame_volver_vidas,
    text=f"Vidas: {'💗 ' * vidas}",
    font=("Arial", 14, "bold"),
    bg="tomato",
    fg="white"
)
lbl_vidas.pack(anchor="e", padx=25)

lbl_info_actual=tk.Label(
    frame_actual,
    text="",
    font=("Arial", 18, "bold"),
    bg="tomato",
    fg="white"
)
lbl_info_actual.pack()

lbl_palabra = tk.Label(
    frame_palabra,
    text="",
    font=("Arial", 28, "bold"),
    bg="tomato",
    fg="white"
)
lbl_palabra.pack()







mostrar_frame(frame_inicio)
ventana.mainloop()