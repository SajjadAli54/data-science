import numpy as np
import pandas as pd
import sys

BASENAME = "OUTPUT"

if len(sys.argv) < 2:
    print("No Input FIle Passed")
    exit(0)

data_file = sys.argv[1]


def transform(X):
    return np.array([[1, x] for x in X])

def fit(X, y):
    X_transform = transform(X)
    X_transpose = np.transpose(X_transform)
    XtX = np.dot(X_transpose, X_transform)
    XtX_inverse = np.linalg.inv(XtX)
    XtY = np.dot(X_transpose, y)
    
    bias, slope = np.dot(XtX_inverse, XtY)
    bias = np.round(bias, 3)
    slope = np.round(slope, 3)

    return bias, slope
        
table = pd.read_table(data_file, sep=" ", header=None)
X = table.iloc[:, :3]
y = table.iloc[:, 3]

slope, bias = 0, 0

for i in range(3):
    values = fit(X[0], y)
    bias += values[0]
    slope += values[1]
slope /= 3
bias /= 3
print(f"Slope = {slope}, Interecpt = {bias}")

