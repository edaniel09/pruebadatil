# Disenar e implementar una vending machine
# implementar el proceso de venta
from vending_machine import VendingMachine
from producto import Producto

def seleccionarProductos(maquina):
    #funcion utilizada por el Customer para seleccionar productos
    return

def insertarSaldo(maquina):
    #funcion utilizada por el Customer para aumentar su saldo
    return

def consultarEstadisticas(maquina):
    #funcion utilizada por el Admin para consultar productos mas vendidos
    return

def productoAgotado(maquina):
    #funcion para alertar al Operador de que un producto se ha agotado
    return

# recibe un objeto maquina y una lista de productos a cargar

def cargaProductos(maquina, productos):
    for item in productos:
        maquina.productos.append(item)

# permite visualizar los nombres de los Productos disponibles en la maquina
def verProductosDisponibles(maquina):
    print("[ITEMS DISPONIBLES en " + maquina.tipo + "]")
    print("[Codigo]     [Items]      [Cantidad]")
    if(len(maquina.productos) > 0):
        for item in maquina.productos:
            print(str(item.identificador) +"         "+item.nombre + "       " + str(item.cantidad))
    else:
        print("Esta maquina no tiene productos disponibles")


def venta(maquina, seleccion, saldoDisponible):
    for sel in seleccion:
        for producto in maquina.productos:
            if(producto.identificador == sel):
                productoencontrado = True
                if((producto.cantidad > 0) and (saldoDisponible - producto.precio > 0.0)):
                    nuevo_saldo = saldoDisponible - producto.precio
                    producto.cantidad -= 1
                elif(not(saldoDisponible - producto.precio > 0.0)):
                    print("No tiene fondos suficientes para realizar la compra")
                    return
                elif(not(producto.cantidad > 0)):
                    print("La maquina no tiene "+producto.nombre+" disponible en stock")
                    return
    print("Su cambio es $" + str(nuevo_saldo))

def main():
    seleccion = [3, 1, 4]

    producto1 = Producto(1, "Botella de Agua", 5, 1.00)
    producto2 = Producto(2, "Coca Cola", 10, 1.50)
    producto3 = Producto(3, "Papas Fritas", 7, 0.50)
    producto4 = Producto(4, "Chifles", 11, 1.25)
    producto5 = Producto(5, "Granola", 15, 2.50)

    productos = [producto1, producto2, producto3, producto4, producto5]

    vm1 = VendingMachine("Maquina Generica")
    cargaProductos(vm1, productos)
    verProductosDisponibles(vm1)

    venta(vm1, seleccion, 20.00)

    verProductosDisponibles(vm1)


if __name__ == "__main__":
    main()
