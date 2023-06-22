from fun_immo import *

while True:
    try: #Bucle menu principal.
        opcion=menu()
        if opcion==1: #Opción registrar cliente.
            registro()
        elif opcion==2: #Opción buscar clienye por rut.
            while True:
                id=(input("Ingrese rut cliente sin digito verificador: "))
                if (len(id)==8):
                    buscar(id)
                    break
                else:
                    print("Rut no valido")
        elif opcion==3: #Opción generar reporte por proyecto.
            while True:
                proyecto()
                pro=int(input("¿Qué reporte desea generar?"))
                if pro==1:
                    pro='VS'
                    break
                elif pro==2:
                    pro='VF'
                    break
                elif pro==3:
                    pro='VN'
                    break
                else:
                    print("Ingrese opción de proyecto valida")
            lista_renta(pro)
        elif opcion==4: #Opción salir.
            salir()
            break
    except:
        print("Ingrese valor correcto.")