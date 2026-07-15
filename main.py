from decorators import retry, timer
from generators import fibonacci_generator

@retry(max_attempts=3)
@timer
def greet():
    print("Welcome to Advanced Python Library!")

greet()

print("\nFirst 10 Fibonacci Numbers:")

fib = fibonacci_generator()

for _ in range(10):
    print(next(fib))
