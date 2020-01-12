from operator import itemgetter

n = int(input("Enter number of subjects: "))
m = int(input("Enter number of students: "))

students = []
for i in range(m):
	students.append(list(input("Enter student name along with marks: ").split()))

ranks = []
fail = []
for j,s in enumerate(students):
	s = [int(a) for a in s[1:]]
	
	if any(b < 40 for b in s):
		fail.append(j)
	else:
		avg = sum(s[0:])/n
		ranks.append([j,avg])

ranks.sort(key = itemgetter(1), reverse = True)

for r, i in enumerate(ranks, 1):
	print(students[i[0]][0], r)

for i in fail:
	print(students[i][0], "FAIL")
