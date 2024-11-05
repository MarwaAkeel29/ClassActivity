# 1.Basic Tuple Creation
fruits = ("apple", "banana", "cherry") #creating a tuple
print(fruits)

# 2.Accessing Elements
print(fruits[1])
print(fruits[-1])

# 3.Unpacking Tuples
colors = ("red", "green", "blue")
color1, color2, color3 = colors
print(color1)
print(color2)
print(color3)

# 4.Tuple Concatenation
numbers1 = (1, 2, 3)
numbers2 = (4, 5, 6)
numbers_combined = numbers1 + numbers2
print(numbers_combined)

# 5.Tuple Slicing
alphabet = ("a", "b", "c", "d", "e", "f", "g")
print(alphabet[:3])
print(alphabet[-3:])
print(alphabet[::2])

# 6.Tuple Methods
numbers = (1, 2, 2, 3, 4, 4, 4, 5)
print(numbers.count(4))
print(numbers.index(2))

# 7.Nested Tuples
nested = (1, 2, (3, 4), 5)
print(nested[2][1])

# 8.Tuple Membership Testing
colors = ("red", "green", "blue")
print("yellow" in colors)
print("blue" in colors)



