#!/usr/bin/python3
"""
Python Practical Code for heterodyning and performance testing
Keegan Crankshaw
Date: 7 June 2019

This isn't necessarily performant code, but it is Pythonic
This is done to stress the differences between Python and C/C++

"""

# import Relevant Librares
import numpy as np;
import Timing
from data import carrier, data

# Define values.
c = carrier
d = data
result = []

# Main function
def main():
    Timing.startlog()
    for i in range(len(c)):
        result.append(c[i] * d[i])
    Timing.endlog()

    for i in range(len(c)):
        result[i] = float(result[i])
    np.savetxt("PythonResult1.txt", result, delimiter=", ")

# Only run the functions if this module is run
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
    except Exception as e:
        print("Error: {}".format(e))
