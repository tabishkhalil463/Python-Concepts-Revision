# Normal function
def square(x):
    return x * x

# Lambda version
square_lambda = lambda x: x * x

print("Square using lambda:", square_lambda(5))


# Example 2

names = ["Ali", "Zara", "Ahmed", "Bilal"]
sorted_names = sorted(names, key=lambda name: len(name))
print("Names sorted by length:", sorted_names)