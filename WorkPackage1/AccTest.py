import numpy as np; 

print("Test accuracy of python or c? (p/c)")
ans = input()

PythonResult1 = np.loadtxt("./Python/PythonResult1.txt")
PySamples1 = len(PythonResult1)

print("Python Samples 1: ", PySamples1)

TestResult = []
TestSamples = 0

if(ans == 'p'):

	TestResult = np.loadtxt("./Python/PythonResult2.txt")
	TestSamples = len(TestResult)

	print("Python Samples 2: ", TestSamples)
	
elif(ans == 'c'):
	
	TestResult = np.loadtxt("./C/CResults.txt")
	TestSamples = len(TestResult)

	print("C Samples 2: ", TestSamples)

index = 0
if(PySamples1 > TestSamples):
	index = TestSamples
else:
	index = PySamples1

print("Comparing Samples...")
match = 0
for i in range(index):
	if(round(PythonResult1[i],4) == round(TestResult[i],4)):
		match += 1

print("The outputs match at {res}%.".format(res = match/index*100))



