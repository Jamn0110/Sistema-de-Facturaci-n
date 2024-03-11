from datetime import date
from os import system
from time import sleep
from productos import Producto
from clientes import Cliente
from detallesDeFactura import DetalleFactura
from facturas import Factura



def comprobarExistenciaDeProducto(listaProductos, codigo):
    iterador = listaProductos
    for ite in iterador:
        if ite.codigo == codigo:
            return False
    return True

def agregarProducto(listaProductos, codigo, descripcion, valorUnitario, stockDisponible):
    nuevoProducto = Producto(codigo, descripcion, valorUnitario, stockDisponible)
    if listaProductos is None:
        listaProductos = [nuevoProducto]
    else:
        if comprobarExistenciaDeProducto(listaProductos, codigo):
            posicion_insercion = 0
            for producto in listaProductos:
                if descripcion > producto.descripcion:
                    posicion_insercion += 1
                else:
                    break
            listaProductos.insert(posicion_insercion, nuevoProducto)
        else:
            print("No se puede agregar un producto con un código que ya está registrado en otro producto.")
    print("Producto agregado correctamente. :)")
    return listaProductos

def mostrarProductos(listaProductos):
    print("+----------------------------------------------+")
    print("+             PRODUCTOS DISPONIBLES            +")
    print("+----------------------------------------------+")
    if listaProductos is None:
        print("No hay productos disponibles.")
        return
    for producto in listaProductos:
        print("Código:", producto.codigo, "-", producto.descripcion)
        print("Valor Unitario: $", producto.valorUnitario)
        print("Stock Disponible:", producto.stockDisponible)
        print("----------------------------------------------")

def encontrarProducto(listaProductos, codigoProducto):
    temp = listaProductos
    for tem in temp:
        if tem.codigo == codigoProducto:
            return tem
    return None

def agregarStock(listaProductos):
    mostrarProductos(listaProductos)
    print("\n")
    codigoProducto = int(input("Digite el código del producto al que desea agregarle más stock: "))
    for producto in listaProductos:
        if producto.codigo == codigoProducto:
            print("+----------------------------------------------+")
            print("+             Agregar stock.                   +")
            print("+----------------------------------------------+")
            print("El stock actual del producto", producto.descripcion, "es de", producto.stockDisponible)
            nuevoStockDelProducto = int(input("¿Qué cantidad de stock desea agregar? "))
            producto.stockDisponible += nuevoStockDelProducto
            print("El nuevo stock del producto fue agregado de manera exitosa.")
            print("El producto", producto.descripcion, "ahora tiene un stock de", producto.stockDisponible)
            return  # Salir de la función después de actualizar el stock
    print("No se encontró el producto con el código ingresado.")


def eliminarProductoExistente(listaProductos):
    if listaProductos is None:
        print("No hay productos para eliminar.")
        return

    mostrarProductos(listaProductos)
    print("|--------------------------------------------------|")
    print("|                Eliminar producto.                |")
    print("|--------------------------------------------------|\n")
    
    codigoProducto = int(input("Digite el código del producto que desea eliminar: "))

    encontrado = False
    for i, producto in enumerate(listaProductos):
        if producto.codigo == codigoProducto:
            del listaProductos[i]
            encontrado = True
            print("El producto ha sido eliminado satisfactoriamente.")
            break
    
    if not encontrado:
        print("No se encontró el producto con el código especificado.")


def obtenerFechaActual():
    fechaActual = date.today()
    return fechaActual.strftime("%d/%m/%Y")

def mostrarClientes(listaCliente):
    print("+----------------------------------------------+")
    print("+                  CLIENTES                    +")
    print("+----------------------------------------------+")
    if listaCliente is None:
        print("No hay clientes para mostrar.")
        return
    for cliente in listaCliente:
        print("Cédula:", cliente.cedula)
        print("Nombre:", cliente.nombre)
        print("Dirección:", cliente.direccion)
        print("Teléfono:", cliente.telefono)
        print("Email:", cliente.email)
        print("----------------------------------------------")

