import numpy as np
from scipy.interpolate import Akima1DInterpolator

#funcion de entrada

#funciones de proceso

# Caso1: Funcion sencilla de interpolacion de los datos del excel que se encuentran en el documento "test" (sheet2)
# Datos de columna1: EnergyKeV
# la condicion es que ambos parametros estén en la misma medida o tengan la misma longitud. (posiblemente haya que usar los resultados logaritmicos)

 def interpolar_fluence(energyKeV, fluence_rate, energy_i):
    # Verificamos que energyKeV y fluence_rate tengan la misma longitud
    if len(energyKeV) != len(fluence_rate):
        raise ValueError("Las listas de energyKeV y fluence_rate deben tener la misma longitud")

    # Realizamos la interpolación
    fluence_interpolada = np.interp(energy_i, energyKeV, fluence_rate)

    return fluence_interpolada


# Caso2: Funcion para la interpolacion de datos utilizando la funcion akima. Usando las funciones creadas en "interpolaciones2"
## la condicion es que estos datos deben ser leidos en arrays.

Ln_mu = np.array([10, 20, 30])
lnE = np.array([100, 150, 200])
lnEi = 15  # Valor de Ln_mu para el cual se desea interpolar

 rEi= np.interp(lnEi, Ln_mu, lnE) #### esta vez hago una comprobacion con la funcion de interpolacion lineal
print(f'El valor interpolado por interpolación lineal en Ln_mu = {lnEi} es {rEi}')

# Interpolación polinómica de grado 2
grado = 2
coeficientes = np.polyfit(Ln_mu, lnE, grado)
polinomio = np.poly1d(coeficientes)
lnE_interpolado = polinomio(lnEi)
print(f"El valor interpolado en Ln_mu = {lnEi} por polinomio de grado 2 es {lnE_interpolado}")

akima_interpolator = Akima1DInterpolator(Ln_mu, lnE)
lnE_akima = akima_interpolator(lnEi)
print(f"El valor interpolado por interpolación Akima en Ln_mu = {lnEi} es {lnE_akima}")


#funcion de salida