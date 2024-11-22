# interpolation-tool
Tool for the interpolation of logaritmic data

# Development notes 

The goal of the program is to 

- INPUT: Read two different .xlsx files
- Convert input: Extract data from these Excel files, and convert the data into variables. Take logs
- INPUT: Read the data to be interpolated. Take log
- Select interpolation technique: Allow the user to select the type of interpolation technique to be performed.
- Action: performs the interpolation and reverts the logarithm with the exponential function.
- OUTPUT: Shows the final interpolated data.

  Starting point:

  The input files are two .xlsx files, each of them having two columns of data in which the user needs the interpolation. These interpolations have to be performed with all the variables in logarithmic scale. After the interpolation will be converted back to exponential.  

# Design Process:
First, we divide the problem into different blocks

1 First Block. Input
The input of the data are two excel files, which could be converted into csv. This will be defined later. One Excel file contains the original data (x,y) and the other contains the data (xprime) we would like to get the interpolated function (yprime). 

2 Second Block. Functions. 
This is the part where the key functionalities of the program reside. 
Here is where the program converts the data into logarthmic scale, makes the interpolation and then uses exponential functions to return the output. 

3 Third Block. Output. 
The output format will be dependent of the processing needed for the input in the first block. 

# Scripting 

To ensure functionality the creation and testing of the program will be done in a process of structured scripting. The three scripts belong to three different phases. 

- Interpolation_script:

This is the main script. Here the basic functionality of the program will be structured following a timeline of processes. 

- Interpolation_functions:

Here, functions from the main script are separated and structured. 

- Interpolation_class:

On this file, functions get structured into classes and methods for OOP.
  

# interpolation script: 
¿ what does this code do ? 
1- Imports necesary libraries.
2-Read Excel/csv file
3- Holds data from excel file into columns 
4- Cleans data to discard unnecesary information
5- Transforms clean data into logarithms 
6- Takes logarithmic value and interpolates it 
7- Transforms log values into exp values 
8 - Prints the result fo said values 

# Interpolation functions: 
¿ What does this code do?

1- import necesary libraries
2- reads csv file
3- Cleans data from file
4- Transforms numbers from exponential escale to logarithmic scale
5- Has a function that creates linear interpolations 
6- Has a function that creates Akima interpolations
7- Has a function that transforms from log to exp 
8- Uses main() function to initialize functions
9-Cli function: console to ask user for the data it seeks to interpolate.

Inside the Cli() function, there are the following commands: 
1. ask the user to select the interpolation type 
2. ask the user the data variable that needs to be interpolated
3. (invisible):
   call the functions: read_csv_file, clean_data, take_logarithm, select interpolation
   call the functions: log_linear/ akima,
   then: log_to_value and show_graph 

# What is in the Script? 

1. Imports and set ups:

2. pd.FUNCTIONS to upload csv, read and organize into two lists. Test that the information is correct and then functions to print the results
3. .append functions to clean data in the lists
4. Logarithmic transformation. with .log function
5. Lineal Interpolation (in log)
6. Akima Interpolation (in log)
7. Reversar la transformacion logaritmica
8. Mostrar los resultados de la operacion por pantalla

