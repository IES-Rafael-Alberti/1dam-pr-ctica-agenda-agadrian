"""
# TODO: comprobar si al mostrar un contacto por criterio y hay dos criterios iguales, si muestra 1 o los 2 o los que hayan
# TODO: (SI ME DA TIEMPO)comprobar si el numero al agregar contacto ya existe o no
# TODO: crear otra funcion para impirmir en la opc 6 los contactos, (no usar la misma que ya tenia de mosrtar)
# 

27/11/2023

Práctica del examen para realizar en casa
-----------------------------------------

* El programa debe estar correctamente documentado.

* Debes intentar ajustarte lo máximo que puedas a lo que se pide en los comentarios TODO.

* Tienes libertad para desarrollar los métodos o funciones que consideres, pero estás obligado a usar como mínimo todos los que se solicitan en los comentarios TODO.

* Además, tu programa deberá pasar correctamente las pruebas unitarias que se adjuntan en el fichero test_agenda.py, por lo que estás obligado a desarrollar los métodos que se importan y prueban en la misma: pedir_email(), validar_email() y validar_telefono()

"""

import os
import pathlib
from os import path
import copy

# Constantes globales
RUTA = pathlib.Path(__file__).parent.absolute() 

NOMBRE_FICHERO = 'contactos.csv'

RUTA_FICHERO = path.join(RUTA, NOMBRE_FICHERO)

#TODO: Crear un conjunto con las posibles opciones del menú de la agenda
OPCIONES_MENU = {1, 2, 3, 4, 5, 6, 7, 8}
#TODO: Utiliza este conjunto en las funciones agenda() y pedir_opcion()


def borrar_consola():
    """ Limpia la consola
    """
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")



def pulse_tecla_para_continuar():
    """ Muestra un mensaje y realiza una pausa hasta que se pulse una tecla
    """
    print("\n")
    os.system("pause")



######################################
### FUNCION IMPRIMIR MENU Y OPCION ###
######################################

def mostrar_menu():
    """ 
    Muestra las opciones del menu disponibles para elejir
    """
    print("AGENDA")
    print("-" * len("AGENDA"))
    print("1. Nuevo contacto")
    print("2. Modificar contacto")
    print("3. Eliminar contacto")
    print("4. Vaciar agenda")
    print("5. Cargar agenda inicial")
    print("6. Mostrar contactos por criterio")
    print("7. Mostrar la agenda completa")
    print("8. Salir")



def pedir_opcion():
    opc_ok = False
    while not opc_ok:
        try:
            opc = int(input("Elije una opcion: "))
            if opc in OPCIONES_MENU:
                return opc 
            else:
                print("Elije opcion correcta (1-8)")

        except ValueError:
            print("Debes ingresar valor numerico (1-8))")



######################
### FUNCION AGENDA ###
######################

def agenda(contactos: list):
    """ Ejecuta el menú de la agenda con varias opciones
    ...
    """
    #TODO: Crear un bucle para mostrar el menú y ejecutar las funciones necesarias según la opción seleccionada...
    opcion = 0
    while opcion != 8:
        mostrar_menu()
        opcion = pedir_opcion()

        #TODO: Se valorará que utilices la diferencia simétrica de conjuntos para comprobar que la opción es un número entero del 1 al 7

        if opcion == 1:
            agregar_contacto(contactos)
        elif opcion == 2:
            modificar_contacto(contactos)   
        elif opcion == 3:
            email = input("Introduce email de contacto a eliminar: ")
            eliminar_contacto(contactos, email)
        elif opcion == 4:
            vaciar_agenda(contactos)
        elif opcion == 5:
            cargar_contactos(contactos)
        elif opcion == 6:
            mostrar_contactos_criterio(contactos)
        elif opcion == 7:
            mostrar_contactos(contactos)
            


###################################
### FUNCIONES AGREGAR CONTACTOS ###
###################################

# TODO: controlar la introduccion de espacios en medio de un nombre compuesot, o del mail o apellido. Usar quizas el .split() y luego unir de nuevo las palabras de la lista creada por split

def pedir_nombre():
    nombre_ok = False
    while not nombre_ok:
        try:
            nombre = input("Nombre: ").title()
            validar_nombre(nombre)
            return nombre
        except ValueError as e:
            print("Error " + str(e))


def validar_nombre(nombre):
    if nombre.strip() == '':
        raise ValueError("Nombre incorrecto")
    return True



def pedir_apellido():
    apelllido_ok = False
    while not apelllido_ok:
        try:
            apellido = input("Apellido: ").title()
            validar_apellido(apellido)
            return apellido
        except ValueError as e:
            print("Error " + str(e))


def validar_apellido(apellido):
    if apellido.strip() == '':
        raise ValueError("Apellido incorrecto")

    return True



def pedir_email(contactos):
    email_ok = False
    while not email_ok:
        try:
            email = input("Email: ").strip()
            validar_email(email, contactos)
            return email
        except ValueError as e:
            print("Error: " + str(e))


