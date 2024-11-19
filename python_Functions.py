#Exercise 1: Greet a User
def greet_user(name):
     "Greets the user with their name."
     return f"Hello, {name}! Welome to Python programing."
print(greet_user("Marwa"))

#Exercise 2: Add Two Numbers
def add_numbers(num1, num2):
    "Adds two numbers and returns the result."
    return num1 + num2 
print(add_numbers(4, 9))

#Exercise 3: Check Even or Odd
def check_even_odd(number):
    "Checks if a number is even or odd."
    return "Even" if number % 2 == 0 else "Odd"
print(check_even_odd(17))
print(check_even_odd(26))

#Exercise 4: Find the Largest Number
def find_largest(num1, num2, num3):
    "Finds and returns the largest of three numbers."
    return max(num1, num2, num3)
print(find_largest(67, 99, 108))

#Exercise 5: Calculate Factorial
def calculate_factorial(n):
    "Calculates the factorial of a number."
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial 
print(calculate_factorial(7))  

#Exercise 6: Reverse a String
def reverse_string(text):
    "Reverses the input string."
    return text[::-1]
print(reverse_string("Python"))

#Exercise 7: Check Prime Number
def is_prime(number):
     "Checks if a number is prime."
     if number < 2:
         return False
     for i in range(2, int(number ** 0.5) + 1):
         if number % i == 0:
             return False
     return True
print(is_prime(9))   
print(is_prime(22)) 

#Exercise 8: Count Vowels in a String
def count_vowels(text):
    "Counts the number of vowels in the input string."
    vowels = "aeiouAEIOU"
    count = 0 
    for char in text:
        if char in vowels:
            count += 1
    return count   
print(count_vowels("I love a cup of Tea"))

#Exercise 9: Find the Maximum in a List
def find_max_in_list(numbers):
    "Finds the maximum number in a list."
    return max(numbers)
print(find_max_in_list([5, 7, 8, 9, 6]))

#Exercise 10: Convert Temperature
def convert_temperature(temperature, scale):
    "Converts temperature between Celsius and Fahrenheit."
    if scale == "C":
        return (temperature * 9/5) + 32  # Celsius to Fahrenheit  
    elif scale == "F":
        return (temperature - 32) * 5/9  # Fahrenheit to Celsius
    else:
        return "Invalid sale"
    
print (convert_temperature(0, "C"))   # Celsius to Fahrenheit
print (convert_temperature(32, "F"))  # Fahrenheit to Celsius

#class activity-calulate the average marks
def average_marks(         #Find's the average marks in the list.
        marks1,
        marks2,
        marks3,
        marks4
    ):
    marks = (marks1+marks2+marks3+marks4)
    average = (marks/4)
    return average
print(average_marks(88,88,99,67))
print(average_marks(30,77,49,34))







    





  






