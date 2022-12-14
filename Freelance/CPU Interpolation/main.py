import sys
import numpy as np
import pandas as pd


BASENAME = "OUTPUT"

if len(sys.argv) < 2:
    print("No Input FIle Passed")
    exit(0)

input_temps = sys.argv[1]
data_file = input_temps

def parse_raw_temps(f):
    lines = f.readlines()
    result = []
    time = 0
    for line in lines:
        line = line.strip()
        line = line.split(" ")
        result.append((time, line))
        time = time+30
    return result


def writeOutput(filename, data, basename=BASENAME):
    f = open(f"{basename}-{filename}.txt", "w")
    f.write(data)
    f.close()


with open(input_temps, 'r') as temps_file:
    for temps_as_floats in parse_raw_temps(temps_file):
        print(temps_as_floats)

with open(input_temps, 'r') as temps_file:
    # ----------------------------------------------------------------------
    # Split data
    #  for temps_as_floats in parse_raw_temps(temps_file):
    #  time, core_data = temps_as_floats
    #  print(f"{time = } | {core_data = }")
    # ----------------------------------------------------------------------
    for temps_as_floats in parse_raw_temps(temps_file):
        time, core_data = temps_as_floats
        print(f"{time = } | {core_data = }")

with open(input_temps, 'r') as temps_file:
    times = []
    core_0_data = []
    core_1_data = []
    core_2_data = []
    core_3_data = []
    for time, core_data in parse_raw_temps(temps_file):
        times.append(int(time))
        core_0_data.append(float(core_data[0]))
        core_1_data.append(float(core_data[1]))
        core_2_data.append(float(core_data[2]))
        core_3_data.append(float(core_data[3]))

    s = ""
    # core_0
    for i in range(0, len(times)-1):
        interpolation = np.polyfit(times[i:i+1], core_0_data[i:(i+1)], 0)
        try:
            interpolation = np.polyfit(times[i:i+2], core_0_data[i:i+2], 1)
            typ = "interpolation"
        except:
            typ = "least linear"
        s = s + \
            f"{times[i]} <= {times[i+1]};y_{i} =  {round(core_0_data[i],4)} + {round(interpolation[0],4)}x;{typ}\n"
    writeOutput("core-0", s)
    s = ""
    # core_1
    for i in range(0, len(times)-1):
        interpolation = np.polyfit(times[i:i+1], core_1_data[i:(i+1)], 0)
        try:
            interpolation = np.polyfit(times[i:i+2], core_1_data[i:i+2], 1)
            typ = "interpolation"
        except:
            typ = "least linear"
        s = s + \
            f"{times[i]} <= {times[i+1]};y_{i} =  {round(core_1_data[i],4)} + {round(interpolation[0],4)}x;{typ}\n"
    writeOutput("core-1", s)
    s = ""
    # core_2
    for i in range(0, len(times)-1):
        interpolation = np.polyfit(times[i:i+1], core_2_data[i:(i+1)], 0)
        try:
            interpolation = np.polyfit(times[i:i+2], core_2_data[i:i+2], 1)
            typ = "interpolation"
        except:
            typ = "least linear"
        s = s + \
            f"{times[i]} <= {times[i+1]};y_{i} =  {round(core_2_data[i],4)} + {round(interpolation[0],4)}x;{typ}\n"
    writeOutput("core-2", s)
    s = ""
    # core_3
    for i in range(0, len(times)-1):
        interpolation = np.polyfit(times[i:i+1], core_3_data[i:(i+1)], 0)
        try:
            interpolation = np.polyfit(times[i:i+2], core_3_data[i:i+2], 1)
            typ = "interpolation"
        except:
            typ = "least linear"
        s = s + \
            f"{times[i]} <= {times[i+1]};y_{i} =  {round(core_3_data[i],4)} + {round(interpolation[0],4)}x;{typ}\n"
    writeOutput("core-3", s)


# Least Square Regression Approximation
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
