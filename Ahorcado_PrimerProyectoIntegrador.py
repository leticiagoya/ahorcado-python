import os
os.system('cls')
import random


niveles={
'facil':['gato','casa','sol','mesa','perro','luna','flor','pan','mano','agua'],
'intermedio':['ventana','escuela','mochila','camisa','naranja',
            'teclado','botella','verano','domingo','montaña'],
'dificil':['murcielago','arquitectura','electricidad','responsabilidad','programacion',
         'biodiversidad','civilizacion','circunstancia','comunicacion','interpretacion']}
# modo_sorpresa=['bondi','laburo','pibe','mina','guita','chamuyo','quilombo','fiaca','gil','canchero']

def palabra_con_guiones(palabra):
    """
    Genera una lista de guiones bajos ('_') cuya longitud coincide
    con la cantidad de letras de la palabra a adivinar.

    Esta lista representa el estado inicial de la palabra, antes de
    que el jugador descubra alguna letra.

    :param palabra: Palabra a adivinar.
    :return: Lista de guiones bajos que representa la palabra oculta.
    """
    lista=[]
    for letra in palabra:
        lista.append('_')
    return lista

def letra_en_palabra (letra,palabra,*args):
    """
    Verifica si la letra ingresada se encuentra en la palabra a descubrir y,
    en caso afirmativo, reemplaza los guiones bajos ('_') por la letra
    correspondiente en las posiciones correctas.

    Devuelve una nueva lista que representa el estado actual de la palabra,
    compuesta por letras adivinadas y guiones bajos.

    :param letra: Letra ingresada por el usuario.
    :param palabra: Palabra a adivinar.
    :param args: Estado actual de la palabra (letras y guiones bajos).
    :return: Lista actualizada con las letras descubiertas.
    """
    lista=list(args)
    for indice in range(len(lista)):
        if lista[indice]=='_' and palabra[indice]==letra:
            lista[indice]=letra.upper()
        elif lista[indice]=='_' and palabra[indice]!=letra:
            vidas-=1    
    return lista

def hay_guiones(*args):
    """
    Verifica si existe al menos un guion bajo ('_') en la lista que representa
    el estado actual de la palabra a descubrir.

    Devuelve True si aún quedan letras por descubrir, y False si la palabra
    ya fue completada.

    :param args: Estado actual de la palabra (letras descubiertas y guiones bajos).
    :return: Booleano que indica si quedan guiones bajos.
    """
    lista=list(args)
    encontrado=False
    for indice in range(len(lista)):
        if lista[indice]=='_':
            encontrado=True
    return encontrado

def perder_vidas (letra,palabra,*args):
    """
    Verifica si la letra ingresada se encuentra en la palabra a descubrir y,
    en caso afirmativo, reemplaza los guiones bajos ('_') por la letra
    correspondiente en las posiciones correctas.

    Devuelve una nueva lista que representa el estado actual de la palabra,
    compuesta por letras adivinadas y guiones bajos.

    :param letra: Letra ingresada por el usuario.
    :param palabra: Palabra a adivinar.
    :param args: Estado actual de la palabra (letras y guiones bajos).
    :return: Lista actualizada con las letras descubiertas.
    """
    lista=list(args)
    pierde_vida=False
    for indice in range(len(lista)):
        if lista[indice]=='_' and palabra[indice]!=letra:
               pierde_vida=True
    return pierde_vida

while True:
    try:
        jugar=input('¿Jugamos? (S/N) ').strip().lower()
        match jugar:
            case 's':
                while True:    
                    try:
                        print('Niveles:\n1. Fácil\n2. Intermedio\n3. Difícil')
                        nivel=int(input('Elija el nivel (1-3): ').strip())
                        match nivel:
                            case 1:
                                palabra=random.choice(niveles.get('facil'))
                                vidas=7
                                print(f'{vidas*"💗"}')
                                completa=palabra_con_guiones(palabra)
                                print(' '.join(completa))
                                while vidas!=0:
                                    letra_ingresada=input('Ingrese una letra: ').strip().lower()
                                    if letra_ingresada.isalpha():
                                        completa=letra_en_palabra(letra_ingresada,palabra,*completa)
                                    print(' '.join(completa))
                                    if perder_vidas(letra_ingresada,palabra,*completa):
                                        vidas-=1
                                    vidas_perdidas=7-vidas
                                    print(f'{vidas_perdidas*"❌"}{vidas*"💗"}')
                                    if vidas==0:
                                        print('💀 Perdiste! Te quedaste sin vidas')
                                    if len(completa)==len(palabra) and hay_guiones(*completa)==False:
                                        break
                            case 2:
                                palabra=random.choice(niveles.get('intermedio'))
                                completa=palabra_con_guiones(palabra)
                                print(' '.join(completa))
                                while True:
                                    letra_ingresada=input('Ingrese una letra: ').strip().lower()
                                    if letra_ingresada.isalpha():
                                        completa=letra_en_palabra(letra_ingresada,palabra,*completa)
                                    print(' '.join(completa))
                                    if len(completa)==len(palabra) and hay_guiones(*completa)==False:
                                        break
                            case 3:
                                palabra=random.choice(niveles.get('dificil'))
                                completa=palabra_con_guiones(palabra)
                                print(' '.join(completa))
                                while True:
                                    letra_ingresada=input('Ingrese una letra: ').strip().lower()
                                    if letra_ingresada.isalpha():
                                        completa=letra_en_palabra(letra_ingresada,palabra,*completa)
                                    print(' '.join(completa))
                                    if len(completa)==len(palabra) and hay_guiones(*completa)==False:
                                        break
                            case _:
                                raise ValueError ('Entrada Inválida. Elija los niveles entre 1 y 3.')
                        break
                    except ValueError as e:
                        print(f"Error: {str(e)}. Intente nuevamente.")
                
            case 'n':
                break
            case _:
                raise ValueError ('Entrada Inválida.')
    except ValueError as e:
        print(f"Error: {str(e)}. Intente nuevamente.")