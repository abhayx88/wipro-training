class animal:
    def sound(self):
        print("animal sound")
class dog(animal):
    def sound(self):
        print("dog barks")

class cat(animal):
    def sound(self):
        print("cat meows")
obj=[dog(),cat()]

for a in obj:
    a.sound()