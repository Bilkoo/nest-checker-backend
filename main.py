import random

def generate_random_numbers(count=10, min_val=1, max_val=100):
    return [random.randint(min_val, max_val) for _ in range(count)]

def fibonacci(n):
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def reverse_string(s):
    return s[::-1]

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def count_vowels(s):
    return sum(1 for char in s.lower() if char in "aeiou")

def sort_numbers(arr):
    return sorted(arr)

def find_max(arr):
    return max(arr)

def find_min(arr):
    return min(arr)

def calculate_mean(arr):
    return sum(arr) / len(arr)

def calculate_median(arr):
    arr.sort()
    mid = len(arr) // 2
    return arr[mid] if len(arr) % 2 != 0 else (arr[mid - 1] + arr[mid]) / 2

def is_palindrome(s):
    return s == s[::-1]

def generate_matrix(rows=3, cols=3, min_val=1, max_val=10):
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))

def flatten_matrix(matrix):
    return [num for row in matrix for num in row]

def count_occurrences(arr, value):
    return arr.count(value)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def unique_elements(arr):
    return list(set(arr))

def main():
    numbers = generate_random_numbers()
    print("Random Numbers:", numbers)
    print("Fibonacci Sequence:", fibonacci(10))
    print("Prime Check (17):", is_prime(17))
    print("Reversed String:", reverse_string("Hello World"))
    print("Factorial (5):", factorial(5))
    print("Sorted Numbers:", sort_numbers(numbers))
    print("Max Number:", find_max(numbers))
    print("Min Number:", find_min(numbers))
    print("Mean:", calculate_mean(numbers))
    print("Median:", calculate_median(numbers))
    print("Vowel Count in 'Cryptography':", count_vowels("Cryptography"))
    print("Is 'racecar' a palindrome?", is_palindrome("racecar"))
    
    matrix = generate_matrix()
    print("Matrix:", matrix)
    print("Transposed Matrix:", transpose_matrix(matrix))
    print("Flattened Matrix:", flatten_matrix(matrix))
    
    print("GCD of 48 and 18:", gcd(48, 18))
    print("LCM of 48 and 18:", lcm(48, 18))
    print("Unique Elements:", unique_elements(numbers))

if __name__ == "__main__":
    main()