def eliminarClientesExistente(listaClientes):
    if listaClientes is None:
        print("No hay clientes para eliminar.")
        return

    print("|--------------------------------------------------|")
    print("|                Eliminar cliente.                 |")
    print("|--------------------------------------------------|\n")
    
    numeroCedula = input("Digite el número de cédula del cliente que desea eliminar: ")
    
    clienteAnterior = None
    encontrado = False
    
    for i, cliente in enumerate(listaClientes):
        if cliente.cedula == numeroCedula:
            encontrado = True
            if clienteAnterior is None:
                # Si el cliente a eliminar es el primero de la lista
                listaClientes.pop(i)
            else:
                # Si el cliente a eliminar no es el primero de la lista
                listaClientes.pop(i)
            print("El cliente ha sido eliminado satisfactoriamente.")
            break
    
    if not encontrado:
        print("No se encontró el cliente con el número de cédula especificado.")


def modificarCliente(listaClientes):
    actual = listaClientes
    opcionModificar = None
    nuevaCedula = None
    nuevoNombre = None
    nuevoDireccion = None
    nuevoTelefono = None
    nuevoEmail = None

    if actual == None:
        print("No hay clientes para modificar.")
        return

    print("|--------------------------------------------------|")
    print("|                Modificar cliente.                |")
    print("|--------------------------------------------------|\n")
    print("Lista de clientes:")
    
    for cliente in listaClientes:
        print("Cédula:", cliente.cedula, "Nombre:", cliente.nombre)

    print("\n")

    noDocumento = input("Digite el número de cédula del cliente que desea modificar: ")
    
    for cliente in listaClientes:
        if cliente.cedula == noDocumento:
            print("¿Qué desea modificar del cliente?")
            print("1. Cédula.")
            print("2. Nombre.")
            print("3. Dirección.")
            print("4. Teléfono.")
            print("5. Email.")
            print("0. Salir.")
            opcionModificar = int(input("Digite la opción: "))

            switcher = {
                1: "Ingrese el nuevo número de cédula: ",
                2: "Ingrese el nuevo nombre del cliente: ",
                3: "Ingrese la nueva dirección del cliente: ",
                4: "Ingrese el nuevo número de teléfono del cliente: ",
                5: "Ingrese el nuevo email del cliente: "
            }

            if opcionModificar in switcher:
                print(switcher[opcionModificar])

                if opcionModificar == 1:
                    nuevaCedula = input()
                    cliente.cedula = nuevaCedula
                    print("El número de cédula ha sido actualizado correctamente.")
                elif opcionModificar == 2:
                    nuevoNombre = input()
                    cliente.nombre = nuevoNombre
                    print("El nombre del cliente ha sido actualizado correctamente.")
                elif opcionModificar == 3:
                    nuevoDireccion = input()
                    cliente.direccion = nuevoDireccion
                    print("La dirección del cliente ha sido actualizada correctamente.")
                elif opcionModificar == 4:
                    nuevoTelefono = input()
                    cliente.telefono = nuevoTelefono
                    print("El número telefónico del cliente ha sido actualizado correctamente.")
                elif opcionModificar == 5:
                    nuevoEmail = input()
                    cliente.email = nuevoEmail
                    print("El nuevo email del cliente ha sido actualizado correctamente.")
            elif opcionModificar == 0:
                return
            else:
                print("Opción inválida, ingrese una opción correcta.")
            break
    else:
        print("No se encontró al cliente con la cédula especificada.")


