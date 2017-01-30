# -*- coding: utf-8 -*-

while True:
	fahrenheit = input("Enter a temperature you would like converted into Celsius!: ")
	if fahrenheit and str.isnumeric(fahrenheit):
		fahrenheit = float(fahrenheit)
		celsius = (fahrenheit - 32) / 1.8
		print("{}°F = {:.2f}°C".format(fahrenheit, celsius))
		break

	else:
		print("You did not type a number! Please Try again.")
		continue