import random

def crearcuenta():
    return random.randint(5000,9999)

def Depositar(cuenta, monto):
    listacuentasmontos.update({cuenta:monto})

listadecuentas={}
listacuentasmontos={}
print ("Banco Monte Dei Paschi")
print ("Por favor elija un item del menu:\n\
1-Crear Usuario\n\
2-Modificar Usuario\n\
3-Eliminar Usuario\n\
4-Listar Usuarios\n\
5-Depositar en Cuenta\n\
6-Retirar Dinero de Cuenta\n\
7-Transferir Dinero\n\
8-Salir\n")

opcion= int(input())

while opcion < 8:

    if opcion == 1:
        print("Ingrese Nombre:")
        nombre = input()
        print("Ingrese Apellido:")
        nombre+= " " + input()
        texto = "A Continuacion se le asignara una cuenta a {}"
        print (texto.format(nombre))
        textocuenta = "La cuenta asignada a {} es la cuenta numero {}\n"
        cuenta = crearcuenta()
        print(textocuenta.format(nombre, str(cuenta)))
        listadecuentas[nombre] = cuenta
        opcion = 0
    
    if opcion == 2:
        print("Seleccione el usuario a modificar:")
        for x in listadecuentas:
            print(x)
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
    if opcion == 3:
        print("Seleccione el usuario a eliminar:")
        for x in listadecuentas:
            print(x)
        nombre = input()
        listadecuentas.pop(nombre)
        texto = "Se ha eliminado a {}\n"
        print(texto.format(nombre))
        opcion = 0
    if opcion == 4:
        if listadecuentas:
            for x in listadecuentas:
                print(x)
        else:
           print("La Lista de clientes esta vacia\n")
        opcion = 0
    if opcion == 5:
        print("Seleccionar cuenta a depositar:")
        if listadecuentas:
            for x, y in listadecuentas.items():
                print(x,y)
            print("")
            cuenta = int(input())
            print("Ingrese el monto a depositar:")
            ingreso = float(input())
            if not Depositar(cuenta, ingreso):
                print("Se ha depositado con exito")
            else:
                print("No se ha depositado")   
        else:
            print("La Lista de clientes esta vacia\n")
        for x,y in listacuentasmontos.items():
            print(x,y)
        opcion = 0
        if opcion == 8:
            quit()
    print ("Por favor elija un item del menu:\n\
1-Crear Usuario\n\
2-Modificar Usuario\n\
3-Eliminar Usuario\n\
4-Listar Usuarios\n\
5-Depositar en Cuenta\n\
6-Retirar Dinero de Cuenta\n\
7-Transferir Dinero\n\
8-Salir\n")
    opcion = int(input())





            