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

def descubrir_letra (contador,letra,palabra,*args):
    """
    Verifica si la letra ingresada se encuentra en la palabra a adivinar y,
    por cada coincidencia, reemplaza el guion bajo ('_') por la letra
    correspondiente en la posición correcta.

    Además, incrementa un contador que indica cuántas veces aparece la letra
    descubierta en la palabra.

    :param contador: Cantidad de veces que la letra ya fue encontrada.
    :param letra: Letra ingresada por el usuario.
    :param palabra: Palabra a adivinar.
    :param args: Estado actual de la palabra (letras descubiertas y guiones bajos).
    :return: Tupla con la lista actualizada de la palabra y el contador de apariciones.
    """
    lista=list(args)
    for indice in range(len(lista)):
        if lista[indice]=='_' and palabra[indice]==letra:
            lista[indice]=letra.upper()
            contador+=1
    return lista,contador

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

def actualizar_vidas (contador,vidas,vidas_perdidas):
    """
    Actualiza la cantidad de vidas restantes del jugador según el resultado
    del intento actual y muestra el estado visual de las vidas.

    Si la letra ingresada no fue encontrada (contador == 0), se descuenta una vida.
    En caso contrario, las vidas se mantienen sin cambios.

    :param contador: Cantidad de veces que la letra ingresada aparece en la palabra.
    :param vidas: Cantidad de vidas actuales del jugador.
    :param vidas_perdidas: Cantidad de vidas ya perdidas.
    :return: Tupla con la cantidad actualizada de vidas y vidas perdidas.
    """
    if contador==0:
        vidas-=1
        vidas_perdidas=7-vidas 
        print(f'Vidas: {vidas_perdidas*"❌"}{vidas*"💗"}')
    elif contador_adivinar>0 and vidas<7:
        print(f'Vidas: {vidas_perdidas*"❌"}{vidas*"💗"}')
    else:
        print(f'Vidas: {vidas*"💗"}')
    return vidas,vidas_perdidas

vidas=7
vidas_perdidas=0
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
                                completa=palabra_con_guiones(palabra)
                                print(' '.join(completa))
                                print(f'Vidas: {vidas*"💗"}')
                                while vidas!=0:
                                    letra_ingresada=input('Ingrese una letra: ').strip().lower()
                                    contador_adivinar=0
                                    if letra_ingresada.isalpha():
                                        completa,contador_adivinar=descubrir_letra(contador_adivinar,letra_ingresada,palabra,*completa)
                                    print(' '.join(completa))
                                    vidas,vidas_perdidas=actualizar_vidas(contador_adivinar,vidas,vidas_perdidas)
                                    if vidas==0:
                                        print('💀 Perdiste! Te quedaste sin vidas')
                                    if len(completa)==len(palabra) and hay_guiones(*completa)==False:
                                        print('GANASTE! 🎉🎉🎉')
                                        break
                            case 2:
                                palabra=random.choice(niveles.get('intermedio'))
                                completa=palabra_con_guiones(palabra)
                                print(' '.join(completa))
                                print(f'Vidas: {vidas*"💗"}')
                                while vidas!=0:
                                    letra_ingresada=input('Ingrese una letra: ').strip().lower()
                                    contador_adivinar=0
                                    if letra_ingresada.isalpha():
                                        completa,contador_adivinar=descubrir_letra(contador_adivinar,letra_ingresada,palabra,*completa)
                                    print(' '.join(completa))
                                    vidas,vidas_perdidas=actualizar_vidas(contador_adivinar,vidas,vidas_perdidas)
                                    if vidas==0:
                                        print('💀 Perdiste! Te quedaste sin vidas')
                                    if len(completa)==len(palabra) and hay_guiones(*completa)==False:
                                        print('GANASTE! 🎉🎉🎉')
                                        break
                            case 3:
                                palabra=random.choice(niveles.get('dificil'))
                                completa=palabra_con_guiones(palabra)
                                print(' '.join(completa))
                                print(f'Vidas: {vidas*"💗"}')
                                while vidas!=0:
                                    letra_ingresada=input('Ingrese una letra: ').strip().lower()
                                    contador_adivinar=0
                                    if letra_ingresada.isalpha():
                                        completa,contador_adivinar=descubrir_letra(contador_adivinar,letra_ingresada,palabra,*completa)
                                    print(' '.join(completa))
                                    vidas,vidas_perdidas=actualizar_vidas(contador_adivinar,vidas,vidas_perdidas)
                                    if vidas==0:
                                        print('💀 Perdiste! Te quedaste sin vidas')
                                    if len(completa)==len(palabra) and hay_guiones(*completa)==False:
                                        print('GANASTE! 🎉🎉🎉')
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