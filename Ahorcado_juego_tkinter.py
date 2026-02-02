import tkinter as tk

from random import choice

from palabras_juego import modo_argento, normal_niveles

modo_actual = None
nivel_actual = None
palabra_actual = None

# =====================
# FUNCIONES DEL JUEGO
# =====================

def centrar_ventana(ventana, ancho, alto):
    """
    Centra una ventana de Tkinter en la pantalla.

    Calcula la posición necesaria para ubicar la ventana en el centro
    de la pantalla según el ancho y alto indicados, y ajusta su geometría.

    :param ventana (tk.Tk | tk.Toplevel): ventana a centrar.
    :param ancho (int): ancho deseado de la ventana en píxeles.
    :param alto (int): alto deseado de la ventana en píxeles.
    """
    ventana.update_idletasks() 
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()

    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)

    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

def mostrar_frame(frame):
    """
    Muestra un frame principal y oculta los demás.

    Oculta todos los frames principales de la aplicación y
    muestra únicamente el frame recibido como argumento.
    Se utiliza para navegar entre pantallas del juego.
    
    :param frame (tk.Frame): frame que se desea mostrar.
    """
    frame_inicio.place_forget()
    frame_modos.place_forget()
    frame_niveles.place_forget()
    frame_juego.place_forget()
    frame.place(relwidth=1, relheight=1)

def ir_a_modos():
    """
    Cambia la vista a la pantalla de selección de modos de juego.
    """
    mostrar_frame(frame_modos)

def ir_a_modo_normal():
    """
    Activa el modo de juego normal y muestra la pantalla
    de selección de niveles.
    """
    global modo_actual
    modo_actual = "normal"
    mostrar_frame(frame_niveles)   

def ir_a_modo_argento():
    """
    Activa el modo de juego argento.

    Selecciona una palabra aleatoria del modo argento,
    inicializa la partida, muestra la pantalla de juego
    y habilita la entrada de letras por teclado.
    """
    global modo_actual, palabra_actual

    modo_actual = "argento"
    palabra_actual = choice(list(modo_argento.keys()))

    print("Modo:", modo_actual)
    print("Palabra elegida:", palabra_actual)

    mostrar_frame(frame_juego)
    lbl_info_actual.config(text=f'🔥 MODO {modo_actual.upper()} 🔥\n'\
                           'Palabras de la calle, del interior y bien de acá.')
    resetear_partida()
    mostrar_palabra_oculta()
    ventana.bind("<Key>", tecla_presionada)

def iniciar_juego_normal(nivel):
    """
    Inicia una partida en modo normal según el nivel elegido.

    Selecciona una palabra aleatoria correspondiente al nivel,
    configura el estado actual del juego y muestra la pantalla
    de juego con la palabra oculta.

    :param nivel (str): nivel de dificultad seleccionado 
                        ('facil', 'intermedio' o 'dificil').
    """
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
    """
    Muestra la palabra actual en formato oculto,
    reemplazando cada letra por un guion bajo.
    """
    oculta = " ".join("_" for _ in palabra_actual)
    lbl_palabra.config(text=oculta)

def tecla_presionada(event):
    """
    Maneja la entrada del teclado durante la partida.

    Procesa únicamente letras válidas, evita repeticiones,
    actualiza la palabra oculta o las vidas según corresponda
    y verifica si el jugador ganó la partida.
    """
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

    if verificar_victoria():
        finalizar_juego(ganaste=True)

def actualizar_palabra():
    """
    Actualiza la visualización de la palabra en pantalla,
    mostrando las letras adivinadas y ocultando las restantes.
    """
    resultado = ""

    for letra in palabra_actual:
        if letra in letras_adivinadas:
            resultado += letra.upper() + " "
        else:
            resultado += "_ "

    lbl_palabra.config(text=resultado.strip())

def actualizar_vidas():
    """
    Actualiza el contador visual de vidas del jugador.

    Muestra corazones para las vidas restantes y cruces
    para las vidas perdidas. Finaliza el juego si las vidas
    llegan a cero.
    """
    corazones = "❤ " * vidas
    cruces = "❌ " * (7 - vidas)
    lbl_vidas.config(text=f"Vidas: {cruces}{corazones}")

    if vidas <= 0:
        finalizar_juego(ganaste=False)

def resetear_partida():
    """
    Reinicia el estado de la partida.

    Restaura las vidas iniciales, limpia las letras adivinadas
    y actualiza la visualización de vidas.
    """
    global vidas, letras_adivinadas
    vidas = 7
    letras_adivinadas.clear()
    actualizar_vidas()

def verificar_victoria():
    """
    Verifica si el jugador adivinó todas las letras
    de la palabra actual.

    :return bool: True si todas las letras fueron adivinadas,
                False en caso contrario.
    """
    for letra in palabra_actual:
        if letra not in letras_adivinadas:
            return False
    return True

def volver_al_inicio(event=None):
    """
    Vuelve a la pantalla de inicio del juego.

    Desactiva la captura de teclas y muestra el frame inicial.
    """
    ventana.unbind("<Key>")
    ventana.unbind("<Return>")
    ventana.unbind("<space>")
    mostrar_frame(frame_inicio)

