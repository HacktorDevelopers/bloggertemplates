class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def changeName(self, name, newName):
        if name == self.name:
            self.name = newName
        else:
            print("Old name is not correct !")

    def set_pin(self, pin):
        self.pin = pin

    def changepin(self, old_pin, new_pin):
        if self.pin == old_pin:
            self.pin = new_pin
        else:
            print("Incorrect pin !")


def Main():
    print("We are about to create a person")
    name = input("Input Name: ")
    age = input("Input age: ")

    newPerson = Person(name, age)

    print(newPerson.name)

    print("We are about to change name")
    oldName = input("Input Old Name: ")
    newName = input("Input new Name: ")
    newPerson.changeName(oldName, newName)
    print(newPerson.name)

if __name__ == "__main__":
    Main()
