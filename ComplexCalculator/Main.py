##############################
## UTILIZACION DE LIBRERIAS ##
##############################
from sys import stdin
from Complx_Calculator import *

####################
## METODO MAESTRO ##
####################
def main():
    #Lectura de 2 numeros Complejos de tipo cartesiano
    #Se deben ingresar 2 numeros separados por un espacio en cada linea
    num1 = Cartesian(tuple([float(x) for x in stdin.readline().split()]))
    num2 = Cartesian(tuple([float(x) for x in stdin.readline().split()]))
    #Se muestran enumeradas las Opciones requeridas para numeros complejos
    print("""
1-)Suma
2-)Resta
3-)Multiplicacion
4-)Division
5-)Conjugado
6-)Fase
7-)Cartesiano A Polar 
8-)Polar A Cartesiano
9-)Inverso Aditivo""")
    #Se debe ingresar el numero de la operacion que se desea realizar
    r = int(input(":"))
    #Se suman Los 2 Numeros Complejos
    if r == 1:
        print(num1 + num2)
    #Se resta entre 2 Numeros Complejos
    elif r == 2:
        print(num1 - num2)
    #Se Multiplican 2 Numeros Complejos
    elif r == 3:
        print(num1 * num2)
    #Se divide entre los 2 Numeros Complejos
    elif r == 4:
        print(num1.div(num2))
    #Muestra el Conjugado de ambos numeros
    elif r == 5:
        print(num1.conj(), "\n", num2.conj())
    #Muestra la fase de ambos numeros
    elif r == 6:
        print( phase((num1.element_1, num1.element_2)), "\n",
               phase((num2.element_1, num2.element_2)) )
    #Convierte de coordenadas Cartesianas a polares ambos Complejos
    elif r == 7:
        print(Pol((num1.element_1, num1.element_2)).cart_to_pol(), "\n",
              Pol((num2.element_1, num2.element_2)).cart_to_pol())
    #Convierte de Coordenadas Polares a Cartesianas ambos complejos
    elif r == 8:
        print(Cartesian((num1.element_1, num1.element_2)).pol_to_cart(), "\n",
              Cartesian((num2.element_1, num2.element_2)).pol_to_cart())
    #Muestra el inverso Aditivo de ambos numeros
    elif r == 9:
        print(num1.inv(), "\n", num2.inv())
main()
