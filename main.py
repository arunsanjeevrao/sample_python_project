import pandas as pd
import numpy as np
import os

print("Starting the program...\n")
print("The items in the root directory: ", os.listdir())
df = pd.read_csv('9cfb1200eb45d829f4af96480a118238.csv')
print("The first 5 records in the table: \n", df.head())

# New features
print("The Number of Records in the table: ", len(df))
print("\nSummary Statistics: \n\n", df.describe())