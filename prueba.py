import pandas as pd


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


###en el main:

import pandas as pd

# Ejemplo de DataFrame
data = {'energy': [1, 2, 3, 4], 'values': [10, -20, 30, 0]}
df = pd.DataFrame(data)

# Limpieza de datos
cleaned_df = clean_data(df)

# Ver los datos limpios
print(cleaned_df)

