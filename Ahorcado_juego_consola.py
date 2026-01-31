import os
os.system('cls')
from random import choice
import logica_juego as lj

normal_niveles={
'facil':['gato','casa','sol','mesa','perro','luna','flor','pan','mano','agua'],
'intermedio':['ventana','escuela','mochila','camisa','naranja',
            'teclado','botella','verano','domingo','montaña'],
'dificil':['murcielago','arquitectura','electricidad','responsabilidad','programacion',
         'biodiversidad','civilizacion','circunstancia','comunicacion','interpretacion']}

modo_argento = {
    "bondi": {
        "significado": "Autobús o colectivo de transporte público.",
        "uso_principal": "Uso urbano en todo el país, especialmente Buenos Aires.",
        "lunfardo": True
    },
    "guita": {
        "significado": "Dinero.",
        "uso_principal": "Uso coloquial en toda Argentina.",
        "lunfardo": True
    },
    "laburo": {
        "significado": "Trabajo o empleo.",
        "uso_principal": "Uso general en Argentina.",
        "lunfardo": True
    },
    "pibe": {
        "significado": "Niño, adolescente o joven.",
        "uso_principal": "Uso general, especialmente en Buenos Aires.",
        "lunfardo": True
    },
    "mina": {
        "significado": "Mujer.",
        "uso_principal": "Uso coloquial urbano.",
        "lunfardo": True
    },
    "chamuyo": {
        "significado": "Charla engañosa o exagerada para convencer a alguien.",
        "uso_principal": "Uso urbano en todo el país.",
        "lunfardo": True
    },
    "quilombo": {
        "significado": "Situación caótica, problema o desorden.",
        "uso_principal": "Uso general en Argentina.",
        "lunfardo": True
    },
    "canchero": {
        "significado": "Persona segura de sí misma o con experiencia.",
        "uso_principal": "Uso general.",
        "lunfardo": True
    },
    "guri": {
        "significado": "Niño.",
        "uso_principal": "Litoral argentino (Entre Ríos, Corrientes, Misiones).",
        "lunfardo": False
    },
    "chango": {
        "significado": "Niño o muchacho.",
        "uso_principal": "Noroeste argentino (NOA).",
        "lunfardo": False
    },
    "yuyo": {
        "significado": "Planta silvestre o hierba.",
        "uso_principal": "Interior del país, zonas rurales.",
        "lunfardo": False
    },
    "guaso": {
        "significado": "Persona rústica, tosca o del campo.",
        "uso_principal": "Cuyo (San Juan, Mendoza, San Luis).",
        "lunfardo": False
    },
    "tonada": {
        "significado": "Forma particular de hablar, acento.",
        "uso_principal": "Cuyo, especialmente Mendoza.",
        "lunfardo": False
    },
    "culiao": {
        "significado": "Expresión intensificadora; puede ser insulto o muletilla.",
        "uso_principal": "Córdoba.",
        "lunfardo": False
    },
    "birra": {
        "significado": "Cerveza.",
        "uso_principal": "Uso general en Argentina.",
        "lunfardo": True
    },
    "macana": {
        "significado": "Error, mentira o problema.",
        "uso_principal": "Uso general.",
        "lunfardo": False
    },
    "fiaca": {
        "significado": "Pereza o falta de ganas.",
        "uso_principal": "Uso general, urbano.",
        "lunfardo": True
    },
    "boliche": {
        "significado": "Bar, local nocturno o discoteca.",
        "uso_principal": "Uso general.",
        "lunfardo": False
    },
    "empanada": {
        "significado": "Comida típica rellena y horneada o frita.",
        "uso_principal": "Todo el país.",
        "lunfardo": False
    },
    "mate": {
        "significado": "Infusión tradicional hecha con yerba mate.",
        "uso_principal": "Argentina y región del Cono Sur.",
        "lunfardo": False
    }
}


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