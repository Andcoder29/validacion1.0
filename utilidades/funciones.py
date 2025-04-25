#declaracion de funciones.

# muestra un float como moneda colombiana
def pesoCOl(valor):
    return f"$ {valor:,.2f}"

# validacion del valor
def validarValor(valor):
    if not valor.isdigit():
        print("valor invalido: solo se aceptan numeros sin puntos.")
        return False
    return True        

# validacion de numeros enteros
def validarEnteros(valor):
    if not valor.isdigit():
        print("valor invalido: solo se aceptan numeros enteros.")
        return False
    return True 

# asignacion del descuento dependiendo de repuesta
def asignarDescuento(descuento):
    if descuento == "S" or descuento == "s":
        procentaje_descuentoStr = input("Ingrese porcentaje de 1 a 100 y sin %: ")
        if procentaje_descuentoStr.isdigit():
            porcentaje = int(procentaje_descuentoStr)
            if porcentaje >= 1 and porcentaje <= 100:
                return True, porcentaje
            else:
                print("El porcentaje debe estar entre 1 y 100.")
                return False
        else:
            print("valor invalido: solo se aceptan numeros")
            return False
    elif descuento == "N" or descuento == "n":
        return True, 0
    else:
        print("Respuesta inválida. Escriba S o N.")
        return False

# imprimir factura
def darFactura(nom_product,valor_producto,cant_product,porcentaje,valorSinDescuento,valor_a_descontar,valor_total):
    print(' ')
    print('-----FACTURA DE COMPRA-----')
    print(f'Nombre de producto: {nom_product}')
    print(f'valor unitario :....................{pesoCOl(valor_producto)}')
    print(f'cantidad comprada:...................{cant_product}')
    print(f'descuento aplicado:..................{porcentaje}%')
    print(f'valor sin descuento:................{pesoCOl(valorSinDescuento)}')
    print(f'valor descontado:...................{pesoCOl(valor_a_descontar)}')
    print('======================================')
    print(f'valor Total :.....................{pesoCOl(valor_total)}')
    print('======================================')


            