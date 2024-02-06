import random  # Corrección: Importar correctamente el módulo random
import string

# Corregir nombre de la función y agregar el parámetro de longitud con valor predeterminado
def generar_contraseña(longitud=8):  # Corrección: Agregar el parámetro 'longitud' y corregir la palabra 'contraseña'
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña  # Corrección: Corregir la palabra 'return'

print(generar_contraseña())  # Corrección: Corregir la función a llamar, de generar_contrasena a generar_contraseña
