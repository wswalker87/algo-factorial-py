import functools

def factorial(num):
	## factorial for 6! = 6*5*4*3*2*1 or 6 *5! (six times the previous factorial) 6*5=30, 30*4=120, 120*3=360, 360*2=720, 720*1=720
	# Figure out the factorial for 1 and you can get all the others
	# classic for loop
	# list_of_nums_to_check = list(range(num, 0, -1)) # make the list

	# prod = 1 # init the var

	# for current_item in list_of_nums_to_check:
	# 	prod = prod * current_item
	# return prod
	#
	list_of_nums_to_check = list(range(num, 0, -1))
	# set prod to equal the aggregrate of the lambda. Iterate over the list that I made (the last arg) and multiply it with the agg * current item and use
	prod = functools.reduce(lambda agg, current_item : agg * current_item, list_of_nums_to_check)
	return prod


	

print(factorial(7))
print(factorial(6))
print(factorial(5))
print(factorial(4))
print(factorial(3))
print(factorial(2))
print(factorial(1))