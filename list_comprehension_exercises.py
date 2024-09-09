# 1. Given a list of numbers, create a new list containing the squares of only the even numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares_of_even = [number ** 2 for number in numbers]
print(squares_of_even)

# 2. Given a list of strings, create a new list containing the length of each string.
words = ["apple", "banana", "cherry", "date"]
word_lengths = [len(word) for word in words]
print(word_lengths)

# 3. Given a list of numbers, create a new list containing only the numbers greater than 5.
numbers = [1, 3, 5, 7, 9]
greater_than_five = [number for number in numbers if number > 5]
print(greater_than_five)

# 4. Given a list of strings, create a new list containing the strings that have more than 4 letters.
words = ["dog", "elephant", "cat", "giraffe"]
long_words = [word if len(word) > 4 else 'less than 4' for word in words]
print(long_words)

# 5. Given a list of numbers, create a new list containing the strings "even" or "odd" depending on whether the number is even or odd.
numbers = [1, 2, 3, 4, 5]
even_odd_labels = ['even' if number % 2 == 0 else 'odd' for number in numbers]
print(even_odd_labels)

# 6. Given a list of strings, create a new list containing the same strings but in uppercase.
words = ["python", "list", "comprehension", "example"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)

# 7. Given a list of strings, create a new list containing the first letter of each string.
words = ["sun", "moon", "star", "sky"]
first_letters = [word[0] for word in words]
print(first_letters)

# 8. Given a list of numbers, create a new list containing these numbers multiplied by 2, but only if the number is odd.
numbers = [2, 3, 4, 5, 6]
doubled_odds = [number ** 2 for number in numbers if number % 2 == 1]
print(doubled_odds)

# 9. Given a list of strings, create a new list containing the length of the string only if the string starts with the letter 'a'.
words = ["apple", "banana", "avocado", "grape"]
lengths_of_a_words = [len(word) for word in words if word[0] == 'a']
print(lengths_of_a_words)

# 10. Given a list of numbers, create a new list containing the strings "small" for numbers less than 5, "medium" for numbers between 5 and 10, and "large" for numbers greater than 10.
numbers = [1, 4, 7, 12, 15, 5]
size_labels = ['small' if number < 5 else 'medium' if number <= 10 else 'large' for number in numbers]
print(size_labels)

# 11. Given a list of words, create a new list containing the words that start and end with the same letter.
words = ["level", "radar", "hello", "world", "madam"]
same_start_end = [word for word in words if word[0] == word[-1]]
print(same_start_end)

# 12. Given a list of numbers, create a new list containing the numbers that are divisible by 3 and greater than 10.
numbers = [3, 9, 12, 15, 18, 22, 24, 30]
divisible_by_3_and_greater_than_10 = [number for number in numbers if number % 3 == 0 and number > 10]
print(divisible_by_3_and_greater_than_10)

# 13. Given a list of strings, create a new list containing the strings that have at least one uppercase letter.
words = ["hello", "WORLD", "Python", "List", "Comprehension", "paPieros"]
strings_with_uppercase = [word for word in words if any(letter.isupper() for letter in word)]
print(strings_with_uppercase)

# 14. Given a list of numbers, create a new list where even numbers are squared, and odd numbers remain unchanged.
numbers = [1, 2, 3, 4, 5, 6]
modified_numbers = [number ** 2 if number % 2 == 0 else number for number in numbers]
print(modified_numbers)

# 15. Given a list of strings, create a new list containing the number of vowels in each string.
words = ["apple", "banana", "cherry", "date"]
vowels = "aeiou"
vowel_counts = [sum(1 for char in word if char in vowels) for word in words]
print(vowel_counts)

# 16. Given a list of numbers, create a new list containing the negative of each number, but only if the number is positive.
numbers = [1, -2, 3, -4, 5]
positive_inverses = [number * -1 for number in numbers if number > 0]
print(positive_inverses)

# 17. Given a list of strings, create a new list containing the strings that are palindromes (read the same forwards and backwards).
words = ["level", "world", "deified", "hello", "radar"]
palindromes = [word for word in words if word[0] == word[-1]]
print(palindromes)

# 18. Given a list of numbers, create a new list containing "True" for numbers that are prime and "False" for the rest.
numbers = [2, 4, 5, 6, 7, 8, 9, 10, 11]
prime_flags = [all(number % i != 0 for i in range(2, int(number ** 0.5) + 1)) and number > 1 for number in numbers]
print(prime_flags)

# 19. Given a list of strings, create a new list containing only the strings that contain at least one digit.
words = ["apple1", "banana", "cherry", "d4te", "d4f1nka"]
strings_with_digits = [word for word in words if any(letter.isdigit() for letter in word)]
print(strings_with_digits)

# 20. Given a list of numbers, create a new list where each number is transformed into its absolute value multiplied by 10.
numbers = [-1, -2, 3, -4, 5]
abs_times_ten = [10 * abs(number) for number in numbers]
print(abs_times_ten)
