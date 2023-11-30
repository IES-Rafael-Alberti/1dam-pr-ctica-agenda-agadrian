
#### AÑADIR AL ARCHIVPO PRICNIPIAL

contactos = [
    {"nombre": "Laura", "apellido": "Iglesias", "email": "liglesias@gmail.com", "telefonos": ["666777333", "666888555", "607889988"]},
    {"nombre": "Antonio", "apellido": "Amargo", "email": "aamargo@gmail.com", "telefonos": []},
    {"nombre": "Marta", "apellido": "Copete", "email": "marcopete@gmail.com", "telefonos": ["+34600888800"]},
    {"nombre": "Rafael", "apellido": "Ciruelo", "email": "rciruelo@gmail.com", "telefonos": ["+34607212121", "655001122"]},
    {"nombre": "Daniela", "apellido": "Alba", "email": "danalba@gmail.com", "telefonos": ["+34600606060", "+34670898934"]},
    {"nombre": "Rogelio", "apellido": "Rojo", "email": "rogrojo@gmail.com", "telefonos": ["610000099", "645000013"]}, {"nombre": "Rafael", "apellido": "Copete", "email": "marcopete@gmail.com", "telefonos": ["+34600888800"]}
    ]


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




def mostrar_contactos_criterio(contactos:list):
    """
    También deberás desarrollar la opción 6 que deberá preguntar por el criterio de búsqueda (nombre, apellido, email o telefono) y el valor a buscar para mostrar los contactos que encuentre en la agenda.
    """
    criterio = input("Mediante que criterio de busqueda quieres idetificar al contacto (nombre,apellido,email,telefono): ").lower().strip().replace(" ", "")

    while criterio not in {"nombre", "apellido", "email", "telefono"}:
        criterio = input("Debe elejir un criterio correcto (nombre,apellido,email,telefono): ").lower().strip().replace(" ", "")
    
    
    valor_criterio = input(f"Introduce {criterio}: ").title()
    
    # TODO: arreglar cuando elije criterio telefono, ya que contiene una lista
   
        

    cont = 0
    for contacto in range(len(contactos)):
        if criterio == "telefono":
            for numero in contactos[contacto]["telefonos"]:
                if numero == valor_criterio.lower():
                    imprimir_contacto_criterio([contactos[contacto]], criterio, valor_criterio, cont)
                    cont +=1
        else: 
            if contactos[contacto][criterio] == valor_criterio.lower():
                imprimir_contacto_criterio([contactos[contacto]], criterio, valor_criterio, cont)
                cont+=1
    if cont == 0:
        print(f"No hay ningun {criterio} -> {valor_criterio}")
    



def imprimir_contacto_criterio(contactos:list, criterio, valor_criterio, cont):
    if cont == 0 :
        print(f"Contactos con el criterio '{criterio}' y valor '{valor_criterio}'")
    print("---------------------------------------------")
    for contacto in contactos:
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


mostrar_contactos_criterio(contactos)
