import os
os.system('cls')

from random import choice

import logica_juego as lj

from palabras_juego import modo_argento, normal_niveles

print(f'{"💀 El Juego del Ahorcado 💀":^100}')
print(f'{"Adiviná la palabra antes de quedarte sin vidas 😉":^100}')

while True:
    jugar=input('¿Jugamos? (S/N) ').strip().lower()
    
    match jugar:
        case 's':
            while True:
                os.system('cls')
                print(f'{"💀 El Juego del Ahorcado 💀":^100}')
                print('Modos de juego:')
                print('1. Modo Normal\n2. Modo Argento')
                try:
                    modo=int(input('Elija el modo (1-2): ').strip())
                except ValueError:
                    print(f'Error: Entrada inválida. Ingrese el número 1 o 2. Intente nuevamente.')
                else:
                    match modo:
                        case 1:
                            modo="Normal"
                            while True:
                                os.system('cls')
                                print(f'{"💀 El Juego del Ahorcado 💀":^100}')
                                print(f'{"Modo Normal":^100}')    
                                print('Niveles:\n1. Fácil\n2. Intermedio\n3. Difícil')
                                try:
                                    nivel=int(input('Elija el nivel (1-3): ').strip())
                                except ValueError:
                                    print(f'Error: Entrada inválida. Ingrese un número entero entre 1 y 3 Intente nuevamente.')
                                else:
                                    match nivel:
                                        case 1:
                                            nivel_elegido="Fácil"
                                            lj.mostrar_titulos(modo,nivel_elegido)
                                            palabra=choice(normal_niveles.get('facil'))
                                            lj.jugar_partida(palabra)
                                            print()
                                        case 2:
                                            nivel_elegido="Intermedio"
                                            lj.mostrar_titulos(modo,nivel_elegido)
                                            palabra=choice(normal_niveles.get('intermedio'))
                                            lj.jugar_partida(palabra)
                                            print()
                                        case 3:
                                            nivel_elegido="Difícil"
                                            lj.mostrar_titulos(modo,nivel_elegido)
                                            palabra=choice(normal_niveles.get('dificil'))
                                            lj.jugar_partida(palabra)
                                            print()
                                        case _:
                                            print('Error: Entrada Inválida. Elija los niveles entre 1 y 3.')
                                            continue
                                    break 
                        case 2:
                            modo="Argento"
                            lj.mostrar_titulos(modo)
                            palabra=choice(list(modo_argento.keys()))
                            lj.jugar_partida(palabra)
                            print(f' • Significado: {modo_argento[palabra].get("significado")}')
                            print(f' • Usado en: {modo_argento[palabra].get("uso_principal")}')
                            if modo_argento[palabra].get("lunfardo"):
                                print(' • Pertenece al lunfardo rioplatense')
                            else:
                                print(' • No pertenece al lunfardo rioplatense')
                            print()
                        case _:
                            print('Error: Entrada Inválida. Elija los modos 1 y 2.')
                            continue
                    break 
        case 'n':
            os.system('cls')
            print(f'{"💀 El Juego del Ahorcado 💀":^100}')
            print('Nos vemos! 😊 Vuelve pronto. 😉\n')
            break
        case _:
            print('Error: Entrada Inválida. Intente nuevamente.\n')