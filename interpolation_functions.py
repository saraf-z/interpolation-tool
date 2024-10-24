import math
from idlelib.autocomplete import FILES

import numpy as np
import pandas as pd
from scipy.interpolate import Akima1DInterpolator
from math import log, exp
from openpyxl import load_workbook


#load Excel spreadsheet
#convert data from spreadsheet into energy, and values
#clean data

def read_csv_file (file_path_csv):
    """ This function reads a CSV file using pandas and returns the DataFrame."""
    file_path_csv = r'n60.csv'  # csv file path created
    try:
        df =pd.read_csv(file_path_csv)
        return df
    except FileNotFoundError:
        print(f"Error: The file {file_path_csv} was not found.")
        return None
print(read_csv_file('n60.csv'))

def clean_data (df): #reads the rows, identifies irrelevant data and deletes said data
    """This function cleans unused data by removing rows where the value us less than or equal to 0 """

    #Initialize lists to hold clean values
    clean_energies = []
    clean_values = []
    #Extrae columnas 'Energy[keV]' y 'Fluence_rate [cm^-2s^-1]' del DataFrame
    energy =df['Energy[keV]']
    values = df['Fluence_rate [cm^-2s^-1]']

    #Itera sobre ambas columnas simultaneamente
    for i, j in zip (energy, values):
        if j>0:#solo si el valor es mayor que j
            clean_energies.append(i)
            clean_values.append(j)
        else:
            pass
        # print(clean_energies)
        print(0 in clean_values)
        print(len(clean_energies) == len(clean_values))
        return pd.DataFrame({'clean_energies': clean_energies, 'clean_values': clean_values})



# Logarithmic transformation: calculate logarithmic values of energy and values
def take_logarithm(clean_energies, clean_values, interpolated_energy):
    """Calculate the logarithm of a set of values."""
    log_energy = [log(i) for i in clean_energies]
    log_values = [log(e) for e in clean_values]
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

def log_to_value(log_interpolated_value, log_interpolated_value_akima): #function to return values from logarithmic to int
    interpolated_value = math.exp(log_interpolated_value)
    interpolated_value_akima = math.exp(log_interpolated_value_akima)
    return interpolated_value, interpolated_value_akima

def main():
    print('Script interpolator_functions.py')
    file_path_csv = r'n60.csv'
    result = read_csv_file(file_path_csv)

    # Input data: define some dummy data to test the script
    # energy = [1, 2, 3]  # Energy values of the distribution
    # values = [10, 20, 30]  # Variable values of the distribution
    # interpolated_energy = 1.5  # Energy value to interpolate
    #take logarithms of the data
    # log_energy, log_values, log_interpolated_energy = take_logarithm(energy, values, interpolated_energy)
    # #log-linear
    # log_interpolated_value = log_linear_interpolation(log_energy, log_values, log_interpolated_energy)
    # #log-akima
    # log_interpolated_value_akima = log_akima_interpolation(log_energy, log_values, log_interpolated_energy)
    # #convert to normal values
    # interpolated_value, interpolated_value_akima = log_to_value(log_interpolated_value, log_interpolated_value_akima)
    #
    # print(f'Energy: {energy}')  #prints values of variables used in functions
    # print(f'Values:{values}')
    # print(f'Interpolated_energy:{ interpolated_energy }')
    # print(f'log_energy:{log_energy}')
    # print(f'log_values:{log_values}')
    # print(f'log_interpolated_energy:{log_interpolated_energy}')
    # print(f'log_interpolated_value:{log_interpolated_value}')
    # print(f'log_interpolated_value_akima{log_interpolated_value_akima}')
    # print(f'Interpolated value: {interpolated_value}')
    # print(f'Interpolated_value (Akima):{interpolated_value_akima}')


 #def cli():
    # Command Line Interface to get input from the user
    # # Step 1: Get input for energy and values from the user
    # # print('Introduce data for energy (comma-separated, e.g., "1, 2, 3"), then press enter:')
    # # energy_input = input()
    # #
    # # print('Introduce data for values (comma-separated, e.g., "10, 20, 30"), then press enter:')
    # # values_input = input()
    #
    # # Step 2: Get input for the interpolated energy value
    print('Introduce interpolated energy (a single number, e.g., "1.5"):')
    interpolated_energy = float(input())  # Convert the user input to a float
    # # Step 3: Perform the logarithmic transformation
    # log_energy, log_values, log_interpolated_energy = take_logarithm(energy, values, interpolated_energy)
    #
    # # Step 4: Perform the interpolations
    # log_interpolated_value = log_linear_interpolation(log_energy, log_values, log_interpolated_energy)
    # log_interpolated_value_akima = log_akima_interpolation(log_energy, log_values, log_interpolated_energy)
    #
    # # Step 5: Convert log-interpolated values to normal values
    # interpolated_value, interpolated_value_akima = log_to_value(log_interpolated_value, log_interpolated_value_akima)
    #
    # # Step 6: Print the results
    # print(f'Log Interpolated Value (Linear): {log_interpolated_value}')
    # print(f'Log Interpolated Value (Akima): {log_interpolated_value_akima}')
    # print(f'Interpolated Value (Linear): {interpolated_value}')
    # print(f'Interpolated Value (Akima): {interpolated_value_akima}')
    #
    #

# main block

if __name__ == "__main__":
    main()



