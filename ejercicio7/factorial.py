def factorial(n):  # Corrección: Agregar dos puntos (:) al final de la línea de definición de función
    if n == 0 or n == 1:  # Corrección: Utilizar '==' en lugar de '=' para comparar valores
        return 1  # Corrección: Corregir la palabra 'retunr' a 'return'

    # Corrección: Corregir la palabra 'retunr' a 'return'
    return n * factorial(n - 1)  # Corrección: Utilizar el operador '*' para multiplicar

numero = int(input("Ingrese un número para calcular su factorial: "))
print(f"El factorial de {numero} es {factorial(numero)}")  # Corrección: Pasar 'numero' como argumento a la función 'factorial'
