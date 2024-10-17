# Goal: Interpolate quantity from quantity energy distribution
# Modeling steps: script, functional programing and OOP programing
from math import log, exp
import numpy as np
from scipy.interpolate import Akima1DInterpolator

print('Script interpolator_script.py')

# Input data: define some dummy data to test the script
energy = [1,2,3]  # Energy values of the distribution
values = [10,20,30]  # Variable values of the distribution
interpolated_energy = 1.5  # Energy value to interpolate

#print results
print(f'Energy: {energy}')
print (f'Values: {values}')
print (f'interpolated_energy: {interpolated_energy}')

# Logarithmic transformation: calculate logarithmic values of energy and values
log_energy = [log(i) for i in energy]
log_values = [log(i) for i in values]
log_interpolated_energy = log(interpolated_energy)

#print results
print (f'log_energy: {log_energy}')
print (f'log_values: {log_values}')
print (f'log_interpolated_energy: {log_interpolated_energy}')

# Interpolate lineal
log_interpolated_value = np.interp(log_interpolated_energy, log_energy,log_values)# get interpolated_energy, energy and values as arguments for the np.interp function
#Akima interpolation
akima_interpolator = Akima1DInterpolator(log_energy, log_values)#get energy and values as args for the Akima1D function
log_interpolated_value_akima = akima_interpolator(log_interpolated_energy) #shows in result the result of the Akima1D interpolation

#print results
print (f'log_interpolated_value: {log_interpolated_value}')
print (f'log_interpolated_value_akima: {log_interpolated_value_akima}')

# inverse logarithmic transformation.
#interpolated_energy
interpolated_value = exp(log_interpolated_value)
interpolated_value_akima = exp(log_interpolated_value_akima)

# Print results
print (f'Interpolated value: {interpolated_energy}: {interpolated_value}')
print (f'Interpolated value (Akima) {interpolated_energy}: {interpolated_value_akima}')
