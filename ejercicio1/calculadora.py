def calculadora():
    # Solicitamos al usuario que ingrese el primer número como cadena y luego lo convertimos a flotante
    num1 = float(input("Ingrese el primer número: "))  # Corrección: Utilizar input en lugar de float("Ingrese el primer número: ")
    
    # Solicitamos al usuario que ingrese el segundo número como cadena y luego lo convertimos a flotante
    num2 = float(input("Ingrese el segundo número: "))  # Corrección: Utilizar input en lugar de float("Ingrese el segundo número: ")
    
    # Solicitamos al usuario que ingrese la operación a realizar
    operacion = input("Ingrese la operación (+, -, *, /): ")
    
    # Verificamos la operación ingresada y realizamos el cálculo correspondiente
    if operacion == '+':
        resultado = num1 + num2  # Corrección: Utilizar num1 en lugar de num
    elif operacion == '-':
        resultado = num1 - num2
    elif operacion == '*':
        resultado = num1 * num2
    elif operacion == '/':
        resultado = num1 / num2
    else:
        resultado = "Operación no válida"
    
    # Mostramos el resultado
    print("Resultado:", resultado)  # Corrección: Agregar coma para concatenar el resultado

calculadora()  # Corrección: Llamar correctamente a la función calculadora
