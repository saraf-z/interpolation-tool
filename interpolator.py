# Goal: Interpolate quantity from quantity energy distribution
# Modeling steps: script, functional programing and OOP programing
from math import log

# Input data: define some dummy data to test the script
energy = [1,2,3]  # Energy values of the distribution
values = [10,20,30]  # Variable values of the distribution
interpolated_energy = 1.5  # Energy value to interpolate

# Logarithmic transformation: calculate logarithmic values of energy and values
log_energy = [log(i) for i in energy]
log_values = None

# Interpolate

# Print results
print(f'Energy: {energy}')
print(f'Logarithmic energy: {log_energy}')
