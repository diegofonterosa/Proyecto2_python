import os
from datetime import datetime

def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("\n=========================")
    print("  GESTOR DE ARCHIVOS ")
    print("=======================")
    print("1. Listar contenido")
    print("2. Crear directorio")
    print("3. Crear archivo")
    print("4. Escribir en archivo")
    print("5. Eliminar archivo o directorio")
    print("6. Ver información de archivo")
    print("7. Salir")
    print("===========================")
    
def listar_contenido():
    try:
        print("\n--- CONTENIDO DEL DIRECTORIO ---")
        elementos = os.listdir()
        
        if len(elementos) == 0:
            print("El directorio está vacío.")
            return
        
        for elemento in elementos:
            if os.path.isdir(elemento):
                print("[CARPETA]", elemento)
            else:
                print("[ARCHIVO]", elemento)
                
    except Exception as e:
        print("Error al listar:", e)
        
        
def crear_directorio():
    try:
        nombre = input("Nombre del archivo: ")
        if not nombre.endswith('.txt'):
            nombre = nombre + '.txt'
        if os.path.exists(nombre):
            print("Error: Ya existe un archivo con ese nombre.")
            return
        
        print("Escribe el contenido del archivo (escribe FIN para terminar):")
        contenido = []
        while True:
            linea = input()
            if linea.strip().upper() == "FIN":
                break
            contenido.append(linea)
            
        archivo = open(nombre, 'w')