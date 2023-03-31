class Animal:
    def __init__(self, name):
        self.name = name
        print("init function activated")

    def run(self):
        print(f"{self.name} is running!")


# a sub class example
class Dog(Animal):
    def bark(self):
        print(f"{self.name}: woof")


if __name__ == '__main__':
    cat1 = Animal("Riki")

