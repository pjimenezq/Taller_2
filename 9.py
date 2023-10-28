#Resolver el punto 7 del taller 1 usando operaciones con vectores.
#Punto 7: Escriba un programa que pida 5 números reales y calcule las siguientes operaciones: el promedio, la mediana, el promedio multiplicativo (multiplica todos y luego calcula la raíz de la cantidad de operandos), ordenar los números de forma ascendente, ordenar los números de forma descendente, la potencia del mayor número elevado al menor número, la raíz cúbica del menor número

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
