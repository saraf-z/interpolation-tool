# Goal: Interpolate quantity from quantity energy distribution
# Modeling steps: script, functional programing and OOP programing
from math import log
import numpy as np
from scipy.interpolate import Akima1DInterpolator

# Input data: define some dummy data to test the script
energy = [1,2,3]  # Energy values of the distribution
values = [10,20,30]  # Variable values of the distribution
interpolated_energy = 1.5  # Energy value to interpolate

# Logarithmic transformation: calculate logarithmic values of energy and values
log_energy = [log(i) for i in energy]
log_values = None

# Interpolate lineal
interpolated_value = np.interp(interpolated_energy, energy,values)# get interpolated_energy, energy and values as arguments for the np.interp function
#Akima interpolation
akima_interpolator = Akima1DInterpolator(energy, values)#get energy and values as args for the Akima1D function
interpolated_value_akima = akima_interpolator(interpolated_energy) #shows in result the result of the Akima1D interpolation

# Print results
print(f'Energy: {energy}')
print(f'Logarithmic energy: {log_energy}')
print (f'Interpolated value: {interpolated_energy}: {interpolated_value}')
print (f'Interpolated value (Akima) {interpolated_energy}: {interpolated_value_akima}')

# ------------------------------------

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
