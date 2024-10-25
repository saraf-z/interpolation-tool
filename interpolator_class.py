from math import log, exp
import numpy as np
from scipy.interpolate import Akima1DInterpolator


# interpolator class
class Interpolator:
    # constructor to initialize attributes
    #atributes store static data that is not visible to the user.
    def __init__(self, energy, values, interpolated_energy):
        self.energy = energy
        self.values = values
        self.interpolated_energy = interpolated_energy

        self._log_energy = None
        self._log_values = None
        self._log_interpolated_energy = None
        self._log_interpolated_value = None

        self.interpolated_value = None

        #

        # select data frame path, clean file (atributes = cleanvalues)

        # method to transform initial values into logarithmic data

    def take_logarithm(self):
        self._log_energy = [log(i) for i in self.energy]
        self._log_values = [log(i) for i in self.values]
        self._log_interpolated_energy = log(self.interpolated_energy)

    # method to create a lineal interpolation of the interpolated energy using "values" and "energy"
    def log_linear_interpolation(self):
        """Interpolate the value at the given energy point."""
        # if self._log_energy is None or self._log_values is None:
        #     self.take_logarithm() #call to clean data
        self.take_logarithm()
        self._log_interpolated_value = np.interp(self._log_interpolated_energy, self._log_energy, self._log_values)
        self.log_to_value()
        return self.interpolated_value

    # method to create an akima-type interpolation of the interpolated energy
    def log_akima_interpolation(self):
        """Interpolate the value at the given energy point using Akima interpolation."""
        self.take_logarithm()  # call to clean data
        akima_interpolator = Akima1DInterpolator(self._log_energy, self._log_values)
        self._log_interpolated_value = akima_interpolator(self._log_interpolated_energy)
        self.log_to_value()
        return self.interpolated_value

    def log_to_value(self):  # function to return values from logarithmic to int
        """transforms values from logarithmic scale to lineal"""
        # interpolated_value = exp(log_interpolated_value)
        self.interpolated_value = exp(self._log_interpolated_value)
        return self.interpolated_value


# function def_read_spectrum_from_file : read path is csv - boolean true/false
#inside interpolation method cleaning files must be included!

def main():
    print('Script interpolator_class.py')
    # define paths . calll read spectrum
    # select paths

    # Input data: define some dummy data to test the script
    energy = [1, 2, 3]  # Energy values of the distribution
    values = [10, 20, 30]  # Variable values of the distribution
    interpolated_energy = 1.5  # Energy value to interpolate

    # Create an instance of class Interpolator
    interpolator = Interpolator(energy, values, interpolated_energy)

    # Perform linear interpolation
    linear_value = interpolator.log_linear_interpolation()
    print("Linear Interpolation:", linear_value)

    # Perform Akima interpolation
    akima_value = interpolator.log_akima_interpolation()
    print("Akima Interpolation:", akima_value)


# main block
if __name__ == "__main__":
    main()
