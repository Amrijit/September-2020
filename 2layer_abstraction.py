from abc import ABC,abstractclassmethod
class human(ABC):
    def occupation(self):
        pass

class engineer(human):
    def occupation(self):
        print("we are engineers !")
    def type_of_engineer(self):
        pass

class ML_enginner(engineer):
    def type_of_engineer(self):
        print("I develop AI applications !")
    def sector(self):
        pass

class deep_learner(ML_enginner):
    def sector(self):
        return super().sector()


m=ML_enginner()
m.occupation()
m.type_of_engineer()
