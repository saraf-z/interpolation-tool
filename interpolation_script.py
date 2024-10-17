# Goal: Interpolate quantity from quantity energy distribution
# Modeling steps: script, functional programing and OOP programing
from math import log, exp
import numpy as np
from scipy.interpolate import Akima1DInterpolator

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



# Input data: define some dummy data to test the script
energy = [1,2,3]  # Energy values of the distribution
values = [10,20,30]  # Variable values of the distribution
interpolated_energy = 1.5  # Energy value to interpolate

# Logarithmic transformation: calculate logarithmic values of energy and values
def take_logarithm(energy, values):
    """Calculate the logarithm of a set of values."""
    log_energy = [log(i) for i in energy]
    log_values = [log(i) for i in values]
    return log_energy, log_values

log_energy, log_values = take_logarithm(energy, values)

# Interpolate lineal: takes values: energy, values and interpolated energy, returns interpolated value with the solution
def linear_interpolation(energy, values, interpolated_energy):
    """Interpolate the value at the given energy point."""
    interpolated_value = np.interp(interpolated_energy, energy, values)
    return interpolated_value

# Interpolate akima: takes energy, values and interpolated_energy, returns interpolated_value_akima
def akima_interpolation(energy, values, interpolated_energy):
    """Interpolate the value at the given energy point using Akima interpolation."""
    akima_interpolator = Akima1DInterpolator(energy, values)
    interpolated_value_akima = akima_interpolator(interpolated_energy)
    return interpolated_value_akima

# Print results
print(f'Energy: {energy}')
print(f'Logarithmic energy: {log_energy}')
print(f'Values: {values}')
print(f'Logarithmic values: {log_values}')
print(f'Interpolated value (Akima) at energy {interpolated_energy}: {interpolated_value_akima}')