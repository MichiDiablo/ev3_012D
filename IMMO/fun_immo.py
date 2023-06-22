import os
import time
import random as r
import msvcrt as m

#Listas.
cliente=[]
clientes=[]

#Función limpia pantalla.
def limpiar_pantalla(seg):
    time.sleep(seg)
    os.system("cls")

#Menu principal.
def menu():
    print("--------IMMO Ltda.--------")
    print("Bienvenid@ a nuestra inmoviliaria,")
    print("por favor seleccione una opción.")
    print("1. Registrarse.")
    print("2. Buscar por rut.")
    print("3. Reporte según renta.")
    print("4. Salir.")
    opcion=int(input("Ingrese opción: "))
    return opcion

#Menu proyectos.
def proyecto():
    print("Proyectos disponibles.")
    print("1. Vive Santiago\n2. Vive La Florida")
    print("3. Vive Ñuñoa")

#Función registro cliente.
def registro():
    id_cl=input("Ingrese su rut sin digito verificador: ")
    while (len(id_cl)!=8):
        print("Ingrese un rut valido.")
        id_cl=(input("Ingrese su rut sin digito verificador: "))
    nom_cl=input("Ingrese nombre: ")
    while (len(nom_cl)<1):
        print("Debe ingresar un nombre.")
        nom_cl=input("Ingrese nombre: ")
    renta_cl=int(input("Ingrese renta mensual: "))
    while renta_cl<1:
        print("Ingrese una renta valida.")
        renta_cl=input("Ingrese renta mensual: ")
    proyecto()
    proyecto_cl=int(input("¿En que proyecto desea inscribirse?: "))
    if proyecto_cl==1:
        pro='VS'
    elif proyecto_cl==2:
        pro='VF'
    elif proyecto_cl==3:
        pro='VN'
    else:
        print("Opción invalida, por favor ingrese una opción valida.")
    cliente=[id_cl,nom_cl,renta_cl,pro]
    clientes.append(cliente)
    print("Registro completo")
    limpiar_pantalla(3)

#Función buscar cliente por rut.
def buscar(id):
    p=1
    for lista in clientes:
        if lista[0]==id:
            print(f"Rut cliente: {lista[0]}")
            print(f"Nombre cliente: {lista[1]}")
            print(f"Renta mensual: {lista[2]}")
            if lista[3]=='VS':
                print("Proyecto: Vive Santiago")
            elif lista[3]=='VF':
                print("Proyecto: Vive La Florida")
            elif lista[3]=='VN':
                print("Proyecto: Vive Ñuñoa")
            p=0
            print("Presione una tecla para continuar.")
            m.getch()
            limpiar_pantalla(4)
    if p==1:
        print("No se encontro cliente con ese rut registrado.")
        limpiar_pantalla(3)

#Función crear reporte por proyecto.
def lista_renta(pro):
    cont=0
    x=900000
    for lista in clientes:
        if lista[2]>x and lista[3]==pro:
            cont+=1
            n=r.randint(2500,3700)
            print(f"Sr/a {lista[1]}")
            print(f"Rut: {lista[0]}")
            print(f"Con renta de: $ {lista[2]}")
            if lista[3]=='VS':
                print("En el proyecto Vive Santiago")
            elif lista[3]=='VF':
                print("En el proyecto Vive La Florida")
            elif lista[3]=='VN':
                print("En el proyecto Vive Ñuñoa")
            print(f"Puede acceder a un Dpto. de {n} UF")
            print(f"Se generaron {cont} reportes")           
    print("Presione una tecla para continuar.")
    m.getch()
    limpiar_pantalla(1.5)

#Función salir.
def salir():
    while True:
        print("Gracias por visitar IMMO Ltda.\nVuelva pronto.")
        break