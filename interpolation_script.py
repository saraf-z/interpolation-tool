# Goal: Interpolate quantity from quantity energy distribution
# Modeling steps: script, functional programing and OOP programing
from math import log, exp
import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import Akima1DInterpolator, interp1d
from openpyxl import load_workbook
import csv
import pandas as pd

#Option used: read csv file with pandas
print('Script interpolator_script.py')
# Input data: from csv file
file_path_excel = r"C:\Users\VPECOS\Desktop\documentos sara\PRACTICAS\DOCUMENTACION\N60.xlsx"
file_path_csv = r'n60.csv'# csv file path created
df_excel = pd.read_excel(file_path_excel)#call to excel file
print(df_excel.head)
df = pd.read_csv(file_path_csv)
# print(df.head())
# print(type(df['Energy[keV]']))
# print(df['Fluence_rate [cm^-2s^-1]'])
column1 = list(df['Energy[keV]'])
column2 = list(df['Fluence_rate [cm^-2s^-1]'])

# testing the script
energy = column1  # Energy values of the distribution
values = column2  # Variable values of the distribution
interpolated_energy = 20.9  # Energy value to interpolate

#print results
print(f'Energy: {energy}')
print (f'Values: {values}')
print (f'interpolated_energy: {interpolated_energy}')

# Clean data
clean_energies, clean_values = [], []
for i, j in zip(energy, values):
    # print('line', i, j)
    if j>0:
        clean_energies.append(i)
        clean_values.append(j)
    else:
        pass
#print(clean_energies)
print(0 in clean_values)
print(len(clean_energies)==len(clean_values))

# Logarithmic transformation: calculate logarithmic values of energy and values
log_energy = [log(i) for i in clean_energies]
log_values = [log(i) if i>0 else None for i in clean_values]
log_interpolated_energy = log(interpolated_energy)
#saltar valor = 0, y energia correspondiente al valor 0
#clean data before converting logarithm
#print results
print (f'log_energy: {log_energy}')
print (f'log_values: {log_values}')
print (f'log_interpolated_energy: {log_interpolated_energy}')

#Ask user for interpolation:
##3. ask user for type of interpolation
print("Select the interpolation type:")
print("1 - Linear")
print("2 - Quadratic")
print("3 - Cubic")
print("4 - Akima")
interpolation_type = input("Enter the number corresponding to the interpolation type: ")
try:
    if interpolation_type == '1':
        interp_function = interp1d(column1, column2, kind='linear')
        print("Linear interpolation selected.")
        log_interpolated_value = np.interp(log_interpolated_energy, log_energy, log_values)
        interpolated_value = exp(log_interpolated_value)
        print("Interpolated log value:", log_interpolated_value, "Exponential value:", interpolated_value)
        #plotting
        plt.figure(figsize=(8, 6))
        plt.plot(energy, values, 'o', label='Data points', color='blue')
        plt.plot(interpolated_energy, interpolated_value, 'ro',
                 label=f'Exp Interpolated value ({interpolated_value:.2f})')
        plt.plot(energy, interp_function(energy), '-', color='gray', label='Linear Interpolation (log scale')
        plt.xlabel("log_energy")
        plt.ylabel("log_values")
        plt.title("Exponential Linear Interpolation with Graph")
        plt.legend()
        plt.grid(True)
        plt.show()

    elif interpolation_type == '2':
        interp_function = interp1d(column1, column2, kind='quadratic')
        print("Quadratic interpolation selected.")
        log_interpolated_value_quadratic = np.interp(log_interpolated_energy, log_energy, log_values)
        interpolated_value_quadratic = exp(log_interpolated_value_quadratic)
        print("Interpolated log value:", log_interpolated_value_quadratic, "Exponential value:", interpolated_value_quadratic)
        # plotting
        plt.figure(figsize=(8, 6))
        plt.plot(energy, values, 'o', label='Data points', color='blue')
        plt.plot(interpolated_energy, interpolated_value_quadratic, 'ro',
                 label=f'Exp Interpolated value ({interpolated_value_quadratic:.2f})')
        plt.plot(energy, interp_function(energy), '-', color='gray', label='Linear Interpolation (log scale')
        plt.xlabel("log_energy")
        plt.ylabel("log_values")
        plt.title("Exponential Linear Interpolation with Graph")
        plt.legend()
        plt.grid(True)
        plt.show()

    elif interpolation_type == '3':
        interp_function = interp1d(column1, column2, kind='cubic')
        print("Cubic interpolation selected.")
        log_interpolated_value_cubic = np.interp(log_interpolated_energy, log_energy, log_values)
        interpolated_value_cubic = exp(log_interpolated_value_cubic)
        print("Interpolated log value:", log_interpolated_value_cubic, "Exponential value:",interpolated_value_cubic)
        plt.figure(figsize=(8, 6))
        plt.plot(energy, values, 'o', label='Data points', color='blue')
        plt.plot(interpolated_energy, interpolated_value_cubic, 'ro',
                 label=f'Exp Interpolated value ({interpolated_value_cubic:.2f})')
        plt.plot(energy, interp_function(energy), '-', color='gray', label='Linear Interpolation (log scale')
        plt.xlabel("log_energy")
        plt.ylabel("log_values")
        plt.title("Exponential Linear Interpolation with Graph")
        plt.legend()
        plt.grid(True)
        plt.show()

    elif interpolation_type == '4':
        interp_function = Akima1DInterpolator(column1, column2)
        print("Akima interpolation selected.")
        akima_interpolator = Akima1DInterpolator(column1, column2)  # get energy and values as args for the Akima1D function
        log_interpolated_value_akima = akima_interpolator(log_interpolated_energy)  # shows in result the result of the Akima1D interpolation
        interpolated_value_akima = exp(log_interpolated_value_akima)
        #Plotting
        plt.figure(figsize=(8, 6))
        plt.plot(energy, values, 'o', label='Data points', color='blue')
        plt.plot(interpolated_energy, interpolated_value_akima, 'ro',
                 label=f'Exp Interpolated value ({interpolated_value_akima:.2f})')
        plt.plot(energy, akima_interpolator(energy), '-', color='gray',label='Exponential Linear interpolation')
        plt.xlabel("log_energy")
        plt.ylabel("log_values")
        plt.title("Exponential Linear Interpolation with Graph")
        plt.legend()
        plt.grid(True)
        plt.show()


    else:
        print("Invalid selection. Please enter 1, 2, 3 or 4")
        exit()
except Exception as e:
    print(f"An error occurred: {e}")

#