def modificarProductos(listaProductos):
    numeroCodigo = None
    opcionModificar = None
    nuevoCodigo = None
    nuevaDescripcion = None
    nuevoValorUnitario = None

    if listaProductos == None:
        print("No hay productos para modificar.")
        return

    print("|---------------------------------------------------|")
    print("|                Modificar producto.                |")
    print("|---------------------------------------------------|\n")

    print("Lista de productos:")
    for producto in listaProductos:
        print("Código del producto:", producto.codigo, "-", producto.descripcion)

    print("\n")
    print("\n")

    numeroCodigo = int(input("Digite el código del producto que desea modificar: "))

    for producto in listaProductos:
        if producto.codigo == numeroCodigo:
            print("¿Qué desea modificar del producto?")
            print("1. Código del producto.")
            print("2. Descripción del producto.")
            print("3. Valor unitario del producto.")
            print("0. Salir al menú de administrador.")
            opcionModificar = int(input("Digite la opción: "))

            switcher = {
                1: "Ingrese el nuevo código del producto: ",
                2: "Ingrese la nueva descripción del producto: ",
                3: "Ingrese el nuevo valor unitario del producto: "
            }

            if opcionModificar in switcher:
                print(switcher[opcionModificar])
                if opcionModificar == 1:
                    nuevoCodigo = int(input())
                    if comprobarExistenciaDeProducto(listaProductos, nuevoCodigo):
                        producto.codigo = nuevoCodigo
                        print("El código del producto fue actualizado correctamente.")
                    else:
                        print("No puedes renombrar el producto con un código que está en uso.")
                        return
                elif opcionModificar == 2:
                    nuevaDescripcion = input()
                    producto.descripcion = nuevaDescripcion
                    print("La nueva descripción del producto fue actualizada correctamente.")
                elif opcionModificar == 3:
                    nuevoValorUnitario = float(input())
                    producto.valorUnitario = nuevoValorUnitario
                    print("El nuevo valor unitario del producto fue actualizado correctamente.")
            elif opcionModificar == 0:
                print("Regresando al menú...")
                return
            else:
                print("Opción inválida, ingrese una opción correcta.")
            break
    else:
        print("No se encontró el producto que digitó.")

def modificarDatos(listaClientes, listaProductos):
    opcion = None
    print("|----------------------------------------------------|")
    print("|          Modificar (clientes o productos).         |")
    print("|----------------------------------------------------|\n")
    print("¿Qué desea modificar?")
    print("1. Cliente.")
    print("2. Producto.")
    print("3. Salir.")
    opcion = int(input("Digite la opción: "))


    if opcion == 1:
        modificarCliente(listaClientes)
    elif opcion == 2:
        modificarProductos(listaProductos)
    elif opcion == 3:
        return
    else:
        print("Opción inválida, ingrese la opción correcta.")


def encontrarCliente(listaClientes, cedula):
    for cliente in listaClientes:
        if cliente.cedula == cedula:
            return cliente
    return None

def agregarCliente(listaClientes, cedula, nombre, direccion, telefono, email):
    nuevoCliente = Cliente(cedula, nombre, direccion, telefono, email)
    if listaClientes == None:
        listaClientes = [nuevoCliente] 
    else:
        listaClientes.append(nuevoCliente) 


