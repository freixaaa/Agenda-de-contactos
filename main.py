import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from servicios.agenda import agenda
from servicios.archivo_json import cargar_json, guardar_json
from servicios.archivo_csv import cargar_csv, guardar_csv

def mostrar_contactos(lista):
    for c in lista:
        print(f"nombre: {c.nombre}")
        print(f"telefono: {c.telefono}")
        print(f"email: {c.email}")
        print(f"edad: {c.edad}")
        print(f"residencia: {c.residencia}")
        print()

ag = agenda()

while True:
    print("1. cargar agenda desde archivo")
    print("2. agregar contacto")
    print("3. buscar contacto por nombre")
    print("4. buscar contacto por telefono")
    print("5. mostrar promedio de edad")
    print("6. mostrar todos los contactos")

    opcion = input()

    if opcion.lower() == "finalizar":
        break

    if opcion == "1":
        print("1. cargar desde json")
        print("2. cargar desde csv")
        sub = input()

        if sub == "1":
            ag.contactos = cargar_json("contactos.json")
            ag.ruta = "contactos.json"
            ag.tipo = "json"

        elif sub == "2":
            ag.contactos = cargar_csv("contactos.csv")
            ag.ruta = "contactos.csv"
            ag.tipo = "csv"

    elif opcion == "2":
        nombre = input("nombre: ")
        telefono = input("telefono: ")
        email = input("email: ")
        edad = input("edad: ")
        residencia = input("residencia: ")

        ag.agregar(nombre, telefono, email, edad, residencia)

        if ag.tipo == "json":
            guardar_json(ag.ruta, ag.contactos)
        elif ag.tipo == "csv":
            guardar_csv(ag.ruta, ag.contactos)

    elif opcion == "3":
        texto = input("buscar nombre: ")
        resultados = ag.buscar_nombre(texto)
        mostrar_contactos(resultados)

    elif opcion == "4":
        texto = input("buscar telefono: ")
        resultados = ag.buscar_telefono(texto)
        mostrar_contactos(resultados)

    elif opcion == "5":
        print(ag.promedio_edad())

    elif opcion == "6":
        mostrar_contactos(ag.mostrar())

    print()
    print("escriba 'finalizar' si desea salir del programa")print()print("'escriba finalizar' si desea salir del programa")
