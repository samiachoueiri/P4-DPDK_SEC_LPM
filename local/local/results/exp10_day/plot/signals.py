import numpy as np


# Load and process data1
data1 = np.loadtxt("5min_out.txt")
data2 = np.loadtxt("day_20240619_12_out.txt")
data3 = np.loadtxt("day_20250409_out.txt")

def process_data(data):
    time = data[:, 0]
    actual = data[:, 3] / 1000
    predicted = data[:, 4] / 1000
    allowed = data[:, 5] / 1000
    return (
        time[:-1],
        actual[:-1],
        predicted[1:],
        allowed[1:]
    )

time1, actual1, predicted1, allowed1 = process_data(data1)
last_5_actual = actual1[-5:]
last_5_predicted = predicted1[-5:]
last_5_allowed = allowed1[-5:]
actual1 = np.concatenate((actual1, last_5_actual, last_5_actual))
predicted1 = np.concatenate((predicted1, last_5_predicted, last_5_predicted))
allowed1 = np.concatenate((allowed1, last_5_allowed, last_5_allowed))
time1 = list(range(len(actual1)))
time1 = [i / 60 for i in range(len(actual1))]
xtickss = range(0, int(time1[-1]) + 1, 1)
time_o = [(i-1)/ 60 for i in range(len(actual1))]


time2, actual2, predicted2, allowed2 = process_data(data2)
last_20_actual = actual2[-20:]
last_20_predicted = predicted2[-20:]
last_20_allowed = allowed2[-20:]
actual2 = np.concatenate((actual2, last_20_actual, last_20_actual))
predicted2 = np.concatenate((predicted2, last_20_predicted, last_20_predicted))
allowed2 = np.concatenate((allowed2, last_20_allowed, last_20_allowed))
time2 = list(range(len(actual2)))
time2 = [i / 3600 for i in range(len(actual2))]
xtickshh = range(0, int(time2[-1]) + 1, 1)
time_o2 = [(i-1)/ 3600 for i in range(len(actual2))]

time3, actual3, predicted3, allowed3 = process_data(data3)
last_900_actual = actual3[-900:]
last_900_predicted = predicted3[-900:]
last_900_allowed = allowed3[-900:]
actual3 = np.concatenate((actual3, last_900_actual, last_900_actual))
predicted3 = np.concatenate((predicted3, last_900_predicted, last_900_predicted))
allowed3 = np.concatenate((allowed3, last_900_allowed, last_900_allowed))
time3 = list(range(len(actual3)))
time3 = [i / 3600 for i in range(len(actual3))]
xticksh = range(0, int(time3[-1]) + 1, 1)
time_o3 = [(i-1)/ 3600 for i in range(len(actual3))]

mean_data1 = np.mean(actual1)
mean_data2 = np.mean(actual2)
mean_data3 = np.mean(actual3)
print(f"mean1: {mean_data1}")
print(f"mean2: {mean_data2}")
print(f"mean3: {mean_data3}")

std_data1 = np.std(actual1)
std_data2 = np.std(actual2)
std_data3 = np.std(actual3)
print(f"STD1: {std_data1}")
print(f"STD2: {std_data2}")
print(f"STD3: {std_data3}")

var_data1 = np.var(actual1)
var_data2 = np.var(actual2)
var_data3 = np.var(actual3)
print(f"VAR1: {var_data1}")
print(f"VAR2: {var_data2}")
print(f"VAR3: {var_data3}")