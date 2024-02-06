def es_palindromo(texto):  # Corrección: Agregar dos puntos (:) al final de la línea de definición de función
    texto = ''.join(caracter.lower() for caracter in texto if caracter.isalnum())
    return texto == texto[::-1]

palabra_frase = input("Ingrese una palabra o frase: ")
if es_palindromo(palabra_frase):  # Corrección: Pasar 'palabra_frase' como argumento a la función 'es_palindromo'
    print(f"{palabra_frase} es un palíndromo.")
else:
    print(f"{palabra_frase} no es un palíndromo.")
