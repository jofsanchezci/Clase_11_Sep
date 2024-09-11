# Abrir el archivo en modo escritura ('w' para sobrescribir, 'a' para agregar)
with open('archivo.txt', 'w', encoding='utf-8') as archivo:
    # Escribir contenido en el archivo
    archivo.write("Este es el contenido que estoy escribiendo en el archivo.\n")
    archivo.write("Puedes agregar tantas líneas como quieras.\n")
    for i in range(1,10):
        archivo.write( str(i), "\n")

# El archivo se cierra automáticamente al salir del bloque 'with'
print("El contenido ha sido escrito en el archivo.")
