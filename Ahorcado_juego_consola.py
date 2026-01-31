import os
os.system('cls')

from random import choice

import logica_juego as lj

from palabras_juego import modo_argento, normal_niveles

while True:
    jugar=input('¿Jugamos? (S/N) ').strip().lower()
    match jugar:
        case 's':
            while True:
                print('Modos de juego')
                print('1. Modo Normal\n2. Modo Argento')
                try:
                    modo=int(input('Elija el modo (1-2): ').strip())
                except ValueError:
                    print(f'Error: Entrada inválida. Ingrese el número 1 o 2. Intente nuevamente.')
                else:
                    match modo:
                        case 1:
                            while True:
                                print('Modo Normal')    
                                print('Niveles:\n1. Fácil\n2. Intermedio\n3. Difícil')
                                try:
                                    nivel=int(input('Elija el nivel (1-3): ').strip())
                                except ValueError:
                                    print(f'Error: Entrada inválida. Ingrese un número entero entre 1 y 3 Intente nuevamente.')
                                else:
                                    match nivel:
                                        case 1:
                                            palabra=choice(normal_niveles.get('facil'))
                                            lj.jugar_partida(palabra)
                                        case 2:
                                            palabra=choice(normal_niveles.get('intermedio'))
                                            lj.jugar_partida(palabra)
                                        case 3:
                                            palabra=choice(normal_niveles.get('dificil'))
                                            lj.jugar_partida(palabra)
                                        case _:
                                            print('Error: Entrada Inválida. Elija los niveles entre 1 y 3.')
                                            continue
                                    break 
                        case 2:
                            print('🔥 MODO ARGENTO 🔥')
                            print('Palabras de la calle, del interior y bien de acá.')
                            palabra=choice(list(modo_argento.keys()))
                            lj.jugar_partida(palabra)
                            for clave,valor in modo_argento[palabra].items():
                                if clave=="lunfardo":
                                    if valor:
                                        print('Pertenece al lunfardo rioplatense')
                                    else:
                                        print('No pertenece al lunfardo rioplatense')
                                else:
                                    print(f'{clave.replace("_", " ").capitalize()}: {valor}')
                        case _:
                            print('Error: Entrada Inválida. Elija los modos 1 y 2.')
                            continue
                    break 
        case 'n':
            break
        case _:
            print('Error: Entrada Inválida. Intente nuevamente.')