# Taller_2

**Nombre del grupo:**

Agrocode industry

**Integrantes:**

* Paula Jiménez Quiñones
* Mario Alejandro Martinez
* David Rodriguez Rueda

**Logo:**

![logo](https://github.com/pjimenezq/Taller_1/assets/141860508/136373ec-f9a4-4b51-a52a-1b1e893e1859)

## Primer punto
**Instrucción**

Desarrollar un programa que ingrese un número entero n y separe todos los digitos que componen el número.

**Explicación de la solución**
* Primero lo que se hizo fue una función para los dígitos separados en función del número 'n' que se ingresó. Haremos un caso de función recursiva, si la respuesta es 0 entonces el dígito es 0, aunque no habría problema si no aparece nada en la lista. En la función recursiva se creará un ciclo while que funcionará siempre que 'n' sea mayor a 0.
* Este ciclo crea una nueva variable que va a ser 'd', para hallar 'd' nosotros hacemos 'n' módulo 10. Este resultado nos dará el último dígito del número ingresado. Despues de tener este digito lo ingresamos a una lista creada en la función main. Para actualizar 'n' y que no se tenga en cuenta el último digito que ya se separó entonces hacemos 'n' división entera 10; esto hará que no se tenga en cuenta el último digito que ya separamos. Si el resultado de esta división es mayor que 0 se repite el ciclo.
* En la función main cremos la variable 'n', que será un entero ingresado por el usuario, creamos la lista en la que ingresamos los dígitos. Llamamos a la función de digitosSeparados e imprimimos el resultado

**Código**
```python
# Primero creamos una función que nos dará los digitos separados del número 'n' ingresado por el usuario. Es decir, digitosSeparados en función de n
def digitosSeparados(n: int) -> int: #Aplicaremos la función recursiva
    #La función base es si n es igual a 0, el dígito será 0, aunque si no aparecía nada en la lista no habría problema ya que 0 no representa un valor
    if n == 0:
        digitosListaRev.append(n)
        return digitosListaRev
    # La función recursiva es la siguiente:
    else:
        #Para esto creamos un ciclo, el cual funcionará siempre que 'n' sea mayor que 0
        while n > 0:
            #Vamoa a separar los digitos de la siguiente manera: Creamos la variable 'd' que será el dígito que en ese momento se esté trabajando. El resultado de 'd' será 'n' módulo 10.
            #El residuo de la división anterior será el digito que se trabaje.
            d = n % 10
            #Ese resultado lo añadimos a la lista creado en la función main
            digitosListaRev.append(d)
            #Tenemos que actualizar 'n' en diviendo el valor de 'n' en 10, esto hará que el dígito que ya se ingresó a la lista no se tome en cuenta en el siguiente ciclo
            n = n // 10
        # Creamos una nueva variable que será la lista creada aplicando slicing para que la lista quede ordenada.
        digitosLista = digitosListaRev[::-1]
        # Se nos retorna la variable de la lista ordenada
        return digitosLista

if __name__ == "__main__":
    #En la función main creamos la variable 'n' que será un entero ingresado por el usuario
    n : int = int(input("Ingrese el número entero que usted desee: "))
    #Esta es la lista en la cual ingresamos los digitos.
    digitosListaRev = []
    #Creamos la variable digitos donde llamamos a la función que hicimos al inicio
    digitos = digitosSeparados(n)
    #Imprimimos
    print("Los digitos del número deseado por el usuario son los sigueintes", digitos)
```
## Segundo punto
**Instrucción**

Desarrollar un programa que ingrese un número flotante n y separe su parte entera de la parte decimal, y luego entregue los dígitos tanto de la parte entera como de la decimal.

**Explicación de la solución**



**Código**
```
```
## Tercer punto
**Instrucción**

Desarrollar un programa que permita ingresar dos números enteros y determinar si se tratan de números espejos, definiendo números espejos como dos números a y b tales que a se lee de izquierda a derecha igual que se lee b de derecha a izquierda, y viceversa.

**Explicación de la solución**



**Código**
```
```
## Cuarto punto
**Instrucción**

Diseñar una función que permita calcular una aproximación de la función coseno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Taylor. nota: use math para traer la función coseno y mostrar la diferencia entre el valor real y la aproximación. Calcule con cuántos términos de la serie (i.e: cuáles valores de n), se tienen errores del 10%, 1%, 0.1% y 0.001%.

**Explicación de la solución**
* Primero lo que se hizo fue importar la librería math y de la librería math importar la función coseno y el factorial
* Después se creó la aproximación de la función coseno, en la que se iban a introducir los valores de la base y los valores del exponente. Creamos la variable 'funcCos' la cual igualamos a 0, y a esta variable le sumamos la ecuación de la función, la cual es la que está presentada en el código, segun la serie de terminos de Taylor.
* Mencionamos la función main; en la cual le pedimos al usuario que ingrese el número de la base, el exponente será igual a 1, llamamos a la 'AproxFuncCos' y usamos la función coseno real.
* Como el exponente es igual a 1, entonces tenemos que crear un ciclo en el que el valor del exponente aumente o disminuya conforme a la necesidad que presenta la base, para ello mientras que la aproximación sea mayor a un margen de error que se determine entonces se le pedirá a 'n' que aumente su valor más 1 hasta que el margen de error se menor al valor determinado.
* Por último imprimimos comparando el valor real de la función coseno con el aproximado y la resta entre el valor real con la aproximación.

**Código**

Para este caso el balance de error tenía que ser menos de 10

```python
#Importamos math y de math traemos la función coseno y al factorial
from math import cos, factorial
#Creamos una función que nos ayude a llegar a la aproximación de la función coseno
def aproxFuncCos (x:float, n:int) -> float:
    funcCos: float = 0
    for i in range(0, n+1):
        funcCos += ((-1)**i)*(x**((2*i))/factorial(2*i)) #Esta es la ecuación de la función coseno para hallarla
    return funcCos

if __name__=="__main__":
    #Le pedimos al usuario que ingrese un valor para la base
    x = float(input("Ingrese un valor para la base 'x': "))
    # El exponente tiene valor de 1, porque conforme a la base irá cambiando el exponente
    n : int = 1
    aprox = aproxFuncCos(x, n) #Llamamos a la aproximación de la función coseno
    real = cos(x) #Llamamos a la función coseno real después de importar la librería math

    #Para que el exponente sea el correcto creamos un while con la siguiente operación, así miramos la aproximación
    while abs((real - aprox)/real*100)>10:
        aprox: float = aproxFuncCos(x, n)
        #Actualizamos cada vez el exponente conforme al resultado que obtenemos para llegar más fácil a la aproximación
        n += 1
        # El while se termina cuando el valor que obtenemos es menor al error posible que establecemos en este caso es 10, pero se irá disminuyendo para comprobar el comportamiento de los exponentes
    print(n, " es el valor del exponente para que funcione la aproximación")
    
    #Restamos el valor real con el exponente
    difAprox = real - aprox

    #Imprimimos
    print("La aproximación de la función seno es", aprox)
    print("La función seno real es", real)
    print("La diferencia de la función real y la aproximación es", difAprox)
```
Cuando el balance de error es menor a 10 los exponentes que toma el ejercicio normalmente toman todos los naturales empezando desde 4, cuando la base es 2 o mayor. Haciendo saltos en el exponente en muy pocas ocasiones, esto saltos eran de dos números. Es decir, en alguna ocasión podía dar saltos de 4 a 6 por ejemplo. Siendo un ejemplo, Se tomó en cuenta cuando la base es de 2 hasta 20.

---

Siguiente caso, el balance de error debe ser menor a 1

```python
#Importamos math y de math traemos la función coseno y al factorial
from math import cos, factorial
#Creamos una función que nos ayude a llegar a la aproximación de la función coseno
def aproxFuncCos (x:float, n:int) -> float:
    funcCos: float = 0
    for i in range(0, n+1):
        funcCos += ((-1)**i)*(x**((2*i))/factorial(2*i)) #Esta es la ecuación de la función coseno para hallarla
    return funcCos

if __name__=="__main__":
    #Le pedimos al usuario que ingrese un valor para la base
    x = float(input("Ingrese un valor para la base 'x': "))
    # El exponente tiene valor de 1, porque conforme a la base irá cambiando el exponente
    n : int = 1
    aprox = aproxFuncCos(x, n) #Llamamos a la aproximación de la función coseno
    real = cos(x) #Llamamos a la función coseno real después de importar la librería math

    #Para que el exponente sea el correcto creamos un while con la siguiente operación, así miramos la aproximación
    while abs((real - aprox)/real*100)>1:
        aprox: float = aproxFuncCos(x, n)
        #Actualizamos cada vez el exponente conforme al resultado que obtenemos para llegar más fácil a la aproximación
        n += 1
        # El while se termina cuando el valor que obtenemos es menor al error posible que establecemos en este caso es 1, pero se irá disminuyendo para comprobar el comportamiento de los exponentes
    print(n, " es el valor del exponente para que funcione la aproximación")
    
    #Restamos el valor real con el exponente
    difAprox = real - aprox

    #Imprimimos
    print("La aproximación de la función seno es", aprox)
    print("La función seno real es", real)
    print("La diferencia de la función real y la aproximación es", difAprox)
```

En este caso podemos apreciar que el comportamiento de los exponentes cambia, ya es más seguido que se salten número naturales. Pasa un caso interesante cuando elegimos que la base sea 11, y cuando elegimos que la base sea 12. Nos damos cuenta que envés de que el exponente siga creciendo, en este caso disminuye, después de esto sigue en crecimiento. Seguramente esto pase por el comportamiento de la función coseno al ser una función periódica en el cual el valor más alto que puede tomar en el eje y es 1. Tener en cuenta que x tomó los valores de 1 a 20 en esta ocasión.

---

Siguiente caso, el balance de error debe ser menor a 0.1

```python
#Importamos math y de math traemos la función coseno y al factorial
from math import cos, factorial
#Creamos una función que nos ayude a llegar a la aproximación de la función coseno
def aproxFuncCos (x:float, n:int) -> float:
    funcCos: float = 0
    for i in range(0, n+1):
        funcCos += ((-1)**i)*(x**((2*i))/factorial(2*i)) #Esta es la ecuación de la función coseno para hallarla
    return funcCos

if __name__=="__main__":
    #Le pedimos al usuario que ingrese un valor para la base
    x = float(input("Ingrese un valor para la base 'x': "))
    # El exponente tiene valor de 1, porque conforme a la base irá cambiando el exponente
    n : int = 1
    aprox = aproxFuncCos(x, n) #Llamamos a la aproximación de la función coseno
    real = cos(x) #Llamamos a la función coseno real después de importar la librería math

    #Para que el exponente sea el correcto creamos un while con la siguiente operación, así miramos la aproximación
    while abs((real - aprox)/real*100)>0.1:
        aprox: float = aproxFuncCos(x, n)
        #Actualizamos cada vez el exponente conforme al resultado que obtenemos para llegar más fácil a la aproximación
        n += 1
        # El while se termina cuando el valor que obtenemos es menor al error posible que establecemos en este caso es 0.1, pero se irá disminuyendo para comprobar el comportamiento de los exponentes
    print(n, " es el valor del exponente para que funcione la aproximación")
    
    #Restamos el valor real con el exponente
    difAprox = real - aprox

    #Imprimimos
    print("La aproximación de la función seno es", aprox)
    print("La función seno real es", real)
    print("La diferencia de la función real y la aproximación es", difAprox)
```

Se empiezan a tomar saltos más amplios en los número naturales que puede tomar los exponentes, sabiendo que es necesario para que se cumpla la condición que se está poniendo. Hay saltos en ocasiones de cuatro números, posiblemente en punto específicos de la función en los cuales se demuestran en la gráfica de la función. Se tomaron en cuenta datos para la base de 1 a 20.

---

Siguiente caso, el balance de error debe ser menor a 0.001

```python
#Importamos math y de math traemos la función coseno y al factorial
from math import cos, factorial
#Creamos una función que nos ayude a llegar a la aproximación de la función coseno
def aproxFuncCos (x:float, n:int) -> float:
    funcCos: float = 0
    for i in range(0, n+1):
        funcCos += ((-1)**i)*(x**((2*i))/factorial(2*i)) #Esta es la ecuación de la función coseno para hallarla
    return funcCos

if __name__=="__main__":
    #Le pedimos al usuario que ingrese un valor para la base
    x = float(input("Ingrese un valor para la base 'x': "))
    # El exponente tiene valor de 1, porque conforme a la base irá cambiando el exponente
    n : int = 1
    aprox = aproxFuncCos(x, n) #Llamamos a la aproximación de la función coseno
    real = cos(x) #Llamamos a la función coseno real después de importar la librería math

    #Para que el exponente sea el correcto creamos un while con la siguiente operación, así miramos la aproximación
    while abs((real - aprox)/real*100)>0.001:
        aprox: float = aproxFuncCos(x, n)
        #Actualizamos cada vez el exponente conforme al resultado que obtenemos para llegar más fácil a la aproximación
        n += 1
        # El while se termina cuando el valor que obtenemos es menor al error posible que establecemos en este caso es 0.001, pero se irá disminuyendo para comprobar el comportamiento de los exponentes
    print(n, " es el valor del exponente para que funcione la aproximación")
    
    #Restamos el valor real con el exponente
    difAprox = real - aprox

    #Imprimimos
    print("La aproximación de la función seno es", aprox)
    print("La función seno real es", real)
    print("La diferencia de la función real y la aproximación es", difAprox)
```

Como se ve en los anteriores casos cada vez la suma de los exponentes crece más porque el margen de error es mucho menor, por lo que la cifra tiene que ser mucho más exacta. Se tomaron los valores para la base desde 1 hasta 20.

## Quinto punto
**Instrucción**

Desarrollar un programa que permita determinar el Minimo Comun Multiplo de dos numeros enteros. Abordar el problema desde una perpectiva tanto iterativa como recursiva

**Explicación de la solución**
El código calcula el Mínimo Común Múltiplo (MCM) de dos números enteros. Utiliza el algoritmo de Euclides para el Máximo Común Divisor (MCD) y la fórmula MCM = (|a * b|) / MCD(a, b). Es un enfoque más corto y eficiente para obtener el MCM.


**Código**
```def mcm_iterativo(a, b):
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

```
## Sexto punto
**Instrucción**

Desarrollar un programa que determine si en una lista existen o no elementos repetidos.

**Explicación de la solución**
el código muestra cómo utilizar una función para verificar si una lista dada contiene elementos repetidos. Utiliza la conversión de la lista a un conjunto para hacer esta verificación y luego informa si la lista contiene o no elementos duplicados.
Función tiene_elementos_repetidos(lista):

Esta función se encarga de comprobar si hay elementos repetidos en una lista dada.
Utiliza la conversión de la lista a un conjunto (set(lista)). Los conjuntos en Python no contienen elementos duplicados, por lo que si el tamaño de la lista es diferente al tamaño del conjunto, implica que hay elementos repetidos.
Devuelve True si hay elementos repetidos, ya que el tamaño de la lista y del conjunto será diferente. En caso contrario, devuelve False.


**Código**
```def tiene_elementos_repetidos(lista):
    """
    Función que verifica si una lista tiene elementos repetidos.
    Devuelve True si hay elementos repetidos, de lo contrario, devuelve False.
    """
    # Utilizamos un conjunto para almacenar elementos únicos y comparar tamaños
    return len(set(lista)) != len(lista)

# Lista de ejemplo
mi_lista = [1, 2, 3, 4, 5, 1]  # Lista con elementos repetidos

# Verificar si la lista tiene elementos repetidos
if tiene_elementos_repetidos(mi_lista):
    print("La lista tiene elementos repetidos.")
else:
```

## Séptimo punto
**Instrucción**

Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o más vocales. Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'.

**Explicación de la solución**
el código proporcionado consta de una función y un bucle que verifica si una lista de cadenas contiene al menos una cadena que posee dos o más vocales. Aquí está una explicación más detallada:

Función tiene_vocales(cadena):

Toma una cadena como entrada y verifica si tiene al menos dos vocales.
Itera a través de cada carácter de la cadena y cuenta cuántas vocales hay.
Si encuentra al menos dos vocales, devuelve True, de lo contrario, devuelve False.
Bucle principal:

Define una lista de cadenas llamada lista.
Recorre cada cadena en la lista.
Llama a la función tiene_vocales(cadena) para verificar si la cadena tiene al menos dos vocales.
Si encuentra una cadena que cumple con esa condición, la imprime y detiene el bucle.
Si ninguna cadena cumple con la condición, imprime 'No existe'.


**Código**
```def tiene_vocales(cadena):
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
lista = ["j73a8r", "David", "planeta", "Python", ]  

encontrado = False  # Inicializamos una variable que indica si hemos encontrado la cadena buscada

for cadena in lista:  # Recorremos cada cadena de la lista
    if tiene_vocales(cadena):  # Si la cadena tiene dos o más vocales
        print("La cadena que cumple con la condición es: ", cadena)  # Mostramos la cadena por pantalla
        encontrado = True  # Indicamos que hemos encontrado la cadena buscada
        break  # Salimos del ciclo

if not encontrado:  # Si no hemos encontrado la cadena buscada
    print("No existe")  # Mostramos 'No existe' por pantalla
```
## Octavo punto
**Instrucción**

Desarrollar un programa que dadas dos listas determine que elementos tiene la primer lista que no tenga la segunda lista.

**Explicación de la solución**

1. Crear función

Para solucionar este punto se crea una función que tiene como argumentos dos listas diferentes. En este caso la función se nombró _diferenciaLista_.
La función compara cada uno de los elementos de la primera lista con los elementos de la segunda lista y cuando son iguales, se elimina ese elemento de la primera lista. Después de que se ejecuta la anterior instrucción, la función retorna la primera lista (ahora que en la primera lista, ya no están los elementos que también tiene la segunda lista).

2. Usar la función

Se define la _función main_, se declaran las dos listas con los elementos que se deseen, se llama la función creada anteriormente (llamada _diferenciaLista_) y se imprime el resultado. Es decir que el programa va a imprimir la lista con los elementos que únicamente tiene la primera lista.


**Código**
```
def diferenciaLista(primeraLista,segundaLista):#Declarando función diferenciaLista, la cual determina los elementos que tiene una lista que no tiene otra lista
    for x in segundaLista:#Para cada elemento en la segunda lista
        for y in primeraLista:#Para cada elemento en la primera lista
            if x==y:#Si el elemento de la segunda lista es igual al elemento de la primera lista
                primeraLista.remove(x)#Eliminar el elemento en común de la primera lista
    return primeraLista#Retornar la primera lista (donde sus elementos son los que la segunda lista no tiene)


if __name__=="__main__":#Función principal
    #Declarando las dos listas y sus elementos
    listaUno=[1, 'Hola', -12.3 ,True]
    listaDos=[11, -12.3, 'Hola', False]
    elementosPrimera=diferenciaLista(listaUno,listaDos)#Llamando la función diferenciaLista
    print("Los elementos que tiene la primer lista que no tiene la segunda lista son "+str(elementosPrimera))#Imprimiendo la lista con los elementos que solo tiene la primera lista

```
## Noveno punto
**Instrucción**

Resolver el punto 7 del taller 1 usando operaciones con vectores.

**Punto 7 del taller 1:** 

Escriba un programa que pida 5 números reales y calcule las siguientes operaciones:

* El promedio
* La mediana
* El promedio multiplicativo (multiplica todos y luego calcula la raíz de la cantidad de operandos)
* Ordenar los números de forma ascendente
* Ordenar los números de forma descendente
* La potencia del mayor número elevado al menor número
* La raíz cúbica del menor número

**Explicación de la solución**
1.	Crear las funciones

* El promedio: Se crea una función que tiene como argumento una lista. En este caso la función se nombró _promedio_. La función toma cada uno de los elementos de la lista y los suma entre sí. Luego, divide la suma entre el tamaño de la lista. Después de que se ejecuta la anterior instrucción, la función retorna el resultado (que es el promedio)
* La mediana: Se crea una función que tiene como argumento una lista. En este caso la función se nombró _mediana_.  En la función se utiliza sort() para ordenar los elementos de la lista. Posteriormente, se halla el elemento que se encuentra en la posición de la mitad de la lista, es decir el elemento con índice 2 de la lista. La función retorna el elemento que se encuentra en la posición del medio.
* El promedio multiplicativo: Se crea una función que tiene como argumento una lista. En este caso la función se nombró _promedioMultiplicativo_. La función toma cada uno de los elementos de la lista y los multiplica entre sí. Luego, eleva la multiplicación total a 1 entre el tamaño de la lista. Después de que se ejecuta la anterior instrucción, la función retorna el resultado (que es el promedio multiplicativo)
* Orden ascendente: Se crea una función que tiene como argumento una lista. En este caso la función se nombró _ordenAscendente_.  En la función se utiliza sort() para ordenar los elementos de la lista de menor a mayor. La función retorna la lista ordenada.
* Orden descendente: Se crea una función que tiene como argumento una lista. En este caso la función se nombró _ordenDescendente_.  En la función se utiliza sort(reverse=True) para ordenar los elementos de la lista de mayor a menor. La función retorna la lista ordenada.
* La potencia del mayor número elevado al menor número: Se crea una función que tiene como argumento una lista. En este caso la función se nombró _potencia_.  En la función se utiliza sort() para ordenar los elementos de la lista de menor a mayor. Posteriormente, se eleva el elemento que se encuentra en la última posición al elemento de la primera posición (el elemento con índice -1 elevado al elemento con índice 0). La función retorna el cálculo de la potencia.
* La raíz cúbica del menor número: Se crea una función que tiene como argumento una lista. En este caso la función se nombró _raiz_.  En la función se utiliza sort() para ordenar los elementos de la lista de menor a mayor. Posteriormente, se eleva el elemento que se encuentra en la primera posición (el elemento con índice cero) a un tercio. La función retorna la raíz cúbica del menor número.

2.	Usar las funciones

Se define la _función main_, se crea una lista vacía y con la función input() y .append() se agregan los cinco números reales ingresados por el usuario a la lista. Posteriormente, se llaman las funciones creadas anteriormente, para aplicarlas en la lista creada y se imprimen los resultados de las operaciones realizadas con los cinco elementos de la lista.



**Código**
```
#El promedio
def promedio(lista)->float:#función para hallar promedio de un arreglo
        suma:int=0#Se declara la variable suma que se inicializa en 0
        for i in lista:#Para cada elemento i de la lista
                suma+=i#...se hace la suma de este elemento a la variable suma
        elPromedio=suma/(len(lista))#Para encontrar el promedio se divide la suma de todos los elementos entre la cantidad de elementos que tiene la lista
        return elPromedio#Se retorna el promedio


#La mediana
def mediana(lista)->float:#Función para hallar la mediana de un arreglo
       lista.sort()#Se ordena la lista de menor a mayor
       laMediana=lista[2]#Dado a que la lista tiene 5 elementos, la mediana es igual al elemento que se encuentra en la posición de la mitad (es decir la posición 2)
       return laMediana#Se retorna la mediana


#El promedio multiplicativo (multiplica todos y luego calcula la raíz de la cantidad de operandos)
def promedioMultiplicativo(lista)->float:#función para hallar promedio multiplicativo de un arreglo
        multiplicacion:int=1#Se declara la variable multiplicaciíon que se inicializa en 1
        for i in lista:#Para cada elemento i de la lista
                multiplicacion*=i#...se hace la multiplicación de este elemento a la variable multiplicación
        elPromedioM=multiplicacion**(1/len(lista))#Para encontrar el promedio multiplicativo se halla la raíz de la cantidad de los elementos de la lista de la multiplicación de todos los elementos
        #Para hacer el cálculo de la raíz se eleva la multiplicación de todos los elementos a uno sobre la cantidad de elementos en la lista
        return elPromedioM#Se retorna el promedio multiplicativo


#Ordenar los números de forma ascendente
def ordenAscendente(lista)->float:#Función para ordenar los elementos de la lista de menor a mayor
       lista.sort()#Con sort(), se ordena la lista ascendentemente
       return lista#Se retorna la lista ya ordenada


#Ordenar los números de forma descendente
def ordenDescendente(lista)->float:#Función para ordenar los elementos de la lista de mayor a menor
       lista.sort(reverse=True)#Con sort(reverse=True), se ordena la lista descendentemente
       return lista#Se retorna la lista ya ordenada


#La potencia del mayor número elevado al menor número
def potencia(lista)->float:#Función para hallar la potencia del mayor número elevado al menor número
       lista.sort()#Con sort(), se ordena la lista de menor a mayor
       mayorElevadoMenor=lista[-1]**lista[0]#Para encontra el mayor número elevado al menor se eleva el elemento de la última posición al elemento de la primera posición en la lista
       return mayorElevadoMenor#Se retorna la potencia del mayor número elevado al menor número


#La raíz cúbica del menor número
def raiz(lista)->float:#función para hallar la raíz cúbica del menor número
       lista.sort()#Con sort(), se ordena la lista de menor a mayor
       raizCubicaMenor=lista[0]**(1/3)#La raíz cúbica del menor número es igual al primer elemento de la lista ordenada elevado a un tercio
       return raizCubicaMenor#Se retorna la raíz cúbica del menor número


if __name__=="__main__":#Función principal
    lista=[]#Se crea una lista vacia
    #Con la función input() se declaran e inicializan las variables a, b, c, d y e que corresponden a los cinco números reales que pide el programa
    a=float(input("Ingrese el primer número real "))
    b=float(input("Ingrese el segundo número real "))
    c=float(input("Ingrese el tercer número real "))
    d=float(input("Ingrese el cuarto número real "))
    e=float(input("Ingrese el quinto número real "))
    #Los cinco números reales ingresados por el ususario son agregados a la lista que estaba vacia
    lista.append(a)
    lista.append(b)
    lista.append(c)
    lista.append(d)
    lista.append(e)

    promedioTotal=promedio(lista)#Se llama la función de promedio
    print("El promedio del arreglo es " +str(promedioTotal))#Se imprime el promedio del arreglo

    medianaFinal=mediana(lista)#Se llama la función de la mediana
    print("La mediana del arreglo es " +str(medianaFinal))#Se imprime la mediana del arreglo

    promedioMultiplicativoTotal=promedioMultiplicativo(lista)#Se llama la función de promedio multiplicativo
    print("El promedio multiplicativo del arreglo es " +str(promedioMultiplicativoTotal))#Se imprime el promedio multiplicativo del arreglo

    listaFinalAscendente=ordenAscendente(lista)#Se llama la función del orden ascendente
    print("Los números ordenados de forma ascendente son " +str(listaFinalAscendente))#Se imprime el arreglo en orden ascendente

    listaFinalDescendente=ordenDescendente(lista)#Se llama la función del orden descendente
    print("Los números ordenados de forma descendente son " +str(listaFinalDescendente))#Se imprime el arreglo en orden descendente

    potenciaFinal=potencia(lista)#Se llama la función de la potencia del mayor número elevado al menor número
    print("La potencia del mayor número elevado al menor número es " +str(potenciaFinal))#Se imprime la potencia

    raizMenor=raiz(lista)#Se llama la función de la raíz cúbica del menor número
    print("La raíz cúbica del menor número es " +str(raizMenor))#Se imprime la raíz cúbica del menor número
```
## Décimo punto
**Instrucción**

Suponga que se tiene una lista A con ciertos números enteros. Desarrolle una función que, independientemente de los números que se encuentran en la lista A, tome aquellos números que son múltiplos de 3 y los guarde en una lista nueva, la cual debe ser retornada por la función. Implemente la perspectiva de un patrón de acumulación y también de comprensión de listas. 

**Explicación de la solución**

Desde la perspectiva de un patrón de acumulación:

1.	Crear función

Para solucionar este punto se crea una función que tiene como argumento una lista. En este caso la función se nombró multiplosTres. En la función se crea una lista vacía (llamada listaNueva). Luego, para cada número de la lista que se ingresa en la función principal, se evalúa si este número se puede dividir entre tres sin dejar residuo (utilizando el módulo). En caso de que se cumpla con esta condición, el número es agregado a la lista nueva. La función retorna la listaNueva, que contiene solamente los múltiplos de tres.

2.	Usar la función

Se define la función main, se declara la lista A con los elementos que se deseen, se llama la función creada anteriormente (llamada multiplosTres) y se imprime el resultado. Es decir que el programa va a imprimir la lista con los elementos que sean múltiplos de tres.

Desde la perspectiva de comprensión de listas:
1.	Crear función

Para solucionar este punto se crea una función que tiene como argumento una lista. En este caso la función se nombró multiplosTresComprension. En la función se crea una lista la cual se compone por los elementos de la lista que se ingresa en la función principal que se puedan dividir entre tres sin dejar residuo. La función retorna la lista que contiene solamente los múltiplos de tres.

2.	Usar la función

Se define la función main, se declara la lista A con los elementos que se deseen, se llama la función creada anteriormente (llamada multiplosTresComprension) y se imprime el resultado. Es decir que el programa va a imprimir la lista con los elementos que sean múltiplos de tres.



**Código**
```
# Perspectiva de un patrón de acumulación

def multiplosTres(lista):#Declarando función multiplosTres
    listaNueva=[]#Creando lista vacia
    for num in lista:#para cada elemento de la lista
        if num%3==0:#si el residuo del elemento dividido entre 3 es igual a 0, el elemento es múltiplo de 3
            listaNueva.append(num)#Se agrega ese elemento a la lista que estaba vacia
    return(listaNueva)#Se retorna la lista con los múltiplos de tres

if __name__=="__main__":#Función principal
    listaA=[33,45,61,22,5,21,18]#Se declara la lista A y sus elementos
    multiplosDeTres=multiplosTres(listaA)#Se llama la función multiplosTres
    print("Los números que son múltiplos de tres son: "+ str(multiplosDeTres))#Se imprimen los elementos que son múltiplos de tres de la lista A



# Comprensión de listas

def multiplosTresComprension(lista):#Declarando función MultiplosTresComprension
    listaFinal=[num for num in lista if num%3==0]#Los elementos de la lista final son aquellos elementos de la lista que si se dividen entre tres el residuo es igual a cero
    return(listaFinal)#Se retorna la lista final con los múltiplos de tres


if __name__=="__main__":#Función principal
    listaA=[7,23,35,33,67,99,15]#Se declara la lista A y sus elementos
    multiplosDeTresComprension=multiplosTresComprension(listaA)#Se llama la función multiplosTresComprension
    print("Los números que son múltiplos de tres son: "+ str(multiplosDeTresComprension))#Se imprimen los elementos que son múltiplos de tres de la lista A
```
