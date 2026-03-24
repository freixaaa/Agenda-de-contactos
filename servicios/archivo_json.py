import json
from modelos.contacto import contacto

def cargar_json(ruta):
    contactos = []
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            for c in datos:
                contactos.append(contacto(**c))
    except:
        pass
    return contactos

def guardar_json(ruta, contactos):
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump([c.to_dict() for c in contactos], archivo, indent=4)
