# -*-coding:utf-8 -*-
import math
from re import X
from tabulate import tabulate

#Función que encuentra el valor de B en la regresión
def B(x=[],y=[]):
    sum_num = 0
    sum_den = 0

    tabla = []

    for i in range(0,len(x)):
        x_i = x[i]
        y_i =y[i]

        sum_num += x_i*y_i
        sum_den += x_i*x_i

        tabla.append([
            x.index(x_i)+1,
            x_i*y_i,
            x_i*x_i
        ])

    tabla.append([
        "SUM",
        sum_num,
        sum_den, 
    ])

    print("\n")

    print(tabulate(
        tabla,
        headers=["No.","(x_i * y_i)","x_i^2", "y_i - B+x_i"],
        tablefmt="grid"
        ))

    return sum_num/sum_den

#desviación de y
def des_y(B, x=[], y=[]):

    suma = 0

    table = []

    for i in range(0,len(x)):
        x_i = x[i]
        y_i =y[i]

        suma += (y_i - (B*x_i))*(y_i - (B*x_i))

        table.append([
            i+1,
            (y_i - (B*x_i))*(y_i - (B*x_i))
        ])

    table.append([
        "SUM",
        suma
    ])

    print(tabulate(
        table,
        headers=["No.","( y_i - B*x_i )^2"],
        tablefmt="grid"
        ))

    return math.sqrt(( 1/(len(x)-1) )*suma)

#Incertidumbre de B
def incertidumbre_B(B, x=[], y=[]):
    suma = 0

    for i in range(0,len(x)):
        x_i = x[i]

        suma += x_i*x_i

    return des_y(B,x,y)/math.sqrt(suma)    

#Función que obtiene promedio de los items en un arreglo
def getPromedio(arr = []):
    prom = 0

    for i in arr:
        prom += i

    return prom/( len(arr) )

#Función que calcula la R
#def getR()

#Creación de coeficiente de correlación linea
def coef_cor_lin(x=[], y=[]):

    tabla = []

    prom_X = getPromedio(x)
    prom_Y = getPromedio(y)
    sum_x_sqrd = 0
    sum_y_sqrd = 0
    sum_x_y = 0
    sum_x = 0
    sum_y = 0

    for i in range(0,len(x)):
        x_i = x[i]
        y_i =y[i]

        tabla.append([ 
            x.index(x_i)+1,
            x_i,
            y_i,
            round(x_i - prom_X,4),
            round(y_i - prom_Y,4),
            round(pow(x_i - prom_X, 2),5),
            round(pow(y_i - prom_Y, 2),5),
            round((x_i - prom_X) * (y_i - prom_Y),5)
         ])

        sum_x += x_i
        sum_y += y_i
        sum_x_sqrd += round(pow(x_i - prom_X, 2),5)
        sum_y_sqrd += round(pow(y_i - prom_Y, 2),5)
        sum_x_y += round((x_i - prom_X) * (y_i - prom_Y),5)

    tabla.append([
        "SUM",
        sum_x,
        sum_y,
        "",
        "",
        sum_x_sqrd,
        round(sum_y_sqrd,4),
        sum_x_y
    ])

    tabla.append([
        "PROM",
        prom_X,
        prom_Y,
        "",
        "",
        "",
        "",
        ""
    ])

    r = sum_x_y/( math.sqrt(sum_x_sqrd*sum_y_sqrd) )

    print(tabulate(tabla,
     headers=["No.","x","y","x-X","y-Y", "(x-X)^2", "(y-Y)^2", "(x-X)(x-Y)"],
     tablefmt="grid"
     ))
    print("\nr = %s\n\n"%(r))

#MAIN****************+
x = [6.0025,5.5084,5.3038, 4.9863,4.8136,4.6612]
y = [57.56,53.93,50.45,48.52,46.82,45.04]


coef_cor_lin(x,y)

b = B(x,y)

print("\nB: %s"%(b))
print("Incertidumbre: %s"%(incertidumbre_B(
    b,
    x,
    y
) ))