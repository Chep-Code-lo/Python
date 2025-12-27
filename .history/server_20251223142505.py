class Dog:

    def walk(self):

        return "*walking*"

    def speak(self):

        return "Woof!"

class JackRussellTerrier(Dog):

    def speak(self):

        return "Arff!"

bobo = JackRussellTerrier()

print(bobo.walk())