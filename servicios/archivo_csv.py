import csv
from modelos.contacto import contacto

def cargar_csv(ruta):
    contactos = []
    try:
        with open(ruta, newline="", encoding="utf-8") as archivo:
            reader = csv.DictReader(archivo)
            for fila in reader:
                contactos.append(contacto(**fila))
    except:
        pass
    return contactos

def guardar_csv(ruta, contactos):
    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        campos = ["nombre", "telefono", "email", "edad", "residencia"]
        writer = csv.DictWriter(archivo, fieldnames=campos)
        writer.writeheader()
        for c in contactos:
            writer.writerow(c.to_dict())
