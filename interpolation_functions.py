import math
from idlelib.autocomplete import FILES

import numpy as np
import pandas as pd
from scipy.interpolate import Akima1DInterpolator
from math import log, exp
from openpyxl import load_workbook

from interpolation_script import log_energy, log_values


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

#function to select interpolation method
def select_interpolation():
    options = {
        1:"lineal",
        2:"Akima"
    }
    print("Select interpolation method")
    for key, value in options.items():
        print(f"{key}, {value}")
    while True:
        try:
            selected_method = int(input("Select method: "))
            if selected_method in options:
                print(f"Selected method [selected_method]")
                return options[selected_method]
            else:
                print("Unavailable method, try again")
        except ValueError:
            print("Invalid input, try again")

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

#function to visualize interpolation.


def main():
    print('Script interpolator_functions.py')
    # Contains main flow of the program
    #what is the main flow of the program?
    #Step1: Read file
    file_path = 'n60.csv'
    df= read_csv_file(file_path)
    #comprobar nombres

    try:
        clean_df = pd.read_csv(file_path)  # Cambia por la ruta de tu archivo
    except FileNotFoundError:
        print("Error: No se encontró el archivo de datos.")
        return

        # Verifica las columnas del DataFrame
    print("Columnas en el DataFrame:", clean_df.columns)

    # Prueba acceder a la columna 'Energy[keV]'
    try:
        clean_energies = clean_df['Energy[keV]']
    except KeyError:
        print("Error: La columna 'Energy[keV]' no existe. Verifica el nombre de la columna.")
        return  # Detiene la ejecución si no se encuentra la columna


    #step2: clean data
    if df is not None:
        print("Csv file read, cleaning data...")
        clean_df = clean_data(df)
        print ("Clean data update:")
        print(clean_df)
    else:
        print (" unable to read csv file.")





    #Step 3: ask user for the value of the interpolated_energy to start converting the numbers for the interpolations


    while True:
        try:
            interpolated_energy = float(input("Enter the energy point you want to interpolate in a range of 20.0 to 400: "))
            if interpolated_energy <= 0: #interpolated energy must be 20 or higher
                print("Invalid input, interpolated energy must be greater than 20 try again")
            else:
                break
        except ValueError:
            print("Invalid input, enter a numeric value")

    #Once a valid interpolated energy is obtained take_logarithm is called using clean_energies, clean_values and interpolated_energy
    #Step 4: Call the take_logarithm function with user input and example

    clean_energies = clean_df['Energy[keV]']
    clean_values = clean_df['Fluence_rate [cm^-2s^-1]']


    # Step 5: logarithm of the values
    log_energy, log_values, log_interpolated_energy = take_logarithm(clean_energies, clean_values, interpolated_energy)
    print("Logarithmic values:", log_energy, log_values, log_interpolated_energy)

    # Step 6: Logarithmic Interpolation
    interpolator = interp1d(log_energy, log_values, kind='linear', fill_value='extrapolate')
    interpolated_log_value = interpolator(log_interpolated_energy)

    # Step 7: Convert to exp
    interpolated_value = np.exp(interpolated_log_value)
    print(f"Interpolated value for energy {interpolated_energy} keV is approximately {interpolated_value}")






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
    print('Introduce interpolated energy (a single number from 20.0 to 400, e.g., "22.3"):')
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



