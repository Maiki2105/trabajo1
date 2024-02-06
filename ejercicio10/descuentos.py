def calcular_precio_con_descuento(precio_base, porcentaje_descuento):  # Corrección: Agregar dos puntos (:) al final de la línea de definición de función
    descuento = precio_base * (porcentaje_descuento / 100)
    precio_final = precio_base - descuento
    return precio_final  # Corrección: Corregir la palabra 'retunr' a 'return'

precio_base = float(input("Ingrese el precio base del producto: "))  # Corrección: Utilizar input() en lugar de float()
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))
precio_final = calcular_precio_con_descuento(precio_base, porcentaje_descuento)
print(f"El precio final con {porcentaje_descuento}% de descuento es: {precio_final}")
