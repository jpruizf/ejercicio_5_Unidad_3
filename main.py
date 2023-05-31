from clase_Interface import Coleccion

if __name__ == '__main__':
    i_coleccion = Coleccion()
    elemento = int(input("Ingrese el elemento >> "))
    posicion = int(input("Ingrese la posicion >> "))
    i_coleccion.insertarElemento(elemento, posicion)
    elemento = 0
    elemento = int(input("Ingrese el elemento >> "))
    i_coleccion.agregarElemento(elemento)
    posicion = 0
    posicion = int(input("Ingrese la posicion >> "))
    i_coleccion.mostrarElemento(posicion)