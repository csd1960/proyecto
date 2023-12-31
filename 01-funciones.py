def agregar_producto(codigo,foto,titulo,descripcion,ambientes,habitaciones,baños,telefono):
    if consultar_producto(codigo):
        return False
    nuevo_producto={
        'codigo':codigo,
        'foto':foto,
        'titulo':titulo,
        'descripcion':descripcion,
        'ambientes':ambientes,
        'habitaciones':habitaciones,
        'baños':baños,
        'telefono':telefono
    }
    productos.append(nuevo_producto)
    return True

def consultar_producto(codigo):
    for producto in productos:
        if producto['codigo'] == codigo:
            return producto
    return False

def modificar_producto(codigo, nueva_foto, nuevo_titulo, nueva_descripcion, nuevo_ambientes, nueva_habitaciones, nuevo_baños, nuevo_telefono):
    for producto in productos:
        if producto['codigo'] == codigo:
            producto['foto'] = nueva_foto,
            producto['titulo']= nuevo_titulo,
            producto['descripcion']= nueva_descripcion,
            producto['ambientes']=nuevo_ambientes,
            producto['habitaciones']=nueva_habitaciones,
            producto['baños']=nuevo_baños,
            producto['telefono']=nuevo_telefono
        return True
    return False

def listar_productos():
    print('-' * 50)
    for producto in productos:
        print(f"Código.......:{producto['codigo']}")
        print(f"Foto.........:{producto['foto']}")
        print(f"Título.......:{producto['titulo']}")
        print(f"Descripción..:{producto['descripcion']}")
        print(f"Ambientes....:{producto['ambientes']}")
        print(f"Habitaciones.:{producto['habitaciones']}")
        print(f"Baños........:{producto['baños']}")
        print(f"Teléfono.....:{producto['telefono']}")
        print('-' * 50)

def eliminar_producto(codigo):
    for producto in productos:
        if producto['codigo']== codigo:
            productos.remove(producto)
        return True
    return False


   

productos = []

    