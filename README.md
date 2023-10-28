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



**Código**
```
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



**Código**
```
```
## Quinto punto
**Instrucción**

Desarrollar un programa que permita determinar el Minimo Comun Multiplo de dos numeros enteros. Abordar el problema desde una perpectiva tanto iterativa como recursiva

**Explicación de la solución**



**Código**
```
```
## Sexto punto
**Instrucción**

Desarrollar un programa que determine si en una lista existen o no elementos repetidos.

**Explicación de la solución**



**Código**
```
```
## Séptimo punto
**Instrucción**

Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o más vocales. Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'.

**Explicación de la solución**



**Código**
```
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

*Punto 7 del taller 1:* 

Escriba un programa que pida 5 números reales y calcule las siguientes operaciones:

* El promedio
* La mediana
* El promedio multiplicativo (multiplica todos y luego calcula la raíz de la cantidad de operandos)
* Ordenar los números de forma ascendente
* Ordenar los números de forma descendente
* La potencia del mayor número elevado al menor número
* La raíz cúbica del menor número

**Explicación de la solución**



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



**Código**
```
```
