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
    """Mustra los archivos y carpetas"""
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
    """Crear un directorio nuevo"""
    try:
        nombre = input("Nombre del directorio: ")
        
        if os.path.exists(nombre):
            print("Error: Ya existe un directorio con ese nombre.")
            return
        
        os.mkdir(nombre)
        print("Directorio creado correctamente.")
        
    except Exception as e:
        print("Error al crear el directorio:", e)
    
    
def crear_archivo():
    """Crear un archivo nuevo"""
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
        for linea in contenido:
            archivo.write(linea + '\n')
        archivo.close()
        
    except Exception as e:
        print("Error al crear el archivo:", e)
        
def escribir_en_archivo():
    """Escribir en un archivo existente"""
    try:
        nombre = input("Nombre del archivo: ")
           
        if not os.path.exists(nombre):
            print("Error: El archivo no existe.")
            return
        if os.path.isdir(nombre):
            print("Error: Es un directorio, no un archivo.")
            return
        print("Escribe el contenido del archivo (escribe FIN para terminar):")
        contenido = []
        while True:
            linea = input()
            if linea.strip().upper() == "FIN":
                break
            contenido.append(linea)
               
            archivo = open(nombre, 'a')
            for linea in contenido:
                archivo.write(linea + '\n')
            archivo.close()
            
            print("Archivo añadido correctamente.")
    except Exception as e:
        print("Error al escribir en el archivo:", e)
           
def eliminar_elemento():
    """Eliminar un archivo o directorio"""
    try:
        nombre = input("Nombre del elemento que quiere eliminar")
            
        if not os.path.exists(nombre):
            print("Error: El elemento no existe")
            return
        
        confirmacion = input(f"¿Está seguro de que desea eliminar '{nombre}'? (s/n): ")
        if confirmacion.lower() != 's':
            print("operación cancelada.")
            return
        
        if os.path.isdir(nombre):
            os.rmdir(nombre)
            print("Directorio eliminado")
        else:
            os.remove(nombre)
            print("Archivo eliminado")
            
    except Exception as e:
        print("Error al eliminar el elemento:", e)
        
def mostrar_informacion():
    """Mostrar información de un archivo o directorio"""
    try:
        nombre = input("Nombre del elemento:   ")

        if not os.path.exists(nombre):
            print("Error: El elemento no existe.")
            return
        
        print("\n--- INFORMACIÓN ---")
        print("Nombre:", nombre)
        
        if os.path.isdir(nombre):
            print("Tipo: Directorio")
        else:
            print("Tipo: Archivo")
            
        info = os.stat(nombre)
        tamaño = info.st_size
        print("Tamaño:", tamaño, "bytes")
        
        fecha = datetime.fromtimestamp(info.st_mtime)
        print("Última modificación:", fecha.strftime("%Y-%m-%d %H:%M:%S"))
        
    except Exception as e:
        print("Error al obtener la información:", e)
        
def main():
    """Función principal del programa."""
    print("Bienvenido al Gestor de Archivos")
    
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            listar_contenido()
        elif opcion == '2':
            crear_directorio()
        elif opcion == '3':
            crear_archivo()
        elif opcion == '4':
            escribir_en_archivo()
        elif opcion == '5':
            eliminar_elemento()
        elif opcion == '6':
            mostrar_informacion()
        elif opcion == '7':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 7.")
            
        input("\nPresiona Enter para continuar...")
        
if __name__ == "__main__":
    main()
           