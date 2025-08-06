def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()



# Example 2

def log_arguments(func):
    def wrapper(x, y):
        print(f"Arguments: x={x}, y={y}")
        return func(x, y)
    return wrapper

@log_arguments
def add(x, y):
    return x + y

result = add(5, 3)
print("Result:", result)