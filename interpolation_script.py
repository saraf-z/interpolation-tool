# Goal: Interpolate quantity from quantity energy distribution
# Modeling steps: script, functional programing and OOP programing
from math import log, exp
import numpy as np
from scipy.interpolate import Akima1DInterpolator
from openpyxl import load_workbook
import csv
import pandas as pd

print('Script interpolator_script.py')

# Input data: from csv file
file_path_excel = r"C:\Users\VPECOS\Desktop\documentos sara\PRACTICAS\DOCUMENTACION\N60.xlsx"
file_path_csv = r'n60.csv'

df_excel = pd.read_excel(file_path_excel)
print(df_excel.head)

# Option 2: using pandas
df = pd.read_csv(file_path_csv)
# print(df.head())
# print(type(df['Energy[keV]']))
# print(df['Fluence_rate [cm^-2s^-1]'])
column1 = list(df['Energy[keV]'])
column2 = list(df['Fluence_rate [cm^-2s^-1]'])
# print(column1)
# print(column2)

# Option 1: parsing csv file as a text file
# with open(file_path, mode='r') as file:
    # energy, values = [], []
    # for row in file:
    #     print(str(row))
    #     line = row.strip('\n').split(';')
    #     print(line)
    #     print(line[0])
    #     print(line[1])
    #     energy.append(float(line[0]))
    #     values.append(float(line[1]))
    #     print(energy)
    #     print(values)

    #content = file.read()
    #print(content)
    #print(type(content))
    #listas vacias para las columnas
    # columna1 = []
    #columna2 = []
    #recorrer el archivo CSV fila por fila

    # print(content[0])
    #for row in content :
        #print(row.split(';'))
        #pass
        # print(row)
        # columna1.append(row['Energy[keV]'])
        #columna2.append(row['Fluence_rate [cm^-2s^-1]'])
    #print("columna1:", columna1)
    #print("columna2:",columna2)

# Input data: define some dummy data to test the script
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
