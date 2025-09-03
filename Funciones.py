def buscar_producto_por_id (listaProducto,idBusqueda):
    '''
    Este va a retornar el primer producto cuyo id
    sea el id ingresado
    '''
    for productoSeleccionado in listaProducto:
        if productoSeleccionado.get("identificacion")==idBusqueda:
            return productoSeleccionado
    return None

def eliminar_producto_por_id(listaProducto,idObjetivo):
    for productoSeleccionado in listaProducto:
        if productoSeleccionado.get("identificacion")==idObjetivo:
            listaProducto.remove(productoSeleccionado)
            return True
        else: print(f"No se ha podido encontrar el ID")
    return False