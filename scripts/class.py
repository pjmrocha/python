
class Person:
    def __init__ (self, name, age):
        self.name=name
        self.age=age

class Superhero(Person):
    def __init__ (self, name, age, superpower):
        Person.__init__(self, name, age)
        self.superpower=superpower

p = Person("Mike", 21)

print p
print p.name
print p.age

h = Superhero("Superman", 99, "Fly")

print h.superpower
print h.name
