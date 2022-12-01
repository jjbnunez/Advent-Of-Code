"""
Day 1: Calorie Counting

Solution written by JJ Nunez.
"""

file = open('input.txt', 'r', encoding="utf-8")

lines = file.readlines()

subbed = []
for sub in lines:
	subbed.append(sub.replace('\n',''))

sums = []
sum = 0
for sub in subbed:
	if sub != '':
		sum += int(sub)
	else:
		sums.append(sum)
		sum = 0

print("Highest calorie sum is", max(sums))

copy = sums.copy()

first = max(copy)

copy.remove(first)

second = max(copy)

copy.remove(second)

third = max(copy)

print("First biggest calorie sum is", first)
print("Second biggest calorie sum is", second)
print("Third biggest calorie sum is", third)
print("Total sum of calories among top three is", first + second + third)