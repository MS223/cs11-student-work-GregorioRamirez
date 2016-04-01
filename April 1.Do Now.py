a = raw_input("Would you like to quit: ")
while a != "y":
	a = raw_input("Would you like to quit: ")
"""
Prediction: It will run y
Observation: It ran would you like to quit.
 """

a = 0
while a < 100:
	print a
"""
Prediction: It will run 0 until a is greater than 100.
Observation: It kept running 0 and it did not stop.
 """

a = 0
while a < 100:
	a = a + 1
	print a
"""
Prediction: It will run 100 zeros until a is greater than 100.
Observation: It ran 100 zeros until a was greater than 100. 
 """
