#number = int(input("Enter a number:"))
#while number >=0:
 #   print(number)
 #   number -= 1

n = 0
while n < 5:
    print(f"number is:  {n}")
    n += 1

for i in range(1, 11, 3):    
  print(i)

total = 0
for i in range(1, 6):
   total += i
print("sum:", total) 

text = input("enter a string: ")
for char in text:
   print(char)

num = int(input("enter a number:"))  
for i in range (1,11) :
   print(f"{num} x {i} = {num * i}")

numbers = [ 3, 5, 7, 9, 11]   
total = 0
for num in numbers:
   total += num
print("Sum of list elements:", total)   

for i in range (1,51,2):
   print(i)

#numbers = [12, 4, 56, 17, 8] 
minimum = numbers[0] 
for num in numbers:
   if num < minimum:
      minimum = num
print("minimum value:", minimum)   

import random
target = random.radient(1, 50)
guess = None 
while guess != target:
   guess = int (input("guess a number between 1 and 50"))
   if guess < target:
      print ("too low!")
   elif guess > target:
      print("too high")  
print("correct! you guessed the number.")       