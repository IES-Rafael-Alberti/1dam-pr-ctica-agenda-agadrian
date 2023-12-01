
#### AÑADIR AL ARCHIVPO PRICNIPIAL
import os
import pathlib
from os import path
contactos = [
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

"""def cargar_contactos(contactos: list):
     Carga los contactos iniciales de la agenda desde un fichero y los añade a una lista
    Args:
        contactos: lista previamente inicializada
    
    #TODO: Controlar los posibles problemas derivados del uso de ficheros...

    with open(RUTA_FICHERO, 'r') as fichero:
        for linea in fichero:
            datos = linea.strip().split(";")
            # Quitamos el /n del ultimo dato
            #datos[-1] = datos[-1][:-1]  
            contactos.append(dict([ ("nombre", datos[0]), ("apellido", datos[1]), ("email", datos[2]), ("telefonos", datos[3:]) ]))
"""



###################################
### FUNCIONES AGREGAR CONTACTOS ###
###################################

def formatear_espacios(cadena):
    
    palabras = cadena.split(" ")
    cadena_sin_espacio = list((palabra for palabra in palabras if palabra != "" ))
    cadena_nueva = " ".join(cadena_sin_espacio)

    return cadena_nueva



def pedir_nombre():
    nombre_ok = False
    while not nombre_ok:
        try:
            nombre = input("Nombre: ").title().strip()
            validar_nombre(nombre)
            if " " in nombre:
                nombre = formatear_espacios(nombre)
            return nombre
        except ValueError as e:
            print("Error " + str(e))


def validar_nombre(nombre):
    if nombre == '':
        raise ValueError("Nombre incorrecto")



def pedir_apellido():
    apelllido_ok = False
    while not apelllido_ok:
        try:
            apellido = input("Apellido: ").title().strip()
            validar_apellido(apellido)
            return apellido
        except ValueError as e:
            print("Error " + str(e))


def validar_apellido(apellido):
    if apellido == '':
        raise ValueError("Apellido incorrecto")



def pedir_email(contactos):
    """try:"""
    email = input("Email: ").strip()
    if validar_email(email, contactos):
        return email
    """except ValueError as e:
        print("Error: " + str(e))"""

def validar_email(email, contactos): 
    if email.lower() in (correo["email"].lower() for correo in contactos):
        raise ValueError("el email ya existe en la agenda")
    
    if email.strip() == '':
        raise ValueError("el email no puede ser una cadena vacía")
    
    if "@" not in email:
        raise ValueError("el email no es un correo válido")
    
    if " " in email:
        raise ValueError("el email no puede tener espacios")

    return True
   #


def pedir_telefonos() -> list:
    telefono_ok = False
    lista_telefonos = []
    while not telefono_ok:
        try:
            telefono = input("Introduce telefonos (enter vacio para parar): ").strip().replace(" ", "")

            if telefono == '':
                telefono_ok = True
                return lista_telefonos
            
            if validar_telefono(telefono):
                lista_telefonos.append(telefono)
        except ValueError as e:
            print("Error: " + str(e))


def validar_telefono(telefono):
    """
    
    """
    if (len(telefono) == 9 and not telefono.isdigit()) or (telefono[:3] == "+34" and not telefono[3:12].isdigit()):
        raise ValueError("Debes introducir caracteres numericos")
    
    if len(telefono) > 9:
        if telefono[-12:-9] == "+34":
            return True
        else:
            raise ValueError("Numero debe contener 9 digitos y opcionalmente un prefijo +34")
    else:
        if len(telefono) < 9:
            raise ValueError("Numero debe contener 9 digitos y opcionalmente un prefijo +34")
    
    return True



def agregar_contacto(contactos:list):
    """
    Añade un contacto a la lista con los valores introducidos

    Args:
        contactos: lista de contactos
    
    """
    print("Datos a introducir\n-----------------")
    nombre = pedir_nombre()
    apellido = pedir_apellido()

    email = None
    while not email:
        email = pedir_email(contactos)

    telefonos = pedir_telefonos()

    contactos.append(dict([("nombre", nombre), ("apellido", apellido), ("email", email), ("telefonos", telefonos) ]))
    print("Contacto añadido correctamente")


agregar_contacto(contactos)