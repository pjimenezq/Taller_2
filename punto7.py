def tiene_vocales(cadena):
    """Función que devuelve True si una cadena tiene dos o más vocales."""
    vocales = "aeiouAEIOU"  # Definimos una cadena con todas las vocales
    contador = 0  # Inicializamos un contador de vocales a cero
    for letra in cadena:  # Recorremos cada letra de la cadena
        if letra in vocales:  # Si la letra es una vocal
            contador += 1  # Incrementamos el contador de vocales
            if contador >= 2:  # Si ya hemos encontrado dos vocales
                return True  # Devolvemos True
    return False  # Si no encontramos dos vocales, devolvemos False

# Definimos una lista de cadenas
lista = ["j73a8r", "Dyvid", "plnta", "Python", ]  

encontrado = False  # Inicializamos una variable que indica si hemos encontrado la cadena buscada

for cadena in lista:  # Recorremos cada cadena de la lista
    if tiene_vocales(cadena):  # Si la cadena tiene dos o más vocales
        print("La cadena que cumple con la condición es: ", cadena)  # Mostramos la cadena por pantalla
        encontrado = True  # Indicamos que hemos encontrado la cadena buscada
        break  # Salimos del ciclo

if not encontrado:  # Si no hemos encontrado la cadena buscada
    print("No existe")  # Mostramos 'No existe' por pantalla
    