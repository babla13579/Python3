#!/usr/bin/env python3

# Fibonnacci Number Generator
a, b = 0, 1
while ( a < 300 ):
  print(a, end=',')
  a, b = b, a+b

# Exponent and print
i=256**2
print("\n\n\nThe value of i is ", i)

# if elif else -- Integer comparison
# x = int(input("Please enter a integer: "))
x = 0
if x < 0:
	x=0
	print("negative changed to 0")
elif x == 0:
	print('0')
elif x == 1:
	print("one")
else:
	print("more")

# Iterate over a list
words = ['cat', 'windows', 'night']
for w in words:
	print(w, len(w))

# How To -- Modify collection during iteration
users = {'mel': 'active', 'thomas': 'inactive', 'mydick': 'inactive'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
	if status == 'inactive':
		del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
	if status == 'active':
		active_users[user] = status

# range() function
print('\nrange function')
for i in range(5):
	print(i, end=",")
print()
print(list(range(5, 10)))
print(list(range(0, 10, 3)))
print(list(range(-10, -100, -30)))
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
	print(i, a[i])
# print(range(0, 10))   # This doesn't work... I do not currently know why.
print(sum(range(4)))

# Nested Looping -- Prime Numbers
for n in range(2, 10):
	for x in range(2, n):
		if n % x == 0:
			print(n, 'equals', x, '*', n//x)
			break
	else:
		# loop fell through without finding a factor
		print(n, 'is a prime number')

# Modulus and continue
print("\n\n")
for num in range(1,10):
	if num % 2 == 0:
		print(num, "is even")
		continue
	print(num, "is odd")

# https://docs.python.org/3/tutorial/controlflow.html
