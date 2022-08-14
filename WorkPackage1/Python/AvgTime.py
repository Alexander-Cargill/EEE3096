import numpy as np

a = list()

with open("PythonTime.txt") as f:
	while True:
		line = f.readline()
		if not line:
			break
		print(line[20:])
		a.append(float(line[20:]))


a = np.array(a)
print("Samples: ", len(a))
print("Mean: ", np.mean(a))
print("Standard Deviation: ", np.std(a))