def realizarCompra(listaProductos, listaFacturas, listaClientes):
    stockDisponible = False
    nombre = ""
    cedula = ""
    direccion = ""
    telefono = ""
    email = ""
    numero = 0
    fecha = obtenerFechaActual()
    cliente = ""
    detalles = ""
    total = 0


    for producto in listaProductos:
        if producto.stockDisponible > 0:
            stockDisponible = True
            break
    
    if not stockDisponible:
        print("No se puede realizar una compra. No hay productos disponibles en stock.")
        return
    
    print("Lista de productos:")
    for producto in listaProductos:
        print("Código:", producto.codigo, "-", producto.descripcion)
        print("Stock Disponible:", producto.stockDisponible)
        print("Valor Unitario: $", producto.valorUnitario)
        print("----------------------------------------------")
    
    print("Seleccione los productos que desea comprar (Digite 0 si no desea agregar más productos):")
    
    nuevaFactura = Factura(numero, fecha, cliente, detalles, total)
    nuevaFactura.detalles = []
    
    while True:
        codigoProducto = int(input("Código del producto: "))
        
        if codigoProducto == 0:
            break
        
        productoEncontrado = None
        
        for producto in listaProductos:
            if producto.codigo == codigoProducto:
                productoEncontrado = producto
                break
        
        if productoEncontrado is None:
            print("El producto con código", codigoProducto, "no existe.")
            continue
        
        print("______________________________________________________")
        print("Descripción:", productoEncontrado.descripcion)
        print("Valor Unitario: $", productoEncontrado.valorUnitario)
        print("Stock:", productoEncontrado.stockDisponible)
        print("______________________________________________________")
        
        cantidadProducto = int(input("Cantidad que desea comprar: "))
        
        if cantidadProducto > productoEncontrado.stockDisponible:
            print("No hay suficiente stock del producto", productoEncontrado.codigo, ".")
            continue
        elif cantidadProducto == 0:
            print("Debe elegir una cantidad mayor de 0 pero menor o igual", productoEncontrado.stockDisponible, ".")
            continue
        

        nuevoDetalle = DetalleFactura(productoEncontrado, cantidadProducto, productoEncontrado.valorUnitario, (cantidadProducto * productoEncontrado.valorUnitario))
        
        
        nuevaFactura.detalles.append(nuevoDetalle)
        
        productoEncontrado.stockDisponible -= cantidadProducto
        
        print("Producto agregado correctamente.")
    
    if not nuevaFactura.detalles:
        print("No se agregó ningún producto para comprar.")
        return
    
    # Limpiar la pantalla
    system("CLS")
    
    cedula = input("Digite el número de cédula del cliente: ")
    
    # Limpiar la pantalla
    system("CLS")
    
    clienteRegistrado = encontrarCliente(listaClientes, cedula)
    
    if clienteRegistrado is None:
        print("|-------------------------------------|")
        print("|           Agregar cliente.          |")
        print("|-------------------------------------|\n")
        print("Cédula del cliente:", cedula)
        nombre = input("Nombre: ")
        direccion = input("Dirección: ")
        telefono = input("Teléfono: ")
        email = input("Email: ")
        
        nuevoCliente = Cliente(cedula, nombre, direccion, telefono, email)
        listaClientes.append(nuevoCliente)
        
        print("El cliente fue agregado correctamente.")
        nuevaFactura.cliente = nuevoCliente
    else:
        nuevaFactura.cliente = clienteRegistrado
    
    totalFactura = sum(detalle.subtotal for detalle in nuevaFactura.detalles)
    nuevaFactura.total = totalFactura
    nuevaFactura.numero = len(listaFacturas) + 1
    nuevaFactura.fecha = date.today()
    
    listaFacturas.append(nuevaFactura)
    
    print("Compra realizada correctamente.")
    sleep(1)
    
    system("CLS")
    
    print("------------------------------------------------------")
    print("|               Factura N°", nuevaFactura.numero, "                         |")
    print("------------------------------------------------------")
    print("Fecha de venta:", nuevaFactura.fecha)
    print("______________________________________________________")
    print("Datos del Cliente:")
    print("  Cédula:", nuevaFactura.cliente.cedula, "-", nuevaFactura.cliente.nombre)
    print("  Dirección:", nuevaFactura.cliente.direccion)
    print("  Teléfono:", nuevaFactura.cliente.telefono)
    print("  Email:", nuevaFactura.cliente.email)
    print("______________________________________________________")
    print("Detalle de la factura:")
    
    for detalle in nuevaFactura.detalles:
        print("------------------------------------------------------")
        print("  Código:", detalle.producto.codigo, "-", detalle.producto.descripcion)
        print("  Cantidad:", detalle.cantidad)
        print("  Precio unitario: $", detalle.precio)
        print("  Subtotal: $", detalle.subtotal)
    
    print("______________________________________________________")
    print("Total: $", nuevaFactura.total)
    print("______________________________________________________\n\n")

