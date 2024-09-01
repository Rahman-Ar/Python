#Decorators
def my_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

@my_decorator
def my_function():
    print("Hello, World!")

my_function()

#UseCase
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} and {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def add(x, y):
    return x + y

add(3, 5)

#Generator
def my_generator():
    yield 1
    yield 2
    yield 3
gen = my_generator()
for value in gen:
    print(value)

#UseCase
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci()
for _ in range(10):
    print(next(fib_gen))
