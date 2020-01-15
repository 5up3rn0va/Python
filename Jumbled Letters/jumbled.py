n = int(input("Enter number of test cases: "))

for i in range(n):
	sen = input("Enter sentence: ")
	sen = sen.replace(" ", "")
	even = "".join(reversed(sen[::2]))
	odd = sen[1::2]
	print(odd+even)