def mostrarFacturas(listaFacturas):
    if listaFacturas == None:
        print("No existen facturas registradas.")
        return
    
    for facturaActual in listaFacturas:
        print("______________________________________________________")
        print("|                  Factura N°", facturaActual.numero, "                 |")
        print("______________________________________________________")
        print("Fecha de venta:", facturaActual.fecha)
        print("______________________________________________________")
        print("Datos del Cliente:")
        print("  Cédula:", facturaActual.cliente.cedula, "-", facturaActual.cliente.nombre)
        print("  Dirección:", facturaActual.cliente.direccion)
        print("  Teléfono:", facturaActual.cliente.telefono)
        print("  Email:", facturaActual.cliente.email)
        print("------------------------------------------------------")
        print("Detalle de la factura:")
        for detalleFactura in facturaActual.detalles:
            print("------------------------------------------------------")
            print("  Detalles del Producto:", detalleFactura.producto.descripcion)
            print("  Código:", detalleFactura.producto.codigo, "-", detalleFactura.producto.descripcion)
            print("    Cantidad:", detalleFactura.cantidad)
            print("    Precio unitario: $", detalleFactura.precio)
            print("    Subtotal: $", detalleFactura.subtotal)
        print("------------------------------------------------------")
        print("Total: $", facturaActual.total, "\n\n")


def mostrarUltimaFactura(listaFacturas):
    if listaFacturas == None or len(listaFacturas) == 0:
        print("No se ha generado ninguna factura hasta el momento.")
        return
    
    ultimaFactura = listaFacturas[-1]  # Acceder al último elemento de la lista de facturas
    
    print("______________________________________________________")
    print("Factura número:", ultimaFactura.numero)
    print("Fecha de venta:", ultimaFactura.fecha)
    print("------------------------------------------------------")
    print("Datos del Cliente:")
    print("  Cédula:", ultimaFactura.cliente.cedula, "-", ultimaFactura.cliente.nombre)
    print("  Dirección:", ultimaFactura.cliente.direccion)
    print("  Teléfono:", ultimaFactura.cliente.telefono)
    print("  Email:", ultimaFactura.cliente.email)
    print("------------------------------------------------------")
    print("Detalle de la factura:")
    print("------------------------------------------------------")
    for detalleFactura in ultimaFactura.detalles:
        print("  Detalles del Producto:", detalleFactura.producto.descripcion)
        print("  Código:", detalleFactura.producto.codigo, "-", detalleFactura.producto.descripcion)
        print("    Precio unitario: $", detalleFactura.precio)
        print("    Subtotal: $", detalleFactura.subtotal)
        print("------------------------------------------------------")
    print("Total: $", ultimaFactura.total, "\n\n")


def encontrarFactura(listaFacturas, codigoFactura):
    for facturaActual in listaFacturas:
        if facturaActual.numero == codigoFactura:
            return facturaActual
    return None


def buscarCliente(listaClientes, listaFacturas):
    cedulaCliente = input("Digite el número de cédula del cliente que desea buscar: ")
    clienteEncontrado = encontrarCliente(listaClientes, cedulaCliente)
    if clienteEncontrado is None:
        print("No se encontró el cliente.")
        return

    print("|-------------------------------------|")
    print("|           Información del cliente.  |")
    print("|-------------------------------------|")
    print("Cédula:", clienteEncontrado.cedula)
    print("Nombre:", clienteEncontrado.nombre)
    print("Dirección:", clienteEncontrado.direccion)
    print("Teléfono:", clienteEncontrado.telefono)
    print("Email:", clienteEncontrado.email)

    sumaTodasLasVentasClientes = 0
    for facturaActual in listaFacturas:
        if facturaActual.cliente.cedula == cedulaCliente:
            print("|-------------------------------------|")
            print("|     Detalles de la factura.         |")
            print("|-------------------------------------|")
            detalleFactura = facturaActual.detalles
            while detalleFactura is not None:
                print("Producto:", detalleFactura.producto.descripcion)
                print("Código:", detalleFactura.producto.codigo)
                print("Cantidad:", detalleFactura.cantidad)
                print("Precio unitario: $", detalleFactura.precio)
                print("Subtotal: $", detalleFactura.subtotal)
                print("---------------------------------------")
                detalleFactura = detalleFactura.siguiente
            sumaTodasLasVentasClientes += facturaActual.total
    
    print("Total de lo que ha comprado este cliente es de: $", sumaTodasLasVentasClientes)
    print("----------------------------------------------")

