import random
def main():
	solved = False
	while solved == False:
		a = (random.randint(0, 2) / random.randint(1, 10))
		b = (random.randint(0, 2) / random.randint(1, 10))
		c = (random.randint(0, 2) / random.randint(1, 10))
		d = (random.randint(0, 2) / random.randint(1, 10))
		e = (random.randint(0, 2) / random.randint(1, 10))
		f = (random.randint(0, 2) / random.randint(1, 10))

		if (a + b + c + d + e + f == (12/13)):
			solved = True

main()
