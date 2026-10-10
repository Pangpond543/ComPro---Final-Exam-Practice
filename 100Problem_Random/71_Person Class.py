class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_name(self) -> str:
        return self.name

    def get_age(self) -> int:
        return self.age

    def set_name(self, name: str) -> None:
        self.name = name

    def set_age(self, age: int) -> None:
        self.age = age
    
person1 = Person("Pond", 18)
person2 = Person("boss", 19)

print(person1.get_name())
print(person1.get_age())

person1.set_age(20)

print(person1.get_age())

print(person2.get_age())