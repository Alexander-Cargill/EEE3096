import numpy as np

a = list()

with open("CTime.txt") as f:
	while True:
		line = f.readline()
		if not line:
			break
		print(line)
		if(line[0] == 'T'):
			a.append(float(line[5:-4]))


a = np.array(a)
print("Samples: ", len(a))
print("Mean: ", np.mean(a))
print("Standard Deviation: ", np.std(a))
