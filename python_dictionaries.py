###1. Introduction to dictionaries
#creating  a dictionarry with student details
student = {
    "name": "Alice",
    "age": 20,
    "course": ["Math", "Physics"]
}
print(student)

#creating a dictionary with details about the item
items = {
    "Title": "Laptop",
    "price": "3000",
    "quanity": "1" 

}
print(items) 

###2. Creating dictionaries
# Using dict function
student_info = {              
    "name": "Bob",
    "age": "Computer Science"
}
# Using dict function
student_info2 = dict(name="Emma", age=22, major="Biology")  
print(student_info)
print(student_info2)

###3. Accessing dictionaries elements
student = {
    "name": "Charlie",
    "age": 19,
    "major": "Physics"
}
#Accessing using key
print(student["name"]) #output: Charlie

#Using .get() to access key safely
print(student.get("GPA", "Not Available")) # output: not available

###4. Modifying dictionary elements
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

###5. Dictionary Methods and Operations
student = {
    "name": "Eve",
    "age": 22,
    "major": "Biology"
}

# Using .keys(), .values(), and .items()
print(student.keys())
print(student.values())
print(student.items())

# Looping through a dictionary
for key, value in student.items():
    print(f"{key}:{value}")

# Check if a key exists
if "GPA" in student:       #using if-else statement as there is more than one condition
    print("GPA is:", student["GPA"])
else:
    print("GPA key not found") 

###6. Nesting Dictionaries 
school = {
    "student": {"name": "Alice", "age": 20, "GPA": 3.9},
     "student2": {"name": "Bob", "age": 21, "GPA": 3.6}
}

# Accessing nested dictionary values       
print(school["student"]["name"])
print(school["student2"]["GPA"])

###7. Real-World Application of Dictionaries 
inventory = {
    "item1": {"name": "Laptop", "price": 1200, "stock": 10},
    "item2": {"name": "Smartphone", "price": 800, "stock": 15},
}

# Checking stock for each item
for item_id, details in inventory.items():
    print(f"{details["name"]}: ${details["price"]} - {details["stock"]} in stock")

###8. Class Activity: Building a Contact List
#creating a ditionary with contact details
contact = {
    "name": "Alice",
    "phone": "123-456-7890",
    "email": "alice@example.com"
}   

#adding a new key-value pair
contact["Hometown"] = "London"

#modifying an existing key-value pair
contact["email"] = "alice7878@example.com"

#removing a key-value pair
contact.pop("phone")

print(contact)