import numpy as np
from scipy.interpolate import Akima1DInterpolator
from math import log, exp



# Logarithmic transformation: calculate logarithmic values of energy and values
def take_logarithm(energy, values, interpolated_energy):
    """Calculate the logarithm of a set of values."""
    log_energy = [log(i) for i in energy]
    log_values = [log(i) for i in values]
    log_interpolated_energy = log(interpolated_energy)
    return log_energy, log_values, log_interpolated_energy


# Interpolate lineal: takes values: energy, values and interpolated energy, returns interpolated value with the solution
def log_linear_interpolation(log_energy, log_values, log_interpolated_energy):
    """Interpolate the value at the given energy point."""
    log_interpolated_value = np.interp(log_interpolated_energy, log_energy, log_values)
    return log_interpolated_value


# Interpolate akima: takes energy, values and interpolated_energy, returns interpolated_value_akima
def log_akima_interpolation(log_energy, log_values, log_interpolated_energy):
    """Interpolate the value at the given energy point using Akima interpolation."""
    akima_interpolator = Akima1DInterpolator(log_energy, log_values)
    log_interpolated_value_akima = akima_interpolator(log_interpolated_energy)
    return log_interpolated_value_akima


def main():
    print('Script interpolator_functions.py')
    # Input data: define some dummy data to test the script
    energy = [1, 2, 3]  # Energy values of the distribution
    values = [10, 20, 30]  # Variable values of the distribution
    interpolated_energy = 1.5  # Energy value to interpolate
    log_energy, log_values, log_interpolated_energy = take_logarithm(energy, values, interpolated_energy)
    take_logarithm(energy, values, interpolated_energy)
    log_linear_interpolation(log_energy, log_values, log_interpolated_energy)
    log_akima_interpolation(log_energy, log_values, log_interpolated_energy)


# main block

if __name__ == "__main__":
    main()


#cli console requesting data from user: energy, values and interpolated_energy
#energy input, three numbers
print(f'introduce data for energy, then press enter:')
energy_input= str (input())
print(f'introduce data for values, then press enter:')
value_input= str (input())

print (f'the result of your operation is:{energy_input} {value_input}')