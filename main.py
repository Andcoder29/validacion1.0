from utilidades.funciones import (validarEnteros,asignarDescuento,darFactura,pesoCOl,validarValor)

# ------------------ ENTRADA -------------------------
print('¡¡Bienvenido Tiendas - Realiza tu compra!!')
nom_product = input('nombre de producto: ')
while True:
    valorStr_producto = (input('Ingrese el precio del producto: '))
    valorStr_esValido = validarValor(valorStr_producto)
    if valorStr_esValido:
        valor_producto = float(valorStr_producto)
        while True:
            cantStr_product = input('cantidad: ')
            cantStr_esValido = validarEnteros(cantStr_product)
            if cantStr_esValido:
                cant_producto = int(cantStr_product)
                while True:
                    aplica_descuentoStr = input('Aplica descuento? --- Si(S) / No(N) ---: ')
                    aplica_descuentoStr_esValido, porcentaje = asignarDescuento(aplica_descuentoStr)
                    if aplica_descuentoStr_esValido:
                        # proceso
                        valorSinDescuento = (valor_producto * cant_producto)
                        valor_a_descontar = (valorSinDescuento * porcentaje)/100
                        valor_total = (valorSinDescuento - valor_a_descontar)
                        darFactura(nom_product,valor_producto,cant_producto,porcentaje,valorSinDescuento,valor_a_descontar,valor_total)
                        break
                break
        break

    
    