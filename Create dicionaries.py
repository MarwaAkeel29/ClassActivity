#Exercise 1: Create and Access a Dictionary
Student = {
    "Name": "Alice",
    "Age": 24,
    "Major": "computer science"
}

print("Name:", Student["Name"])
print("Major:", Student["Major"])

#Exercise 2: Add and Update Values
Student["GPA"]= 3.8
Student["Age"]= 25

print(Student)

#Exercise 3: Loop Through a Dictionary
for key, value in Student.items():
    print(f"{key}: {value}")

#Exercise 4: Check if a Key Exists
def check_key(dictionary, key):
    if key in dictionary:
        return "Key exists"
    else:
        return "Key does not exist"

print(check_key(Student, "Name"))  
print(check_key(Student, "Hobbies"))  

#Exercise 5: Count Occurrences
Fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = {}

for Fruit in Fruits:
    if Fruit in word_count:
        word_count[Fruit] += 1
    else:
        word_count[Fruit] = 1

print(word_count)  

#Exercise 6: Merge Two Dictionaries
dict1 = {"a": 1, "B": 2}
dict2 = {"b": 3, "c": 4}

merged_dict = {**dict1, **dict2}
print(merged_dict)

#Exercise 7: Remove Keys
Student.pop("Age", None)
print(Student)

#Exercise 8: Nested Dictionaries
classroom = {
    "Student1": {"Name": "John", "Age": 20},
    "Student2": {"Name": "Emma", "Age": 22}
}
print("Student2 Name:", classroom["Student2"]["Name"])
print("Student1 Age:" , classroom["Student1"]["Age"])

#Exercise 9: Sort a Dictionary
data = {"z": 10, "b": 5, "a": 15}
sorted_by_keys = dict(sorted(data.items()))
print("sorted by keys:", sorted_by_keys)

sorted_by_values = dict(sorted(data.items(),key=lambda item: item[1])) 
print("sorted by values:", sorted_by_values)
    
#Exercise 10: Dictionary Comprehension
squares = {x: x**2 for x in range(1, 6)}
print(squares)


