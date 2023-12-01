
#### AÑADIR AL ARCHIVPO PRICNIPIAL
import os
import pathlib
from os import path
contactos2 = [
    {"nombre": "Laura", "apellido": "Iglesias", "email": "liglesias@gmail.com", "telefonos": ["666777333", "666888555", "607889988"]},
    {"nombre": "Antonio", "apellido": "Amargo", "email": "aamargo@gmail.com", "telefonos": []},
    {"nombre": "Marta", "apellido": "Copete", "email": "marcopete@gmail.com", "telefonos": ["+34600888800"]},
    {"nombre": "Rafael", "apellido": "Ciruelo", "email": "rciruelo@gmail.com", "telefonos": ["+34607212121", "655001122"]},
    {"nombre": "Daniela", "apellido": "Alba", "email": "danalba@gmail.com", "telefonos": ["+34600606060", "+34670898934"]},
    {"nombre": "Rogelio", "apellido": "Rojo", "email": "rogrojo@gmail.com", "telefonos": ["610000099", "645000013"]}, {"nombre": "Rafael", "apellido": "Copete", "email": "marcopete@gmail.com", "telefonos": ["+34600888800"]}
    ]

contactos = []

RUTA = pathlib.Path(__file__).parent.absolute() 

NOMBRE_FICHERO = 'contactos.csv'

RUTA_FICHERO = path.join(RUTA, NOMBRE_FICHERO)

def cargar_contactos(contactos: list):
    """ Carga los contactos iniciales de la agenda desde un fichero y los añade a una lista
    Args:
        contactos: lista previamente inicializada
    """
    #TODO: Controlar los posibles problemas derivados del uso de ficheros...

    with open(RUTA_FICHERO, 'r') as fichero:
        for linea in fichero:
            datos = linea.strip().split(";")
            # Quitamos el /n del ultimo dato
            #datos[-1] = datos[-1][:-1]  
            contactos.append(dict([ ("nombre", datos[0]), ("apellido", datos[1]), ("email", datos[2]), ("telefonos", datos[3:]) ]))


print(contactos)
cargar_contactos(contactos)
print(contactos)