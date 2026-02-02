import os

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
        if (lista[indice]=='_' and palabra[indice]==letra):
            lista[indice]=letra.upper()
            contador+=1
    return lista,contador

def intentar_palabra_completa (palabra,palabra_arriesgada,lista):
    """
    Verifica si la palabra arriesgada por el jugador coincide con la palabra
    a adivinar.

    Si la palabra es correcta, reemplaza el estado actual de la palabra
    (guiones y letras descubiertas) por la palabra completa en mayúsculas.
    Si es incorrecta, la lista se devuelve sin cambios (la penalización
    se gestiona en otra función).

    :param palabra: Palabra correcta que debía adivinarse.
    :param palabra_arriesgada: Palabra ingresada por el jugador.
    :param lista: Estado actual de la palabra (letras y guiones).
    :return: Lista actualizada con la palabra completa si acertó,
             o la lista original si falló.
    """
    if palabra==palabra_arriesgada:
        lista=palabra.upper().split()
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

def penalizar_error_letra (contador,letra,letras_adivinadas,letras_incorrectas,vidas,vidas_perdidas):
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
    if contador==0 and (letra not in letras_adivinadas):
        letras_incorrectas+=letra
        vidas-=1
        vidas_perdidas=7-vidas 
        print(f'Vidas: {vidas_perdidas*"❌"}{vidas*"💗"}')
    else:
        print(f'Vidas: {vidas_perdidas*"❌"}{vidas*"💗"}')
    return vidas,vidas_perdidas,letras_incorrectas

def penalizar_error_palabra (palabra,palabra_arriesgada,vidas,vidas_perdidas):
    """
    Aplica la penalización correspondiente cuando el jugador arriesga
    la palabra completa y falla.

    Si la palabra arriesgada es incorrecta:
    - Se descuentan 2 vidas si el jugador tiene 2 o más.
    - Se descuenta 1 vida si solo le queda una.
    En caso de acierto, las vidas no se modifican.

    La función también muestra el estado visual actualizado de las vidas.

    :param palabra: Palabra correcta a adivinar.
    :param palabra_arriesgada: Palabra ingresada por el jugador.
    :param vidas: Cantidad de vidas actuales del jugador.
    :param vidas_perdidas: Cantidad de vidas ya perdidas.
    :return: Tupla con la cantidad actualizada de vidas y vidas perdidas.
    """
    if palabra!=palabra_arriesgada and vidas>=2:
        vidas-=2
        vidas_perdidas=7-vidas 
        print(f'Vidas: {vidas_perdidas*"❌"}{vidas*"💗"}')
    elif palabra!=palabra_arriesgada and vidas==1:
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
        letra=input('➡ Ingrese una letra: ').strip().lower()
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

def hay_letras_descubiertas(*args):
    """
    Verifica si al menos una letra de la palabra ya fue descubierta.

    La función recorre el estado actual de la palabra y determina
    si existe alguna letra alfabética (es decir, que no sea un guion).

    :param args: Estado actual de la palabra (letras descubiertas y guiones).
    :return: True si hay al menos una letra descubierta, False en caso contrario.
    """    
    lista=list(args)
    encontrado=False
    for indice in range(len(lista)):
        if lista[indice].isalpha():
            encontrado=True
    return encontrado

def mostrar_titulos(modo,nivel=None):
    """
    Limpia la terminal y muestra los títulos principales del juego
    según el modo y nivel seleccionados.

    :param modo (str): Modo de juego actual. Puede ser "Argento" o "Normal".
    :param nivel (str, optional): Nivel de dificultad del juego (solo se usa en modo normal).

    Notes
    -----
    - En modo Argento se muestra un título y una descripción especial.
    - En modo Normal se muestra el modo y el nivel elegido.
    """
    os.system('cls')
    print(f'{"💀 El Juego del Ahorcado 💀":^100}')
    if modo=="Argento":
        print(f'{"🔥 MODO ARGENTO 🔥":^100}')
        print('Palabras de la calle, del interior y bien de acá.')
    else:
        print(f'{f"Modo {modo}":^100}') 
        print(f'Nivel {nivel}')


def jugar_partida(palabra):
    """
    Ejecuta una partida completa del juego del ahorcado.

    Inicializa el estado de la palabra, las vidas del jugador y gestiona
    el ciclo principal del juego. Durante la partida:
    - Solicita letras al jugador.
    - Actualiza el estado de la palabra según los aciertos.
    - Penaliza la pérdida de vidas por errores de letras.
    - Permite arriesgar la palabra completa una vez que hay letras descubiertas,
      aplicando una penalización adicional en caso de error.

    La función finaliza cuando el jugador se queda sin vidas o
    logra descubrir la palabra completa, mostrando el resultado final.

    :param palabra: Palabra seleccionada para que el jugador intente adivinar.
    """
    completa=palabra_con_guiones(palabra)
    print(' '.join(completa))
    vidas=7
    vidas_perdidas=0
    letras_ingresadas=''
    letras_incorrectas=''
    print(f'Vidas: {vidas*"💗"}')
    print()
    while vidas>0 and hay_guiones(*completa):
        letra=pedir_letra()
        contador_adivinado=0
        completa,contador_adivinado=descubrir_letra(contador_adivinado,letra,palabra,*completa)
        print(' '.join(completa))
        vidas,vidas_perdidas,letras_incorrectas=penalizar_error_letra(contador_adivinado,letra,letras_ingresadas,letras_incorrectas,vidas,vidas_perdidas)
        if letra not in letras_ingresadas:
            letras_ingresadas+=letra
        if (hay_letras_descubiertas(*completa) and hay_guiones(*completa)) and vidas!=0:
            arriesgar='s'
            while arriesgar!='n':
                print()
                arriesgar=input('Probar una palabra, prodria perder 2 vidas. (S/N) ').strip().lower()
                if arriesgar=='s':
                    palabra_arriesgada=input('➡ Ingrese la palabra: ').strip().lower()
                    if palabra_arriesgada.isalpha():
                        completa=intentar_palabra_completa(palabra,palabra_arriesgada,completa)
                        print(' '.join(completa))
                        vidas,vidas_perdidas=penalizar_error_palabra(palabra,palabra_arriesgada,vidas,vidas_perdidas)
                        break
                    else:
                        print('Error: Entrada Inválida. Revise si la palabra ingresada contiene algún caracter no alfabético.')
                if arriesgar not in ('s','n'):
                    print('Error: Entrada Inválida.Intente nuevamente')
            if vidas!=0:
                if hay_guiones(*completa) and letras_incorrectas!='':
                    print()
                    print(f'Letras Incorrectas: {" - ".join(letras_incorrectas)}')
                    print()
                else:
                    print()
            else:
                print()
    mostrar_resultado(vidas,palabra)