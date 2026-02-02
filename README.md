💀 El Juego del Ahorcado

Proyecto del clásico Juego del Ahorcado, desarrollado en Python, con dos versiones jugables:

    🎮 Versión Consola

    🖥️ Versión Gráfica (Tkinter)

El objetivo es adivinar la palabra antes de quedarte sin vidas, ingresando letras una por una.
-----------------------------------------------------------------------------------------------------------------
✨ Características generales

    • Palabras aleatorias

    • Sistema de vidas

    • Validación de letras ingresadas

    • Mensajes de victoria y derrota

    • Estructura modular del código

    • Proyecto pensado como práctica de lógica y estructura de un juego completo
-----------------------------------------------------------------------------------------------------------------
🎮 Versión Consola

La versión por consola se juega desde la terminal y cuenta con las siguientes características:

    • Modo Normal con niveles (fácil, intermedio, difícil)

    • Modo Argento 🇦🇷 con palabras de uso cotidiano argentino. 
      Al finalizar la partida se muestra:

        ➡ Significado

        ➡ Uso principal

        ➡ Si forma parte o no del lunfardo

    • Limpieza de pantalla y títulos dinámicos

    • Sistema de letras usadas

    • Opción de arriesgar la palabra completa
      Una vez descubierta al menos una letra, el jugador puede intentar adivinar la palabra completa para ganar la partida, a costa de perder 2 vidas
 
 - Archivo principal: Ahorcado_juego_consola.py
 
-----------------------------------------------------------------------------------------------------------------
🖥️ Versión Gráfica (Tkinter)

La versión gráfica fue desarrollada usando Tkinter y ofrece una experiencia visual más interactiva:

    • Menú de inicio

    • Selección de modo 
    
    • Selección de nivel en el Modo Normal

    • Interfaz con botones y etiquetas

    • Visualización de vidas con íconos

    • Modo Argento 🇦🇷 con palabras de uso cotidiano argentino. 
      Al finalizar la partida se muestra:

        ➡ Significado

        ➡ Uso principal

        ➡ Si forma parte o no del lunfardo

    • Retorno al menú mediante teclado (ENTER o ESPACIO)

 - Archivo principal: Ahorcado_juego_tkinter.py

🔎 Nota: la versión gráfica no incluye la opción de arriesgar la palabra completa como en la versión consola

🗂️ Estructura del proyecto
├── Ahorcado_juego_consola.py
├── Ahorcado_juego_tkinter.py
├── logica_juego.py
├── palabras_juego.py
└── README.md