def validar_email(email, contactos): #TODO: Comprobar que el correo no existe
    if email.lower() in (correo["email"].lower() for correo in contactos):
        raise ValueError("el email ya existe en la agenda")
    
    if email.strip() == '':
        raise ValueError("el email no puede ser una cadena vacía")
    
    if "@" not in email:
        raise ValueError("el email no es un correo válido")
    
    return True


def pedir_telefonos() -> list:
    telefono_ok = False
    lista_telefonos = []
    while not telefono_ok:
        try:
            telefono = input("Introduce telefonos (enter vacio para parar): ").strip().replace(" ", "")

            if telefono == '':
                telefono_ok = True
                return lista_telefonos
            
            if validar_telefonos(telefono):
                lista_telefonos.append(telefono)
        except ValueError as e:
            print("Error: " + str(e))


def validar_telefonos(telefono):
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
    email = pedir_email(contactos)
    telefonos = pedir_telefonos()

    contactos.append(dict([("nombre", nombre), ("apellido", apellido), ("email", email), ("telefonos", telefonos) ]))
    print("Contacto añadido correctamente")

#####################################
### FUNCIONES MODIFICAR CONTACTOS ###
#####################################

# TODO

def modificar_contactos(agenda:list):
    pass




####################################
### FUNCIONES ELIMINAR CONTACTOS ###
####################################

def buscar_contacto(contactos:list, email):
    """
    Busca la posicion de un contacto en la lista, a partir de su email

    Args:
        contactos: lista de contactos
        email: correo de el contacto a eliminar
    """
    for contacto in range(len(contactos)):
        if contactos[contacto]["email"] == email:
            return contacto
    
    return None


def eliminar_contacto(contactos: list, email):
    """ Elimina un contacto de la agenda a traves de un correo
    
    Args:
        contactos: lista de contactos
        email: correo para identificar el contacto a borrar
    """
    try:
        #TODO --: Crear función buscar_contacto para recuperar la posición de un contacto con un email determinado
        
        pos = buscar_contacto(contactos, email)

        if pos != None:
            del contactos[pos]
            print("Se eliminó 1 contacto")
        else:
            print("No se encontró el contacto para eliminar")
    except Exception as e:
        print(f"**Error** {e}")
        print("No se eliminó ningún contacto")



###############################
### FUNCIONES VACIAR AGENDA ###
###############################


def vaciar_agenda(contactos:list):
    contactos.clear()
    print("Agenda vaciada correctamente")



############################################
### FUNCIONES CARGAR CONTACTOS INICIALES ###
############################################

def cargar_contactos(contactos: list):
    """ Carga los contactos iniciales de la agenda desde un fichero y los añade a una lista
    Args:
        contactos: lista previamente inicializada
    """
    #TODO: Controlar los posibles problemas derivados del uso de ficheros...

    with open(RUTA_FICHERO, 'r') as fichero:
        for linea in fichero:
            datos = linea.split(";")
            # Quitamos el /n del ultimo dato
            datos[-1] = datos[-1][:-1]  
            contactos.append(dict([ ("nombre", datos[0]), ("apellido", datos[1]), ("email", datos[2]), ("telefonos", datos[3:]) ]))


################################################
### FUNCIONES MOSTRAR CONTACTOS POR CRITERIO ###
################################################

def mostrar_contactos_criterio(contactos:list):
    """
    También deberás desarrollar la opción 6 que deberá preguntar por el criterio de búsqueda (nombre, apellido, email o telefono) y el valor a buscar para mostrar los contactos que encuentre en la agenda.
    """
    criterio = input("Mediante que criterio de busqueda quieres idetificar al contacto (nombre,apellido,email,telefono): ").lower().strip().replace(" ", "")

    while criterio not in {"nombre", "apellido", "email", "telefono"}:
        print("Debe elejir un criterio correcto (nombre,apellido,email,telefono): ")
        criterio = input().lower().strip().replace(" ", "")
    
    valor_criterio = input(f"Introduce {criterio}: ")
    
    # TODO: arreglar cuando elije criterio telefono, ya que contiene una lista
    cont = 0
    for contacto in range(len(contactos)):
        if contactos[contacto][criterio] == valor_criterio:
            mostrar_contactos([contactos[contacto]])
            cont+=1
    if cont == 0:
        print(f"No hay ningun {criterio} -> {valor_criterio}")
    
def imprimir_contacto_criterio(contactos:list, criterio, valor_criterio):
    print(f"Contactos con el criterio '{criterio}' y valor' {valor_criterio}")
    print("-----------------------------")




#########################################
### FUNCIONES MOSTRAR LISTA CONTACTOS ###
#########################################

def formatearTelefono(telefono:str):
    """
    Comrpueba si el telefono tiene prefijo y le añade un guion para separar el prefijo y el numero

    Args:
        telefono: str del telefono a comrobar
    
    Retorna: 
        el telefono: formateado si tiene prefijo, o el mismo que se pasa por parametro
    """
    if len(telefono) > 9:
        telefono = telefono[:-9] + "-" + telefono[-9:]

    return telefono


