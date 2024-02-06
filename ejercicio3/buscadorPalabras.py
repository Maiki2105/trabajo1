def contar_palabra(texto, palabra):  # Corrección: Agregar dos puntos (:) al final de la línea de definición de función
    return texto.lower().split().count(palabra.lower())

texto = "Este es un ejemplo de texto. Este texto tiene palabras repetidas."
palabra_buscada = "texto"

# Corrección: Agregar un faltante de comilla (') y corregir el nombre de la variable 'palabra_buscada'
print(f"La palabra '{palabra_buscada}' aparece {contar_palabra(texto, palabra_buscada)} veces.")
