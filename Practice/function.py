def myFunc():
    print("this is my awesome function")
#myFunc()

#tuples (*)
def myFunc2(*args):
    print(f"{args}")
#myFunc2(5, "+", 5)

#key value pairs (**)
def myFunc3(**args):
    print(f"{args}")
#myFunc3(name ="Bob", age=50, job="Painter")

#default values
def myFunc4(name = "world"):
    print(f"Hello, {name}")
#myFunc4("name")
#myFunc4(name="Matt")

def myFunc5(val, name = "world"):
    print(f"Hello, name: {name} val: {val}")
#myFunc5("matt")
#myFunc5("matt", "matt")
#myFunc5(None)

def findPrime(num):
    pass
