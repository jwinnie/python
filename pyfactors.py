
# Python code created (almost) from scratch by Jeremy Potter

def find_factors(*x):
	factor_list = []
	for x in x:
		for n in range(1,x+1):
			if x % n == 0:
				factor_list.append(n)
	return factor_list

def find_common_factors(*args):
	common_factor_list = []
	all_factors = find_factors(*args)
	for n in all_factors:
		if all_factors.count(n) > 1:
			common_factor_list.append(n)
	return sorted(list(set(common_factor_list)))

# This is a simulation of the "cake method".
def lcm(x,y):
	numbers_to_multiply = []
	for n in find_common_factors(x,y):
		if x%n == 0 and y%n == 0:
			numbers_to_multiply.append(n)
			x/=n; y/=n
		else:
			break
	numbers_to_multiply.extend([x,y])
	output = 1
	for x in numbers_to_multiply:
		output *= x
	return output

def gcf(*x):
	return max(find_common_factors(*x))

def is_prime(x):
	if find_factors(x) == [1,x]:
		return True
	else:
		return False
