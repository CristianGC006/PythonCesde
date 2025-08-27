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
        producto={}
        print("A Continuacion ingresa un Producto a nuestra APP")
        producto["identificacion"]=input("Digita el ID del producto a registra: ")
        producto["nombre"]=input("Ingesa el nombre del Producto: ")
        producto["descripcion"]=input("Cuentanos acerca del Producto: ")
        producto["fotografia"]=input("Ingresa la URL de la fotografia del Producto: ")
        producto["precio_unitario"]=float(input("digita el precio unitario del producto: "))
        producto["cantidad_en_bodega"]=int(input("Ingresa la cantidad de los productos en bodega: ")) 
        print("Producto Agregado satisfactoriamente")
        almacen_producto.append(producto) 
    elif Opcion_del_menu==2:
        for productoSeleccionado in almacen_producto:
            print(f"Producto: {productoSeleccionado==producto["nombre"]}-\n precio:{productoSeleccionado==producto["precio_unitario"]}")
    elif Opcion_del_menu==3:
        pass
    elif Opcion_del_menu==4:
        pass
    elif Opcion_del_menu==5:
        pass
    else:
        print("Opcion Incorrecta, ingresa una opcion valida")