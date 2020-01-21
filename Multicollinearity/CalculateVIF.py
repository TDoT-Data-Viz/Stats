import numpy as np
import scipy as sp
import pandas as pd

# Read csv as pandas dataframe
data = pd.read_csv(r"path\table.csv", header=0)

# Convert dataframe columns to lists
var1 = list(data.VAR1) # VAR1 in this case would be the heading for the column
var2 = list(data.VAR2)

# Add new variables for each column to be compared. columns with identical numbers, or numbers that are 
# multiples of another column (e.g. VAR2 = VAR1 * 2) will return a 'singular matrix' error.


# Calculate VIF from lists
ck = np.column_stack([var1, var2])
cc = sp.corrcoef(ck, rowvar=False)
vif = np.linalg.inv(cc)
v = vif.diagonal()
print(v)


