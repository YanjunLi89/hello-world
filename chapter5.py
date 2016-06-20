# a = int(raw_input('a: '))
# b = int(raw_input('b: '))
# c = int(raw_input('c: '))
# n = int(raw_input('n: '))

# def check_fema(a, b, c, n):
# 	if a**n + b**n == c**n:
# 		print('Error')
# 	else:
# 		print('Right')

# check_fema(a, b, c, n)


a = int(raw_input('a: '))
b = int(raw_input('b: '))
c = int(raw_input('c: '))

def is_triangle(a, b, c):
	if a + b >= c:
		if b + c >= a:
			if a + c >= b:
				print('Yes')
			else:
				print('No')
		else:
			print('No')
	else:
		print('No')

is_triangle(a, b, c)

