import numpy as np
import scipy as sp
import pandas as pd

# Read csv as pandas dataframe
def generate_vif(csv):
    """Prints the Variance Inflation Factor (VIF) for the values in a given csv."""
    # Create pandas dataframe from csv.
    data = pd.read_csv(csv)
    # Calculate VIF from dataframe.
    cc = sp.corrcoef(data.values, rowvar=False)
    vif = np.linalg.inv(cc)
    v = vif.diagonal()
    return str(v)
