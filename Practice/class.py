class Person:
    name= "Bob"
    age = 50
    job = "Painter"
    def __init__(self) -> None:
        self.name = "Matt"
        self.age= 32
        self.job="Lecturer"
    def __repr__(self) -> str:
        return str(self.__dict__)
person = Person()
#print(f"{person}")
#print(f"{person}") #shows memory location
#print(f"{Person.__dict__}")
person.course = "IS601"
#del person.course
print(f"{person}")

