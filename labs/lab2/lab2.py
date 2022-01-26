"""
Aidan Stout
lab2.py
Problem: creating a program that calculates the Root-mean-square, Harmonic mean, and the Geometric mean
I certify that this lab is entirely my work
"""

def means():
    number_of_values = eval(input("Enter the number of values to be entered:"))
    rms_average = 0
    harmonic_mean = 0
    geometric_mean = 1
    for i in range(number_of_values):
        input_values = eval(input("Enter value:"))
        rms_average = rms_average + input_values ** 2
        harmonic_mean = harmonic_mean + 1/input_values
        geometric_mean = geometric_mean * input_values
    rms_average = rms_average / number_of_values
    rms_average = rms_average ** (1/2)
    harmonic_mean = number_of_values / harmonic_mean
    geometric_mean = geometric_mean ** (1/number_of_values)
    print("The Root-Mean-Square is:",round(rms_average, 3))
    print("The Harmonic Mean is:", round(harmonic_mean, 3))
    print("The Geometric Mean is:", round(geometric_mean,3))



