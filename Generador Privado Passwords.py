#Importar librerias
import random
import string


function = input("""
1. Generar una contraseña
2. Ver las contraseñas generadas
3. Eliminar una contraseña
4. Mostrar Creditos
5. Instrucciones
6. Salir
""")

print(function)
#Pedir que seleccione una opcion
opcion = int(input("Seleccione una opcion: "))
#Si la opcion es 1
if opcion == 1:
    #Generar una contraseña
    print("Generando contraseña")
    #Generar una contraseña de 18 caracteres alfanumericos.
    password = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(18))
    print(password)
    #Preguntar al usuario si quiere guardar la contraseña en un archivo
    guardar = input("¿Desea guardar la contraseña en un archivo? (s/n): ")
    #Si la respuesta es s
    if guardar == "s":
        #Tomar la contraseña y solicitar al usuario un codigo identificador para la contraseña y guardarlo en un archivo llamado password.txt sin borrar los datos anteriores y agregar un salto de linea.
        codigo = input("Ingrese un codigo identificador para la contraseña: ")
        archivo = open("password.txt", "a")
        archivo.write(codigo + " " + password + "\n")
        archivo.close()
        print("Contraseña guardada!")
    #Si la respuesta es n
    elif guardar == "n":
        #No guardar la contraseña
        print("No se guardo la contraseña")
    #Si la respuesta no es s ni n
    else:
        #No guardar la contraseña
        print("No se guardo la contraseña")

#Si la opcion es 2
elif opcion == 2:
    #Mostrar las contraseñas generadas.
    print("Mostrando las contraseñas generadas")
    #Mostrar las contraseñas guardadas en el archivo password.txt
    with open("password.txt", "r") as f:
        print(f.read())

#Si la opcion es 3
elif opcion == 3:
    #Eliminar una contraseña apartir del codigo identificador
    print("Eliminando una contraseña")
    #Preguntar al usuario el codigo identificador de la contraseña a eliminar
    codigo = input("Ingrese el codigo identificador de la contraseña a eliminar: ")
    #Abrir el archivo password.txt en modo lectura
    archivo = open("password.txt", "r")
    #Leer el archivo
    lineas = archivo.readlines()
    #Cerrar el archivo
    archivo.close()
    #Abrir el archivo password.txt en modo escritura
    archivo = open("password.txt", "w")
    #Recorrer las lineas del archivo
    for linea in lineas:
        #Si la linea no contiene el codigo identificador
        if codigo not in linea:
            #Escribir la linea en el archivo
            archivo.write(linea)
    #Cerrar el archivo
    archivo.close()
    print("Contraseña eliminada")

#Si la opcion es 4
elif opcion == 4:
    #Generar animacion de creditos
    #Crear animacion con texto
    for i in range(10):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        print("\033[38;2;{};{};{}mCreate By José Ignacio <3\033[0m".format(r, g, b))


#Si la opcion es 5
elif opcion == 5:
    print("1.- Usar este generador de contraseñas con un editor de codigo como Vscode, no está testeado en otro.\n2.- Al iniciar el programa apretar un enter para evitar un error de doble entrada.\n3.- El archivo con las contraseñas se genera donde se encuentre el codigo.")

#Si la opcion es 6
elif opcion == 6:
    #Salir
    print("Saliendo")
#Si la opcion no es 1, 2, 3, 4, 5 o 6
else:
    #Mostrar un mensaje de error
    print("Error")