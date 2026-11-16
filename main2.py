from mathutils.basic import add, sub, multiply, div
from mathutils.number import prime, armstrong, palindrome
from mathutils.statsics import mean, maximum, minimum

print("Addition:", add(10, 5))
print("Subtraction:", sub(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", div(10, 5))

n = 153

print("Prime:", prime(n))
print("Armstrong:", armstrong(n))
print("Palindrome:", palindrome(n))

numbers = [10, 20, 30, 40, 50]

print("Mean:", mean(numbers))
print("Maximum:", maximum(numbers))
print("Minimum:", minimum(numbers))