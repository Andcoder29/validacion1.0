
### 🛒 Proyecto: Tienda - Sistema de Compra con Descuento

Este es un programa simple en Python que simula la compra de un producto en una tienda. Pide datos como nombre del producto, precio, cantidad y si aplica o no un descuento. Al final, muestra una factura detallada.

---

## 🔧 Funcionalidades

- Solicita al usuario:
  - Nombre del producto
  - Precio del producto
  - Cantidad de productos
  - Si aplica descuento
- Calcula:
  - El total sin descuento
  - El valor del descuento (si aplica)
  - El total a pagar
- Imprime una **factura** con todos los detalles.

---

## 📦 Estructura del Código

El código se divide en 2 partes principales:

### 1. **Entrada y proceso**

Esta parte recibe los datos del usuario y hace validaciones:

```python
nom_product = input('nombre de producto: ')
# Se valida el precio
# Se valida la cantidad
# Se pregunta si hay descuento
# Se calculan los totales
# Se imprime la factura
```

### 2. **Funciones auxiliares**

Estas funciones están en `utilidades/funciones.py` (o podrían estarlo). Son:

#### `validarValor(valor)`
Valida que el precio ingresado solo tenga números enteros (sin puntos ni letras).

#### `validarEnteros(valor)`
Verifica que la cantidad también sea un número entero válido.

#### `asignarDescuento(descuento)`
Pregunta si se aplicará un descuento. Si sí, pide el porcentaje (entre 1 y 100).

#### `pesoCOl(valor)`
Convierte un número flotante a formato de pesos colombianos (`$ 10,000.00`).

#### `darFactura(...)`
Muestra por consola una factura con toda la información de la compra.

---

## 💡 Ejemplo de uso

```
¡¡Bienvenido Tiendas - Realiza tu compra!!
nombre de producto: Chocolate
Ingrese el precio del producto: 5000
cantidad: 2
Aplica descuento? --- Si(S) / No(N) ---: S
Ingrese porcentaje de 1 a 100 y sin %: 10

-----FACTURA DE COMPRA-----
Nombre de producto: Chocolate
valor unitario :....................$ 5,000.00
cantidad comprada:...................2
descuento aplicado:..................10%
valor sin descuento:................$ 10,000.00
valor descontado:...................$ 1,000.00
======================================
valor Total :.....................$ 9,000.00
======================================
```

---

