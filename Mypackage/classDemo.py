class Person:
    def __init__(self,name):
        self.name = name

    def talk(self):
        print(f" I am {self.name} happy coding")



person1 = Person("spoorthi")
person1.talk()

print(person1.name)