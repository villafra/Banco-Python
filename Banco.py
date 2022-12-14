import random

def Listar():
    print("Nombre\t\t\tCuenta\t  Saldo")
    for x, y in listadecuentas.items():
        print(x,"\t",y,"\t",listacuentasmontos[y])
    print("")

def crearcuenta():
    return random.randint(5000,9999)

def modifusuario(nombre, nuevonombre):
    cuenta = listadecuentas.get(nombre)
    listadecuentas.pop(nombre)
    listadecuentas[nuevonombre] = cuenta

def eliminarusuario(nombre):
    listadecuentas.pop(nombre)

def Depositar(cuenta, monto):
    monto += listacuentasmontos[cuenta]
    listacuentasmontos.update({cuenta:monto})

def Extraer(cuenta, monto):
    si_no = False
    nuevomonto = listacuentasmontos[cuenta] - monto
    if not monto > listacuentasmontos[cuenta]:
        listacuentasmontos.update({cuenta:nuevomonto})
        si_no = True
    return si_no

def Transferir(origen, destino, monto):
    si_no = False
    if Extraer(origen, monto):
        Depositar(destino, monto)
        si_no = True
    return si_no

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
        listacuentasmontos[cuenta] = 0
        opcion = 0
    
    if opcion == 2:
        print("Seleccione el usuario a modificar:")
        if listadecuentas:
            for x in listadecuentas:
                print(x)
            nombre = input()
            texto = "Va a modificar a {}"
            print(texto.format(nombre))
            print("Ingrese Nombre:")
            nuevonombre = input()
            print("Ingrese Apellido:")
            nuevonombre+= " " + input()
            modifusuario(nuevonombre)
            for x in listadecuentas:
                print(x)
        else:
            print("La Lista de clientes esta vacia\n")
        opcion = 0
    if opcion == 3:
        if listadecuentas:
            print("Seleccione el usuario a eliminar:")
            for x in listadecuentas:
                print(x)
            nombre = input()
            eliminarusuario(nombre)
            texto = "Se ha eliminado a {}\n"
            print(texto.format(nombre))
        else:
            print("La Lista de clientes esta vacia\n")
        opcion = 0
    if opcion == 4:
        if listadecuentas:
            Listar()
        else:
           print("La Lista de clientes esta vacia\n")
        opcion = 0
    if opcion == 5:
        print("Seleccionar cuenta a depositar:")
        if listadecuentas:
            Listar()
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
        Listar()
        opcion = 0
    if opcion == 6:
        print("Seleccionar cuenta para extraccion:")
        if listadecuentas:
             Listar()
             print("")
             cuenta = int(input())
             print("Ingrese el monto deseado a extraer:")
             ingreso = float(input())
             if Extraer(cuenta, ingreso):
                print("Se ha extraido con exito")
             else:
                print("El monto que desea extraer supera el saldo de la cuenta")   
        else:
            print("La Lista de clientes esta vacia\n")
        Listar()
        opcion = 0
    if opcion == 7:
         print("Seleccionar cuenta origen:")
         if listadecuentas:
             Listar()
             print("")
             origen = int(input())
             Listar()
             print("Seleccione la cuenta destino:")
             destino = int(input())
             print("Ingrese el monto deseado a transferir:")
             transferencia = float(input())
             if Transferir(origen, destino, transferencia):
                 print("Se ha transferido con exito")
             else:
                 print("El monto que desea transferir supera el saldo de la cuenta de origen")
         else:
            print("La Lista de clientes esta vacia\n")
         Listar()
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





            