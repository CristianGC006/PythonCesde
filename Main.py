from Funciones import buscar_producto_por_id,eliminar_producto_por_id


#Ejercicio de la tienda
Opcion_del_menu=150
almacen_producto=[]

print("---Bodega Online------>")
print("***********************")
while Opcion_del_menu != 0:
    print("1.Registrar un Producto a la APP")
    print("2.Mostrar productos en Bodega")
    print("3.Valorar bodega")
    print("4.Buscar un Producto")
    print("5.Eliminar un Producto")
    print("Digita 0 Para salir")
    Opcion_del_menu=int(input("Digita Una Opcion: "))
    #Zona de condiciones
    if Opcion_del_menu==0:
        print("Saliendo de la App...")
        break
    elif Opcion_del_menu==1:
        #Debo crear un diccionario desde 0
        #para almacenar la info de un producto
        productos={}
        print("A Continuacion ingresa un Producto a nuestra APP")
        productos["identificacion"]=int(input("Digita el ID del producto a registra: "))
        productos["nombre"]=input("Ingesa el nombre del Producto: ")
        productos["descripcion"]=input("Cuentanos acerca del Producto: ")
        productos["fotografia"]=input("Ingresa la URL de la fotografia del Producto: ")
        productos["precio_unitario"]=float(input("digita el precio unitario del producto: "))
        productos["cantidad_en_bodega"]=int(input("Ingresa la cantidad de los productos en bodega: ")) 
        print("Producto Agregado satisfactoriamente")
        almacen_producto.append(productos) 
    elif Opcion_del_menu==2:
        for productoSeleccionado in almacen_producto:
            print(productoSeleccionado)
            
    elif Opcion_del_menu==3:
        pass
    elif Opcion_del_menu==4:
        print("Buscando un producto por ID")
        id_buscado=int(input("Digita el id del producto que quieres Buscar: "))
        producto_encontrado=eliminar_producto_por_id(productos,id_buscado)
        print(producto_encontrado)
        #Si el producto encontrado es NONE, devolver un mensaje de que el producto no es encontrado

    elif Opcion_del_menu==5:
       print("Elimina un producto: ")
       id_buscado=int(input("Ingresa el ID del producto a eliminar: "))
       if eliminar_producto_por_id(productos,id_buscado):
        print(f"producto{productos.get("nombre")} eliminado")
       else: print("No pudimos encontrar tu producto")
    else:
        print("Opcion Incorrecta, ingresa una opcion valida")