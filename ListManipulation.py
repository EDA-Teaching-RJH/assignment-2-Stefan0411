numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
numbers.sort()

numbers = list(set(numbers))

numbers.extend([7, 8])

print(numbers)
