def es_primo(numero):  # Corrección: Agregar dos puntos (:) al final de la línea de definición de función
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):  # Corrección: Agregar dos puntos (:) al final de la línea del bucle for
        if numero % i == 0:
            return False
    return True  # Corrección: Corregir la palabra 'retrun' a 'return' y corregir la palabra 'retunr' a 'return'

limite = int(input("Ingrese el límite superior para encontrar números primos: "))
primos = [num for num in range(2, limite + 1) if es_primo(num)]  # Corrección: Pasar 'num' como argumento a la función 'es_primo'
print("Números primos:", primos)
