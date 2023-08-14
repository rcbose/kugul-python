print ( 'hi' )
fruits = ['apple', 'banana', 'orange', 'grape']

print(fruits[0]) 
print(fruits[2]) 
numbers = [1, 2, 3, 4, 5]
print(numbers)
a = 20
b = a
print (a)
numbers = list(range(1, 11))
print(numbers)

keys = ['name', 'age', 'city']
values = ['kogul', 21, 'arupukottai']

data = dict(zip(keys, values))
print(data)

fruits_tuple = ('apple', 'banana', 'orange')

print(fruits_tuple[0]) 
print(fruits_tuple[2])  
fruits_tuple = ('apple', 'banana', 'orange')

fruit1, fruit2, fruit3 = fruits_tuple

print(fruit1) 
print(fruit2)  
print(fruit3)  

fruits_tuple = ('banana', 'orange')

length = len(fruits_tuple)
print(length) 
# Swap variables using a temporary variable
a = 10
b = 20

# Swapping values
temp = a
a = b
b = temp

print("a:", a)  # Output: a: 20
print("b:", b)  # Output: b: 10
# Swap variables without using a temporary variable or tuple unpacking (using bitwise XOR)
x = 10
y = 20

# Swapping values
x = x ^ y
y = x ^ y
x = x ^ y

print("x:", x) 
print("y:", y) 

a = 10 
b = 5   
result_and = a & b
print("Bitwise AND:", result_and)  

result_or = a | b
print("Bitwise OR:", result_or)   

result_xor = a ^ b
print("Bitwise XOR:", result_xor) 

result_left_shift = a << 2
print("Left Shift of a by 2:", result_left_shift)

result_right_shift = a >> 2
print("Right Shift of a by 2:", result_right_shift) 

print(list(['bose','ran','kogul','bose']))

import math

number = 25
square_root = math.sqrt(number)

print("Square root of", number, "is:", square_root)

floating_number = 7.8
floor_value = math.floor(floating_number)

print("Floor value of", floating_number, "is:", floor_value)
x = int(input("Enter 1st number"))
y = int(input("Enter 2nd number"))
z = x + y
print (z)
ch = input('enter a char')[0]
print (ch)

import math

# Calculate the square root of a number
number = 25
square_root = math.sqrt(number)

print("Square root of", number, "is:", square_root)

floating_number = 7.8
floor_value = math.floor(floating_number)

print("Floor value of", floating_number, "is:", floor_value)

def add_numbers(a, b):
    return a + b

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = add_numbers(num1, num2)

print("The sum of", num1, "and", num2, "is:", result)

age = 15
if age >= 18:
    print("You are an eligible")
else:
    print("You are a not eligible")

score = 85
if score >= 90:
    print("You got an A.")
elif score >= 80:
    print("You got a B.")
elif score >= 70:
    print("You got a C.")
else:
    print("You need to improve.")
