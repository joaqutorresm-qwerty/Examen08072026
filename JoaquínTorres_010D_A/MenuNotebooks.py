productos = {
'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {
'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}

#################################################

def menu():
    print("*** MENU PRINCIPAL ***")
    print("1. Stock marca.")
    print("2. Búsqueda por precio.")
    print("3. Actualizar precio.")
    print("4. Salir.")

def opcion_menu():
    while True:
        try:
            opcion = int(input("Ingrese la opción que desee: "))
            return opcion
        except ValueError:
            print("Escoja una opción valida")

#################################################

def stock_marca(marca):
    marca = input("Ingrese la marca para buscar el stock: ")
    total = 0
    for marca, datos in productos.items():
        if datos[0] == marca.casefold():
            unidades = stock[marca][1]
            total += unidades
    print(f"Total de unidades para la marca: {total}")

#################################################

def busqueda_precio(p_min, p_max, marca):
    if busqueda_precio_menu():
        resultados = []
        for modelo, datos in stock.items():
            precio = datos[0]
            stock = datos[1]
            if p_min <= precio <= p_max and stock:
                modelo = modelo[stock][1]
                resultados.append(f"{marca} -- {modelo} -- {datos}")
                resultados.sort()

                if not resultados:
                    print("No hay modelos en ese rango de precio.")
                else:
                    for modelo in resultados:
                        print(modelo)

def busqueda_precio_menu():
    while True:
        try:
            p_min = int(input("Ingrese el precio mínimo: "))
            p_max = int(input("Ingrese el precio máximo: "))
        except ValueError:
            print("Debe ingresar valores enteros")
            continue
        
        if p_min < 0 or p_max < 0 or p_min > p_max:
            print("Los valores deben ser mayores que cero o el mínimo debe ser menor que el máximo")
            return
        break

def buscar_modelo(modelo):
    for modelo in stock:
        if modelo.casefold() == modelo.casefold():
            return True
    return False

#################################################

def actualizar_precio(modelo, nuevo_precio):
    if buscar_modelo(modelo):
        for modelo in stock:
            if modelo.casefold() == modelo.casefold():
                stock[modelo][0] = nuevo_precio
                return True
    return False

def actualizar_precio_menu():
    while True:
        modelo = input("Ingrese el modelo a cambiar el precio: ")

        while True:
            try:
                nuevo_precio = int(input("Ingrese el nuevo precio: "))
                if nuevo_precio < 0:
                    print("El precio debe ser mayor que 0")
                    continue
                break
            except ValueError:
                print("Debe ingresar un valor valido")

        if actualizar_precio(modelo, nuevo_precio):
            print("Precio actualizado.")
        else:
            print("El modelo no existe.")
        
        repetir = input("Desea repetir el proceso? s/n: ").casefold()
        if repetir == "no":
            break
        elif repetir == "si":
            return actualizar_precio_menu()
        else:
            print("Ingrese un dato valido")

#################################################

while True:
    menu()

    opcion = opcion_menu()

    if opcion == 1:
        stock_marca(productos)
    elif opcion == 2:
        busqueda_precio_menu()
    elif opcion == 3:
        actualizar_precio_menu()
    elif opcion == 4:
        print("Programa finalizado...")
        break
    else:
        print("Escoja una opción valida")