import os
os.system('cls')
from random import choice
import logica_juego as lj

niveles={
'facil':['gato','casa','sol','mesa','perro','luna','flor','pan','mano','agua'],
'intermedio':['ventana','escuela','mochila','camisa','naranja',
            'teclado','botella','verano','domingo','montaña'],
'dificil':['murcielago','arquitectura','electricidad','responsabilidad','programacion',
         'biodiversidad','civilizacion','circunstancia','comunicacion','interpretacion']}
# modo_sorpresa=['bondi','laburo','pibe','mina','guita','chamuyo','quilombo','fiaca','gil','canchero']



while True:
    jugar=input('¿Jugamos? (S/N) ').strip().lower()
    match jugar:
        case 's':
            while True:    
                print('Niveles:\n1. Fácil\n2. Intermedio\n3. Difícil')
                try:
                    nivel=int(input('Elija el nivel (1-3): ').strip())
                except ValueError:
                    print(f'Error: Entrada inválida. Ingrese un número entero entre 1 y 3 Intente nuevamente.')
                else:
                    match nivel:
                        case 1:
                            palabra=choice(niveles.get('facil'))
                            lj.jugar_partida(palabra)
                        case 2:
                            palabra=choice(niveles.get('intermedio'))
                            lj.jugar_partida(palabra)
                        case 3:
                            palabra=choice(niveles.get('dificil'))
                            lj.jugar_partida(palabra)
                        case _:
                            print('Error: Entrada Inválida. Elija los niveles entre 1 y 3.')
                            continue
                    break 
        case 'n':
            break
        case _:
            print('Error: Entrada Inválida. Intente nuevamente.')