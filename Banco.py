
import random

listadecuentas={}
print ("Banco Monte dei Paschi")
print ("Por favor elija un item del menu:\n\
1-Crear Usuario\n\
2-Modificar Usuario\n\
3-Eliminar Usuario\n\
4-Listar Usuarios\n")

opcion= int(input())

while opcion < 5:
    #print ("Banco Monte dei Paschi")
    #print ("Por favor elija un item del menu:\n\
    #1-Crear Usuario\n\
    #2-Modificar Usuario\n\
    #3-Eliminar Usuario\n\
    #4-Listar Usuarios\n")
    #opcion = int(input())

    if opcion == 1:
        print("Ingrese Nombre:")
        nombre = input()
        print("Ingrese Apellido:")
        nombre+= " " + input()
        texto = "A Continuacion se le asignara una cuenta a {}"
        print (texto.format(nombre))
        textocuenta = "La cuenta asignada a {} es la cuenta numero {}"
        cuenta = random.randint(1000,9999)
        print(textocuenta.format(nombre, str(cuenta)))
        listadecuentas[nombre] = cuenta
        opcion = 0
    
    if opcion == 2:
        print("Seleccione el usuario a modificar:")
        print(listadecuentas.keys())
        nombre = input()
        cuenta = listadecuentas.get(nombre)
        texto = "Va a modificar a {}"
        print(texto.format(nombre))
        print("Ingrese Nombre:")
        nuevonombre = input()
        print("Ingrese Apellido:")
        nuevonombre+= " " + input()
        listadecuentas.pop(nombre)
        listadecuentas[nuevonombre] = cuenta
        for x in listadecuentas:
            print(x)
        opcion = 0
    print ("Por favor elija un item del menu:\n\
 1-Crear Usuario\n\
 2-Modificar Usuario\n\
 3-Eliminar Usuario\n\
 4-Listar Usuarios\n")
    opcion = int(input())