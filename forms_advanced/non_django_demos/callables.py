class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __call__(self, *args, **kwargs):
        pass


p = Person('Mike', 25)

print(p)
print(p())
# IF we DO NOT overwrite '__call__' method -> Return: TypeError: 'Person' object is not callable
# IF we overwrite it -> Return: None
