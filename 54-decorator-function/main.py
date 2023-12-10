import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(func):
    def wrapper():
        before = time.time()
        func()
        after = time.time()
        print(f"{func.__name__} run speed: {after - before}")
    return wrapper


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


fast_function()
slow_function()


inputs = [1, 2, 3]


def logging_decorator(function):
    def wrapper(*args):
        print(f"You called {function.__name__}{args}")
        result = function(args[0], args[1], args[2])
        print(f"It returned: {result}")
    return wrapper


@logging_decorator
def a_function(a, b, c):
    return a * b * c


a_function(inputs[0], inputs[1], inputs[2])
