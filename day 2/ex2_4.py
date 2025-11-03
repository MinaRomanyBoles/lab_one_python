# generator that yields lines in reverse order (from end of file).

""" Problem 4: Performance Timer & Logger Decorators
(Decorators - Beginner) """

import time

""" timer Decorator """


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time of {func.__name__}: {end - start} seconds")
        return result
    return wrapper


# Timer decorator
@timer
def slow_function(n):
    time.sleep(n)
    return f"Slept for {n} seconds"

result = slow_function(2)
# Output: [TIMER] Function 'slow_function' executed in 2.0023 seconds
print(result)
# Output: Slept for 2 seconds
def logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(
            f"Function '{func.__name__}' called with args: {args}, kwargs: {kwargs}. Returned: {result}")
        return result
    return wrapper

# Logger decorator
@logger
def add(a, b):
    return a + b

result = add(5, 3)

# Output: Function 'add' called with args: (5, 3), kwargs: {}. Returned: 8
def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        print(
            f"Function '{func.__name__}' has been called {wrapper.call_count} times")
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

# Count calls decorator
@count_calls
def greet(name):
    return f"Hello, {name}!"

def debug(func):
    def wrapper(*args, **kwargs):
        print(f"[DEBUG] Calling '{func.__name__}'")
        print(f"[DEBUG] args: {args}")
        print(f"[DEBUG] kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"[DEBUG] '{func.__name__}' returned: {result}")
        return result
    return wrapper


@debug
def calculate_average(numbers):
    return sum(numbers) / len(numbers)


result = calculate_average([10, 20, 30, 40])


greet("Alice")
greet("Bob")
greet("Charlie")
print(f"Total calls: {greet.call_count}")