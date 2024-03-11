import os
import time
import logicaDelSistema 

listaProductos = []
listaClientes = []
listaFacturas = []

logicaDelSistema.baseDeDatoDeLaTienda(listaProductos, listaClientes)

while True:
    print("================== Sistema de Facturación ==================")
    print("+------------------------------------------------------------+")
    print("|                                                            |")
    print("|         1. Iniciar sesión como director de la tienda.      |")
    print("|                                                            |")
    print("|         2. Iniciar sesión como tendero.                    |")
    print("|                                                            |")
    print("|                                                            |")
    print("|         0. Salir                                           |")
    print("+------------------------------------------------------------+")
    print("\n ")
    print("\n ")
    opcion = int(input("Digite una opción: "))
    os.system("cls")
    if opcion == 1:
        while True:
            print("+------------------------------------------------------------+")
            print("+                  MENÚ DE ADMINISTRADOR                     +")
            print("+------------------------------------------------------------+")
            print("|                                                            |")
            print("|             1. Agregar productos.                          |")
            print("|                                                            |")
            print("|             2. Eliminar (producto o cliente) existente.    |")
            print("|                                                            |")
            print("|             3. Modificar (producto o cliente) existente.   |")
            print("|                                                            |")
            print("|             4. Agregar stock al inventario.                |")
            print("|                                                            |")
            print("|             5. Mostrar productos inscritos.                |")
            print("|                                                            |")
            print("|             6. Mostrar clientes inscritos.                 |")
            print("|                                                            |")
            print("|             7. Mostrar historial de facturas.              |")
            print("|                                                            |")
            print("|             8. Buscar (factura, cliente o producto).       |")
            print("|                                                            |")
            print("|             9. Mostrar total de ventas.                    |")
            print("|                                                            |")
            print("|                                                            |")
            print("|             0. Salir al inicio.                            |")
            print("+------------------------------------------------------------+")
            print("\n ")
            print("\n ")
            opcionAdmin = int(input("Digite una opción: "))
            os.system("cls")
            if opcionAdmin == 1:
                codigo = int(input("Ingrese el código del producto: "))
                descripcion = input("Ingrese la descripción del producto: ")
                valorUnitario = float(input("Ingrese el valor unitario del producto: "))
                stockDisponible = int(input("Ingrese el stock disponible del producto: "))
                logicaDelSistema.agregarProducto(listaProductos, codigo, descripcion, valorUnitario, stockDisponible)
                print("Regresando al menú de administrador...")
                time.sleep(2)
                os.system("cls")
            elif opcionAdmin == 2:
                print("¿Qué desea eliminar?")
                print("1. Cliente")
                print("2. Producto")
                print("3. Salir al menú de administrador")
                opcionEliminar = int(input("Digite su opción: "))
                os.system("cls")
                if opcionEliminar == 1:
                    logicaDelSistema.mostrarClientes(listaClientes)
                    logicaDelSistema.eliminarClientesExistente(listaClientes)
                    print("Regresando al menú de administrador...")
                    time.sleep(1.5)
                    os.system("cls")
                elif opcionEliminar == 2:
                    logicaDelSistema.eliminarProductoExistente(listaProductos)
                    print("Regresando al menú de administrador...")
                    time.sleep(1.5)
                    os.system("cls")
                elif opcionEliminar == 3:
                    print("Regresando al menú de administrador...")
                    time.sleep(1.5)
                    os.system("cls")
                else:
                    print("Esta opción es inválida, por favor intente nuevamente.")
                    time.sleep(1.5)
                    1
                    os.system("cls")
            elif opcionAdmin == 3:
                logicaDelSistema.modificarDatos(listaClientes, listaProductos)
            elif opcionAdmin == 4:
                logicaDelSistema.agregarStock(listaProductos)
                input("Presione Enter para continuar...")
                os.system("cls")
            elif opcionAdmin == 5:
                logicaDelSistema.mostrarProductos(listaProductos)
                input("Presione Enter para continuar...")
                os.system("cls")
            elif opcionAdmin == 6:
                logicaDelSistema.mostrarClientes(listaClientes)
                input("Presione Enter para continuar...")
                os.system("cls")
            elif opcionAdmin == 7:
                logicaDelSistema.mostrarFacturas(listaFacturas)
                input("Presione Enter para continuar...")
                os.system("cls")
            elif opcionAdmin == 8:
                logicaDelSistema.buscarFacturaClienteProducto(listaFacturas, listaClientes, listaProductos)
                os.system("cls")
            elif opcionAdmin == 9:
                print("|-------------------------------------|")
                print("|           Total de ventas.          |")
                print("|-------------------------------------|")
                print(f"El total de ventas hasta el momento son de: ${logicaDelSistema.totalDeVentas(listaFacturas)}")
                print("--------------------------------------------------------------------")
                input("Presione Enter para continuar...")
                os.system("cls")
            elif opcionAdmin == 0:
                print("Regresando al inicio...")
                time.sleep(1.5)
                os.system("cls")
                break
            else:
                print("Esta opción es inválida, por favor intente nuevamente.")
                time.sleep(1.5)
                os.system("cls")
    elif opcion == 2:
        while True:
            print("+------------------------------------------------------------+")
            print("+                     MENÚ DE VENDEDOR                       +")
            print("+------------------------------------------------------------+")
            print("|                                                            |")
            print("|             1. Realizar ventas de productos.               |")
            print("|                                                            |")
            print("|             2. Mostrar productos inscritos.                |")
            print("|                                                            |")
            print("|             3. Mostrar última factura ingresada.           |")
            print("|                                                            |")
            print("|                                                            |")
            print("|             0. Salir al inicio.                            |")
            print("+------------------------------------------------------------+")
            print("\n ")
            print("\n ")
            opcionVendedor = int(input("Digite una opción: "))
            os.system("cls")
            if opcionVendedor == 1:
                logicaDelSistema.realizarCompra(listaProductos, listaFacturas, listaClientes)
                input("Presione Enter para continuar...")
                os.system("cls")
            elif opcionVendedor == 2:
                logicaDelSistema.mostrarProductos(listaProductos)
                input("Presione Enter para continuar...")
                os.system("cls")
            elif opcionVendedor == 3:
                logicaDelSistema.mostrarUltimaFactura(listaFacturas)
                input("Presione Enter para continuar...")
                os.system("cls")
            elif opcionVendedor == 0:
                print("Regresando al inicio...")
                time.sleep(1.5)
                os.system("cls")
                break
            else:
                print("Esta opción es inválida, por favor intente nuevamente.")
                time.sleep(1.5)
                os.system("cls")
    elif opcion == 0:
        print("¡Gracias por usar nuestro programa!")
        print("¡Hasta luego!")
        time.sleep(1.5)
        break
    else:
        print("Opción inválida. Intente nuevamente.")
        time.sleep(1.5)
        os.system("cls")


