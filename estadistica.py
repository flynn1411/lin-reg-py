#-*-coding:utf-8-*-

import math


def media(dat=[]):
    res = 0

    for i in dat:
        res += i

    return res/(len(dat))

def desviacion_estandar(dat = []):
    res = 0
    suma = 0
    prom = media(dat)

    for i in dat:
        suma += (i-prom)*(i-prom)

    res = ( 1/( len(dat) - 1 ) )*suma

    return math.sqrt(res)

def desviacion_media(dat = []):
    return (desviacion_estandar(dat))/(math.sqrt(len(dat)))

longitudes = [
    2.903,
    2.900,
    2.903,
    2.902,
    2.901
]

tiempos = [
    3.427,
    3.424,
    3.43,
    3.419,
    3.463
]

print("Longitudes:")

print("Media %s"%(media(longitudes)))

print("Desviación estándar %s"%(desviacion_estandar(longitudes)))

print("Desviación Estándar de la Media %s"%(desviacion_media(longitudes)))

print("\nTiempos:")

print("Media %s"%(media(tiempos)))

print("Desviación estándar %s"%(desviacion_estandar(tiempos)))

print("Desviación Estándar de la Media %s"%(desviacion_media(tiempos)))