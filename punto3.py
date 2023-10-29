#Creamos dos funciones, cada una para cada número que se evaluará si son espejos.
def nNumero(n):
    #La idea es poner los dígitos del número n en una lista oara ese número. Haciendo el mismo procedimiento en el punto 1
    while n > 0:
        nDigitos = n % 10
        nLista.append(nDigitos)
        n = n // 10
    return nLista

def mNumero(m):
    #Mismo caso para los dígitos del número m, pero cambiando el orden de los números de la lista con el slicing, para que en el momento que se vaya a evaluar, se pueda ver si son número espejos o no
    while m > 0:
        mDigitos = m % 10
        mLista.append(mDigitos)
        m = m // 10
    mListaOrd = mLista[::-1]
    return mListaOrd

if __name__ == "__main__":
    #En la función main le pedimos al usuario que ingrese un número entero para n y para m.
    n = int(input("Ingrese un número entero: "))
    m = int(input("Ingrese otro número entero: "))
    # Creamos las listas, para los dígitos de m y para los dígitos de n
    nLista = []
    mLista = []
    #Llamamos las funciones creadas
    nNum = nNumero(n)
    mNum = mNumero(m)
    #En este punto se evaluará si n y m son números espejos o no.
    #Si son listas iguales son números espejos, sino no. Ponemos el slicing para que se evalúen el orden de las listas.
    if nNum[:] == mNum[:]:
        print("los número son números espejos")
    else:
        print("Los números no son números espejos")