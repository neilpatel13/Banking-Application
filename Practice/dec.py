def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

@do_twice #calling the decorator
def say_hello():
    print("Hello")

say_hello()

@do_twice
def say_hello(name):
    print(f"Hello {name}")
say_hello("Neil")
