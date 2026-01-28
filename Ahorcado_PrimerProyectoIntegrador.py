import os
os.system('cls')
import random


niveles={
'facil':['gato','casa','sol','mesa','perro','luna','flor','pan','mano','agua'],
'intermedio':['ventana','escuela','mochila','camisa','naranja',
            'teclado','botella','verano','domingo','montaña'],
'dificil':['murciélago','arquitectura','electricidad','responsabilidad','programación',
         'biodiversidad','civilización','circunstancia','comunicación','interpretación']}
# modo_sorpresa=['bondi','laburo','pibe','mina','guita','chamuyo','quilombo','fiaca','gil','canchero']

# lista=['a','b','c']
# print(lista)
# lista[0]='d'
# print(lista)

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
                                completa=[]
                                for letra in palabra:
                                    completa.append('_')
                                print(' '.join(completa))
                                while True:
                                    letra_ingresada=input('Ingrese una letra: ').strip().lower()
                                    if letra_ingresada.isalpha():
                                        for indice in range(len(completa)):
                                            if completa[indice]=='_'and palabra[indice]==letra_ingresada:
                                                completa[indice]= letra_ingresada.upper()
                                    print(' '.join(completa))
                                    encontrado=False
                                    for indice in range(len(completa)):
                                        if completa[indice]=='_':
                                            encontrado=True
                                    if len(completa)==len(palabra) and encontrado==False:
                                        print(palabra.upper())
                                        break
                            case 2:
                                print('Intermedio')
                            case 3:
                                print('Difícil')
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