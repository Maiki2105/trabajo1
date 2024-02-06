import random  # Corrección: Corregir el nombre del módulo a importar (random en lugar de radom)

def simular_lanzamiento_dados(cantidad_dados, caras_por_dado):  # Corrección: Agregar dos puntos (:) al final de la línea de definición de función
    resultados = [random.randint(1, caras_por_dado) for _ in range(cantidad_dados)]
    return resultados  # Corrección: Corregir la palabra 'retunr' a 'return'

cantidad_dados = int(input("Ingrese la cantidad de dados a lanzar: "))
caras_por_dado = int(input("Ingrese la cantidad de caras por dado: "))
lanzamientos = simular_lanzamiento_dados(cantidad_dados, caras_por_dado)  # Corrección: Pasar los parámetros adecuadamente
print(f"Resultados del lanzamiento: {lanzamientos}")
