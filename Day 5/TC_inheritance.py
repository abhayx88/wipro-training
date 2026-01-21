class Animal:
    def speak(self):
        print("Animal makes a sound")

class dog(Animal):
    def bark(self):
        print("dog barks")
d=dog()
d.speak()
d.bark()