def mostrar_contactos(contactos: list):
    """
    Muestra de forma visual la lista de contactos ordenados por nombre y su informacion

    Args:
        contactos: lista de contactos
    """
    contactosOrdenados = copy.deepcopy(contactos)
    contactosOrdenados.sort(key=lambda nom: nom["nombre"])

    print(f"AGENDA ({len(contactos)})\n------")
    for contacto in contactosOrdenados:
        nombre = contacto["nombre"]
        apellido = contacto["apellido"]
        email = contacto["email"]
        telefonos = contacto["telefonos"]
        # Comprobamos si tiene telefono, si no tiene le damos el valor "ninguno"
        if not telefonos:
            msgTelefonos = "Ninguno"

        #Si tiene, formateamos el telefono en caso necesario, y comprobamos si tiene 1 o mas
        else:
            contacto["telefonos"] = list(formatearTelefono(telefono) for telefono in telefonos) 
            
            if len(telefonos) > 1:
                msgTelefonos =  " / ".join(map(str, contacto["telefonos"]))
            else:
                msgTelefonos = contacto["telefonos"][0]

        print(f"Nombre: {nombre} {apellido} ({email})\nTeléfonos: {msgTelefonos}")
        print("......")
        


def main():
    """ 
    Función principal del programa
    """
    borrar_consola()

    #TODO --: Asignar una estructura de datos vacía para trabajar con la agenda

    contactos = []

    #TODO --: Modificar la función cargar_contactos para que almacene todos los contactos del fichero en una lista con un diccionario por contacto (claves: nombre, apellido, email y telefonos)
    #TODO --: Realizar una llamada a la función cargar_contacto con todo lo necesario para que funcione correctamente.

    cargar_contactos(contactos)
    
    

    #TODO: Crear función para agregar un contacto. Debes tener en cuenta lo siguiente:
    # - El nombre y apellido no pueden ser una cadena vacía o solo espacios y se guardarán con la primera letra mayúscula y el resto minúsculas (ojo a los nombre compuestos)
    # - El email debe ser único en la lista de contactos, no puede ser una cadena vacía y debe contener el carácter @.
    # - El email se guardará tal cuál el usuario lo introduzca, con las mayúsculas y minúsculas que escriba. 
    #  (CORREO@gmail.com se considera el mismo email que correo@gmail.com)
    # - Pedir teléfonos hasta que el usuario introduzca una cadena vacía, es decir, que pulse la tecla <ENTER> sin introducir nada.
    # - Un teléfono debe estar compuesto solo por 9 números, aunque debe permitirse que se introduzcan espacios entre los números.
    # - Además, un número de teléfono puede incluir de manera opcional un prefijo +34.
    # - De igual manera, aunque existan espacios entre el prefijo y los 9 números al introducirlo, debe almacenarse sin espacios.
    # - Por ejemplo, será posible introducir el número +34 600 100 100, pero guardará +34600100100 y cuando se muestren los contactos, el telófono se mostrará como +34-600100100. 
    #TODO: Realizar una llamada a la función agregar_contacto con todo lo necesario para que funcione correctamente.

    agregar_contacto(contactos)

    pulse_tecla_para_continuar()
    borrar_consola()

    #TODO: Realizar una llamada a la función eliminar_contacto con todo lo necesario para que funcione correctamente, eliminando el contacto con el email rciruelo@gmail.com
    eliminar_contacto(contactos, "rciruelo@gmail.com")

    pulse_tecla_para_continuar()
    borrar_consola()

    #TODO --: Crear función mostrar_contactos para que muestre todos los contactos de la agenda con el siguiente formato:
    # ** IMPORTANTE: debe mostrarlos ordenados según el nombre, pero no modificar la lista de contactos de la agenda original **
    #
    # AGENDA (6)
    # ------
    # Nombre: Antonio Amargo (aamargo@gmail.com)
    # Teléfonos: niguno
    # ......
    # Nombre: Daniela Alba (danalba@gmail.com)
    # Teléfonos: +34-600606060 / +34-670898934
    # ......
    # Nombre: Laura Iglesias (liglesias@gmail.com)
    # Teléfonos: 666777333 / 666888555 / 607889988
    # ......
    # ** resto de contactos **
    #
    #TODO --: Realizar una llamada a la función mostrar_contactos con todo lo necesario para que funcione correctamente.

    mostrar_contactos(contactos)

    pulse_tecla_para_continuar()
    borrar_consola()

    #TODO: Crear un menú para gestionar la agenda con las funciones previamente desarrolladas y las nuevas que necesitéis:
    # AGENDA
    # ------
    # 1. Nuevo contacto
    # 2. Modificar contacto
    # 3. Eliminar contacto
    # 4. Vaciar agenda
    # 5. Cargar agenda inicial
    # 6. Mostrar contactos por criterio
    # 7. Mostrar la agenda completa
    # 8. Salir
    #
    # >> Seleccione una opción: 
    #
    #TODO: Para la opción 3, modificar un contacto, deberás desarrollar las funciones necesarias para actualizar la información de un contacto.
    #TODO: También deberás desarrollar la opción 6 que deberá preguntar por el criterio de búsqueda (nombre, apellido, email o telefono) y el valor a buscar para mostrar los contactos que encuentre en la agenda.

    agenda(contactos)


if __name__ == "__main__":
    main()