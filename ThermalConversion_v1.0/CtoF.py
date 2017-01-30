# -*- coding: utf-8 -*-

while True:
	celsius = input("Enter a temperature you would like converted into Fahrenheit!: ")
	if celsius and str.isnumeric(celsius):
		celsius = float(celsius)
		fahrenheit = 9.0/5.0 * celsius + 32
		print("{}°C = {:.2f}°F".format(celsius, fahrenheit))
		break

	else:
		print("You did not type a number! Please Try again.")
		continue