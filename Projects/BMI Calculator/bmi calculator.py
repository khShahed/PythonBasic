

def bmi_app():
	height = input('How tall are you? ')
	weight = input('How much do you weight? ')
	bmi_value = int(weight)/(int(height)/100)**2
	print("Your BMI is: {:.2f}".format(bmi_value))
	if bmi_value < 18.5:
	    print('You\'d better eat more!')
	elif 18.5 <= bmi_value <= 24:
	    print('Good job!')
	else:
	    print('You\'d better do some exercises')

bmi_app()
