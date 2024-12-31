# Q.1 Write a decorator that measures the time a function takes to execute.
import time


def timer(func):
    def wrapper(*args, **kwargs):
        func_start_time = time.time()
        result = func(*args, **kwargs)
        func_end_time = time.time()

        print(f"{func.__name__} ran in {func_end_time - func_start_time:.0f}s time")
        return result

    return wrapper


@timer
def example_func(n):
    time.sleep(n)


example_func(1)


# Q.2 Create a decorator to print the function name and the values of its arguments every time the function is called.
def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ", ".join(str(arg) for arg in args)
        kwargs_value = ", ".join(f"{key}: {value}" for key, value in kwargs.items())
        print(
            f"calling {func.__name__} with args {args_value} and kwargs {kwargs_value}"
        )
        return func(*args, **kwargs)

    return wrapper


@debug
def greet(name, greeting="👋"):
    return f"{greeting} {name}"


print(greet("Milan"))


# Q.3 Implement a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function.
def cache(func):
    cached_value = {}

    def wrapper(*args):
        if args in cached_value:
            return cached_value[args]
        result = func(*args)
        cached_value[args] = result
        return result

    return wrapper


@cache
def long_running_func(a, b):
    time.sleep(10)
    return a + b


print(long_running_func(10, 14))
print(long_running_func(10, 14))
