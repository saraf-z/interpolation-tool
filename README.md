# interpolation-tool
Tool for the interpolation of logaritmic data

# Development notes 

The goal of the program is to 

- Read two different .xlsx files
- Extract data from said files, and convert the data into variables.
- Save the data from said files and being capable of automating interpolations.
- Allow the user to select what type of interpolation has to be done. 
- Show the data selected.

  Starting point:

  The files of reference are two .xlsx files, each of them having two columns of data that need to be interpolated. These interpolations must be done in logarthmic scale then converted back to exponential.  

# Design Process:
First, we divide the problem into different blocks

1 First Block. Input
The input of the data are two excel files, which could be converted into csv. This will be defined further into the making of the proyect. 

2 Second Block. Functions. 
This is the part where the key functionalities of the program reside. 
Here is where we will need to define all of the procedures from receiving the data, to transform the data into logarthmic scale, to then process the data as the user inputs, to then be processed, converted back to exponentials, and show back to the user via defined output. 

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

interpolation_script.py:4

