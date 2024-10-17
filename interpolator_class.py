from math import log, exp
import numpy as np
from scipy.interpolate import Akima1DInterpolator


# interpolator class
class Interpolator:
    # constructor to initialize attributes
    def __init__(self, energy, values, interpolated_energy):
        self.energy = energy
        self.values = values
        self.interpolated_energy = interpolated_energy

    # method to transform initial values into logarithmic data
    def take_logarithm(self):
        log_energy = [log(i) for i in self.energy]
        log_values = [log(i) for i in self.values]
        log_interpolated_energy = log(self.interpolated_energy)
        return log_energy, log_values, log_interpolated_energy

    # method to create a lineal interpolation of the interpolated energy using "values" and "energy"
    def log_linear_interpolation(self, log_energy, log_values, log_interpolated_energy):
        """Interpolate the value at the given energy point."""
        log_interpolated_value = np.interp(log_interpolated_energy, log_energy, log_values)
        return log_interpolated_value

    # method to create an akima-type interpolation of the interpolated energy
    def log_akima_interpolation(self, log_energy, log_values, log_interpolated_energy):
        """Interpolate the value at the given energy point using Akima interpolation."""
        akima_interpolator = Akima1DInterpolator(log_energy, log_values)
        log_interpolated_value_akima = akima_interpolator(log_interpolated_energy)
        return log_interpolated_value_akima


def main():
    # Input data: define some dummy data to test the script
    energy = [1, 2, 3]  # Energy values of the distribution
    values = [10, 20, 30]  # Variable values of the distribution
    interpolated_energy = 1.5  # Energy value to interpolate

    print("Energy", energy)
    print("Values", values)
    print("Interpolated_energy", interpolated_energy)

    # Create an instance of class Interpolator
    interpolator = Interpolator(energy, values, interpolated_energy)

    energy = interpolator.energy
    values = interpolator.values
    interpolated_energy = interpolator.interpolated_energy

    # Print the attributes of the interpolator object
    print("Energy (from interpolator):", interpolator.energy)
    print("Values (from interpolator):", interpolator.values)
    print("Interpolated energy (from interpolator):", interpolator.interpolated_energy)

    print(type(interpolator))




# main block
if __name__ == "__main__":
    main()
