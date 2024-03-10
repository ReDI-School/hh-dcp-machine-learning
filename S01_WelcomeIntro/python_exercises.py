#%% 1. Write a program to print the Fibonacci sequence up to a given number of terms.

def fibonacci(n):
    pass

print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

#%% 2. Write a function to reverse a given string.
def reverse_string(string):
    pass

print(reverse_string("Hello, World!"))  # Output: !dlroW ,olleH


# %% 3. Write a function to check if a given string is a palindrome.
def is_palindrome(string):
    pass

print(is_palindrome("A man a plan a canal Panama"))  # Output: True
print(is_palindrome("Hello, World!"))  # Output: False

#%% 4. Use list comprehension to generate a list of squares of numbers from 1 to 10.
# print(squares)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#%% 5. Create a class Rectangle with attributes length and width, and methods to calculate the area and perimeter.
class Rectangle:
    pass

rect = Rectangle(5, 3)
print(f"Area: {rect.area()}")  # Output: Area: 15
print(f"Perimeter: {rect.perimeter()}")  # Output: Perimeter: 16

#%% 6. Write a function to count the number of vowels in a given string.
def count_vowels(string):
    pass

print(count_vowels("Hello, World!"))  # Output: 3

#%% 7. Anagram check
# Write a function to check if two given strings are anagrams of each other.
def is_anagram(str1, str2):
    pass

print(is_anagram("listen", "silent"))  # Output: True
print(is_anagram("python", "java"))  # Output: False

#%% 8. Flatten a nested List
# Write a function to flatten a given nested list.
def flatten_list(nested_list):
   pass

nested_list = [1, 2, [3, 4], [[5, 6], [7]], 8]
print(flatten_list(nested_list))  # Output: [1, 2, 3, 4, 5, 6, 7, 8]