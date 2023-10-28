def mcm_iterativo(a, b):
    """
    Función que calcula el Mínimo Común Múltiplo (MCM) de dos números enteros de manera iterativa.
    """
    max_num = max(a, b)
    
    while True:
        if max_num % a == 0 and max_num % b == 0:
            return max_num
        max_num += 1

def mcm_recursivo(a, b):
    """
    Función que calcula el Mínimo Común Múltiplo (MCM) de dos números enteros de manera recursiva.
    """
    def gcd(x, y):
        if y == 0:
            return x
        return gcd(y, x % y)

    return abs(a * b) // gcd(a, b)

def calcular_mcm(a, b):
    """
    Función principal que calcula el MCM de dos números enteros tanto de manera iterativa como recursiva.
    """
    resultado_iterativo = mcm_iterativo(a, b)
    resultado_recursivo = mcm_recursivo(a, b)
    return resultado_iterativo, resultado_recursivo

# Pedir al usuario los números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Calcular e imprimir el MCM utilizando ambas soluciones
iterativo, recursivo = calcular_mcm(num1, num2)
print(f"MCM Iterativo de {num1} y {num2}: {iterativo}")
print(f"MCM Recursivo de {num1} y {num2}: {recursivo}")
