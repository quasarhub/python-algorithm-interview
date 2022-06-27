import sys

# List Comprehension 
[n for n in range(1, 11) if n % 2 == 1]

# Dictionary Comprehension
original = {'a': 1, 'b': 2, 'c': 3}
a = {key:value for key, value in original.items()}

# range()
a = [n for n in range(1000000)]
b = range(1000000)
print(sys.getsizeof(a))
print(sys.getsizeof(b))

# enumerate()
a = [1, 2, 3, 2, 45, 2, 5]
for i, v in enumerate(a):
    print(i, v)

# divmod()
quotient, remainder = divmod(5, 3)  # (1, 2)

# join()
a = ['A', 'B']
print('@@@@'.join(a))

