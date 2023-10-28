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

Para solucionar este punto se crea una función que tiene como argumentos dos listas diferentes. En este caso la función se nombró diferenciaLista.
La función compara cada uno de los elementos de la primera lista con los elementos de la segunda lista y cuando son iguales, se elimina ese elemento de la primera lista. Después de que se ejectuta la anterior instrucción, la función retorna la primera lista (ahora que en la primera lista, ya no están los elementos que también tiene la segunda lista).

2. Usar la función

Se define la función main, se declaran las dos listas con los elementos que se deseen, se llama la función creada anteriormente (llamada diferenciaLista) y se imprime el resultado. Es decir que el programa va a imprimir la lista con los elementos que únicamente tiene la primera lista.


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

**Explicación de la solución**



**Código**
```
```
## Décimo punto
**Instrucción**

Suponga que se tiene una lista A con ciertos números enteros. Desarrolle una función que, independientemente de los números que se encuentran en la lista A, tome aquellos números que son múltiplos de 3 y los guarde en una lista nueva, la cual debe ser retornada por la función. Implemente la perspectiva de un patrón de acumulación y también de comprensión de listas. 

**Explicación de la solución**



**Código**
```
```
