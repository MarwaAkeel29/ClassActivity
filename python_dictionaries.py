# 1.Introduction to dictionaries
student = {
    "name": "Alice",
    "age": 20,
    "course": ["Math", "Physics"]
}
print(student)

items = {
    "Title": "Laptop",
    "price": "3000",
    "quanity": "1" 

}
print(items) 

# 2.Creating dictionaries
student_info = {              #using curly braces
    "name": "Bob",
    "age": "Computer Science"
}
print(student_info)

student_info2 = dict(name="Emma", age=22, major="Biology")   #using dict function
print(student_info2)

# 3. Accessing dictionaries elements
student = {
    "name": "Charlie",
    "age": 19,
    "major": "Physics"
}
#Accessing using key
print(student["name"]) #output: Charlie

#Using .get() to access key safely
print(student.get("GPA", "Not Available")) # output: not available

#
student = {
    "name": "Dave",
    "age": 20,
    "major": "Chemistry"
}

#Adding a new key_value pair
student["GPA"] = 3.8

#Modifying an existing key_value pair
student["age"] = 21

#Removing a key_value pair
student.pop("major") 

print(student)