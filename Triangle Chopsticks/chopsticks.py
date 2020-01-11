def check(a, b, c):
	if (a + b <= c) or (b + c <= a) or (c + a <= b):
		return False
	else:
		return True

n = int(input("Enter number of test cases: "))

for i in range(n):
	a, b, r = [int(x) for x in input("Enter a, b, r: ").split()]
	num = int(input("Enter number of chopsticks in jar: "))
	leng = list(map(int, input("Enter lengths of chopsticks in jar: ").split())) 

	cnt = 0
	for l in leng:
		if check(a, b, l):
			cnt += 1

	print("\nNumber of triangles possible: ", cnt)

	if cnt > r:
		print("Winner: Natsu")
	else:
		print("Winner: Grey")
