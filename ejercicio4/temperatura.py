def celsius_a_fahrenheit(celsius):  # Corrección: Agregar dos puntos (:) al final de la línea de definición de función
    return (celsius * 9/5) + 32  # Corrección: Agregar el operador '+' para calcular la suma

# Corrección: Solicitar al usuario que ingrese la temperatura en Celsius y convertirlo a flotante
temperatura_celsius = float(input("Ingrese la temperatura en Celsius: "))

# Llamar a la función celsius_a_fahrenheit y asignar el resultado a la variable temperatura_fahrenheit
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)

# Corrección: Agregar faltante de comilla (') y corregir la cadena f
print(f"{temperatura_celsius}°C es igual a {temperatura_fahrenheit}°F")
