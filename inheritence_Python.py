class human():
    def who1(self):
        print("we are human in common")

class engineers(human):                         # engineer is child of human
    def who2(self):
        print("we are engineers in general")

class AI_engineer(engineers):                    # AI_engineer is child of engineers
    def who3(self):
        print("we are AI engineers also !")

class deep_learner(AI_engineer):                 # deep_learner is child of AI_engineers
    def who4(self):
        print("we study deep learning !")

class andrew(deep_learner):                     # andrew is child of deep_learner
    def who5(self):
        print("hello I am Anderw")

a=andrew()
a.who5()                           # calling function ofandrew class
a.who4()                           # calling function of deep_learner class
a.who3()                           # calling function of AI_enginners class
a.who2()                           # calling function of enginnner class
a.who1()                           # calling function of human class
