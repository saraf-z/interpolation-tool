
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

        self._log_energy = None
        self._log_values = None
        self._log_interpolated_energy = None

        self.interpolated_value = None


        # method to transform initial values into logarithmic data
    def take_logarithm(self):
        log_energy = [log(i) for i in self.energy]
        log_values = [log(i) for i in self.values]
        log_interpolated_energy = log(self.interpolated_energy)
        return log_energy, log_values, log_interpolated_energy

    def take_logarithm_(self):
        self.log_energy = [log(i) for i in self.energy]
        self.log_values = [log(i) for i in self.values]
        self.log_interpolated_energy = log(self.interpolated_energy)
        return

    # method to create a lineal interpolation of the interpolated energy using "values" and "energy"
    def log_linear_interpolation(self):
        """Interpolate the value at the given energy point."""
        self.interpolated_value = np.interp(self.log_interpolated_energy, self.log_energy, self.log_values)
        return

    # method to create an akima-type interpolation of the interpolated energy
    def log_akima_interpolation(self, log_energy, log_values, log_interpolated_energy):
        """Interpolate the value at the given energy point using Akima interpolation."""
        akima_interpolator = Akima1DInterpolator(log_energy, log_values)
        log_interpolated_value_akima = akima_interpolator(log_interpolated_energy)
        return log_interpolated_value_akima
    @staticmethod
    def log_to_value(self,log_energy, log_values,log_interpolated_value):  # function to return values from logarithmic to int
       """transforms values from logarithmic scale to lineal"""
       interpolated_value = exp(log_interpolated_value)
       interpolated_value_akima = exp(log_interpolated_value_akima)
       return lineal_energy, lineal_values, lineal_interpolated_value


def main():
    print('Script interpolator_class.py')

    # Input data: define some dummy data to test the script
    energy = [1, 2, 3]  # Energy values of the distribution
    values = [10, 20, 30]  # Variable values of the distribution
    interpolated_energy = 1.5  # Energy value to interpolate

    # Create an instance of class Interpolator
    interpolator = Interpolator(energy, values, interpolated_energy)

    energy = interpolator.energy
    values = interpolator.values
    interpolated_energy = interpolator.interpolated_energy
    #log_energy = interpolator.log_linear_interpolation(energy, values, interpolated_energy)
    #log_values = interpolator.log_linear_interpolation(energy, values, interpolated_energy)









# main block
if __name__ == "__main__":
    main()