def finalizar_juego(ganaste):
    """
    Finaliza la partida actual.

    Muestra el resultado (victoria o derrota), revela la palabra,
    presenta su significado si corresponde y habilita las teclas
    ENTER o ESPACIO para volver al inicio.

    :param ganaste (bool): indica si el jugador ganó o perdió la partida.
    """
    ventana.unbind("<Key>")

    if ganaste:
        lbl_palabra.config(text=f"🎉 {palabra_actual.upper()} 🎉")
        mostrar_significado_argento()
        lbl_info_actual.config(text="¡Ganaste! 🥳\n  ")
        lbl_volver_inicio.config(text="Presioná ENTER o ESPACIO para volver al inicio")

    else:
        lbl_palabra.config(text=f"💀 {palabra_actual.upper()} 💀")
        mostrar_significado_argento()
        lbl_info_actual.config(text="Perdiste 😢\n  ")
        lbl_volver_inicio.config(text="Presioná ENTER o ESPACIO para volver al inicio")

    ventana.bind("<Return>", volver_al_inicio)
    ventana.bind("<space>", volver_al_inicio)

def mostrar_significado_argento ():
    """
    Muestra en pantalla el significado de la palabra del modo Argento.

    Presenta la definición, el uso principal y aclara si la palabra
    forma parte o no del lunfardo rioplatense, utilizando la información
    almacenada en el diccionario del modo Argento.
    """
    if palabra_actual in list(modo_argento.keys()):
        if modo_argento[palabra_actual].get('lunfardo'):
            lbl_significado.config(
                text=f"Significado: {modo_argento[palabra_actual].get('significado')}\n"\
                f"Usado en: {modo_argento[palabra_actual].get('uso_principal')}\n"\
                f"Forma parte del lunfardo rioplatense")
        else:
            lbl_significado.config(
                text=f"Significado: {modo_argento[palabra_actual].get('significado')}\n"\
                f"Usado en: {modo_argento[palabra_actual].get('uso_principal')}\n"\
                f"No forma parte del lunfardo rioplatense")

# =============================================================
# Configuración de la ventana principal y la interfaz gráfica
# =============================================================

ventana=tk.Tk()
ventana.title('El Juego del Ahorcado')
ventana.config(bg="tomato")

centrar_ventana(ventana, 600, 500)
ventana.resizable(False, False)

frame_inicio = tk.Frame(ventana, bg="tomato")

pack_titulos= tk.Frame(frame_inicio, bg="tomato")
pack_titulos.pack(pady=50, fill="x")

lbl_titulo=tk.Label(
    pack_titulos,
    text="☠ El Juego del Ahorcado ☠",
    font=("Arial", 25, "bold"),
    bg="tomato",
    fg="white"
)
lbl_titulo.pack(pady=10)

lbl_subtitulo=tk.Label(
    pack_titulos,
    text="Adiviná la palabra antes de quedarte sin vidas 😉",
    font=("Arial", 15),
    bg="tomato",
    fg="white"
)
lbl_subtitulo.pack()

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
btn_jugar.pack(pady=50, anchor="center")

# ===============================
# Configuracióm del Frame Modos
# ===============================

frame_modos = tk.Frame(ventana, bg="tomato")

menu_centrado = tk.Frame(frame_modos, bg="tomato")
menu_centrado.place(relx=0.5, rely=0.4, anchor="center")

lbl_modos = tk.Label(
    menu_centrado,
    text="Elegí el modo de juego",
    font=("Arial", 18, "bold"),
    bg="tomato",
    fg="white"
)
lbl_modos.pack(pady=20)

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

# =================================================
# Configuracióm del Frame Niveles del Modo Normal
# =================================================

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

# ================================================
# Configuracióm del Frame Juego para ambos Modos
# ================================================

frame_juego = tk.Frame(ventana, bg="tomato")

frame_volver_vidas=tk.Frame(frame_juego,bg="tomato")
frame_volver_vidas.pack(fill="x",pady=10)

frame_actual=tk.Frame(frame_juego, bg="tomato")
frame_actual.pack(pady=8)

frame_palabra = tk.Frame(frame_juego, bg="tomato")
frame_palabra.pack(pady=50)

frame_significado=tk.Frame(frame_juego, bg="tomato")
frame_significado.pack(pady=5,fill="x")

frame_abajo=tk.Frame(frame_juego, bg="tomato")
frame_abajo.pack(side="bottom", fill="x")

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

lbl_significado = tk.Label(
    frame_significado,
    text="",
    font=("Arial", 15),
    bg="tomato",
    fg="white"
)
lbl_significado.pack(padx=20)

lbl_volver_inicio = tk.Label(
    frame_abajo,
    text="",
    font=("Arial", 12),
    bg="tomato",
    fg="black"
)
lbl_volver_inicio.pack(padx=10,pady=5)

mostrar_frame(frame_inicio)
ventana.mainloop()