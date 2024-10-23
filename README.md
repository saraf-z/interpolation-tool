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
  