def buscarFactura(listaFacturas):
    codigoFactura = int(input("Digite el código de la factura que desea buscar: "))
    facturaEncontrada = encontrarFactura(listaFacturas, codigoFactura)
    if facturaEncontrada is None:
        print("No se encontró la factura que digitó.")
        return

    print("|-------------------------------------|")
    print("|      Detalles de la factura.       |")
    print("|-------------------------------------|")
    print("Factura número:", facturaEncontrada.numero)
    print("Fecha de venta:", facturaEncontrada.fecha)
    print("------------------------------------------------------")
    print("Datos del Cliente:")
    print("  Cédula:", facturaEncontrada.cliente.cedula, "-", facturaEncontrada.cliente.nombre)
    print("  Dirección:", facturaEncontrada.cliente.direccion)
    print("  Teléfono:", facturaEncontrada.cliente.telefono)
    print("  Email:", facturaEncontrada.cliente.email)
    print("------------------------------------------------------")
    print("Detalle de la factura:")
    print("------------------------------------------------------")
    detalleFactura = facturaEncontrada.detalles
    print("  Detalles del Producto:", detalleFactura.producto.descripcion)
    print("  Código:", detalleFactura.producto.codigo, "-", detalleFactura.producto.descripcion)
    print("    Precio unitario: $", detalleFactura.precio)
    print("    Subtotal: $", detalleFactura.subtotal)
    print("------------------------------------------------------")
    print("Total: $", facturaEncontrada.total, "\n\n")


def buscarProducto(listaProductos):
    codigoProducto = 0
    print("|-------------------------------------|")
    print("|           Buscar producto.          |")
    print("|-------------------------------------|\n")
    codigoProducto = int(input("Digite el código del producto que desea buscar: "))
    if encontrarProducto(listaProductos, codigoProducto) == None:
        print("No se encontró el producto que digitó.")
        return
    else:
        print("Detalles del producto con código", codigoProducto, ".")
        productoActual = encontrarProducto(listaProductos, codigoProducto)
        print("Código:", productoActual.codigo, "-", productoActual.descripcion)
        print("Valor Unitario: $", productoActual.valorUnitario)
        print("Stock Disponible:", productoActual.stockDisponible)
        print("----------------------------------------------")

def buscarFacturaClienteProducto(listaFacturas, listaClientes, listaProductos):
    opcionBuscar = 0
    print("¿Qué desea buscar?")
    print("1. factura \n2. cliente \n3. producto \n4. salir")
    opcionBuscar = int(input("Digite su opción: "))
    if opcionBuscar == 1:
        buscarFactura(listaFacturas)
        system("PAUSE")
    elif opcionBuscar == 2:
        buscarCliente(listaClientes, listaFacturas)
        system("PAUSE")
    elif opcionBuscar == 3:
        buscarProducto(listaProductos)
        system("PAUSE")
    elif opcionBuscar == 4:
        print("Regresando al menú anterior...")
        sleep(1500)
        system("CLS")
    else:
        print("Opción inválida, ingrese una opción nuevamente.")
        sleep(1500)
        system("CLS")

def totalDeVentas(listaFacturas):
    sumarTodasLasVentas = 0
    for facturaActual in listaFacturas:
        sumarTodasLasVentas += facturaActual.total
    return sumarTodasLasVentas


def baseDeDatoDeLaTienda(listaProductos, listaClientes):
    agregarProducto(listaProductos, 1, "Carne Waygu x kilo", 200000, 18)
    agregarProducto(listaProductos, 2, "Salchicha ranchera (paquete x 6)", 12000, 25)
    agregarProducto(listaProductos, 3, "Pack pan tostado x 6", 6500, 10)
    system("CLS")
    agregarCliente(listaClientes, "1082240703", "Juan Mosquera", "Manzana D casa 12 Villa del mar ", "3218123101", "jamn011020@gmail.com")
    agregarCliente(listaClientes, "1082859769", "Sofia Cotes", "Manzana 209 casa 209 Boulevard de la 19", "3014075880", "sofiacvilla@gmail.com")


