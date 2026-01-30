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
    else:
        print(f'Vidas: {vidas_perdidas*"❌"}{vidas*"💗"}')
    return vidas,vidas_perdidas

def pedir_letra():
    """
    Solicita al usuario una letra para intentar descubrir la palabra.

    La función valida que la entrada sea un único carácter alfabético.
    Si la entrada no es válida, muestra un mensaje de error y vuelve
    a solicitar la letra hasta que el ingreso sea correcto.

    :return: Letra válida ingresada por el usuario, en minúscula.
    """
    while True:
        letra=input('Ingrese una letra: ').strip().lower()
        if len(letra)==1 and letra.isalpha():
            return letra
        else:
          print('Error: Entrada Inválida. Recuerde que de ingresar una sola letra.')

def mostrar_resultado(vidas,palabra):
    """
    Muestra el resultado final de la partida.

    Si el jugador se queda sin vidas, informa que ha perdido y revela
    la palabra a adivinar. En caso contrario, indica que el jugador
    ha ganado la partida.

    :param vidas: Cantidad de vidas restantes al finalizar la partida.
    :param palabra: Palabra que debía ser adivinada.
    """
    if vidas==0:
        print('💀 Perdiste! Te quedaste sin vidas')
        print(f'La palabra era: {" ".join(palabra.upper())}')
    else:
        print('GANASTE! 🎉🎉🎉')

def jugar_partida(palabra):
    """
    Ejecuta una partida completa del juego del ahorcado.

    Inicializa el estado de la palabra, las vidas del jugador y gestiona
    el ciclo principal del juego, solicitando letras, actualizando el
    estado de la palabra y las vidas, y verificando las condiciones de
    victoria o derrota.

    La función finaliza mostrando el resultado de la partida.

    :param palabra: Palabra seleccionada para que el jugador intente adivinar.
    """ 
    completa=palabra_con_guiones(palabra)
    print(' '.join(completa))
    vidas=7
    vidas_perdidas=0
    print(f'Vidas: {vidas*"💗"}')
    while vidas>0 and hay_guiones(*completa):
        letra=pedir_letra()
        contador_adivinar=0
        completa,contador_adivinar=descubrir_letra(contador_adivinar,letra,palabra,*completa)
        print(' '.join(completa))
        vidas,vidas_perdidas=actualizar_vidas(contador_adivinar,vidas,vidas_perdidas)
    mostrar_resultado(vidas,palabra)

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
                            palabra=random.choice(niveles.get('facil'))
                            jugar_partida(palabra)
                        case 2:
                            palabra=random.choice(niveles.get('intermedio'))
                            jugar_partida(palabra)
                        case 3:
                            palabra=random.choice(niveles.get('dificil'))
                            jugar_partida(palabra)
                        case _:
                            print('Error: Entrada Inválida. Elija los niveles entre 1 y 3.')
                            continue
                    break 
        case 'n':
            break
        case _:
            print('Error: Entrada Inválida. Intente nuevamente.')