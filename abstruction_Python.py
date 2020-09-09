from abc import ABC, abstractclassmethod
class human(ABC):
    def name(self):
        pass

class john(human):
    def name(self):
        print("my name is john!")

class mike(human):
    def sound(self):
        print("my name is mike")

class bella(human):
    def name(self):
        print("my name is bella")


j=john()
m=mike()
b=bella()

j.name()
m.name()
b.name()




