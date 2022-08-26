import pandas as pd
import numpy as np
import os

print("Starting the program...\n")
print("The items in the root directory: ", os.listdir())
df = pd.read_csv('6f104bbb5dc80fcbbac2cce23ca18d76.csv')
print("The first 5 records in the table: \n", df.head())
