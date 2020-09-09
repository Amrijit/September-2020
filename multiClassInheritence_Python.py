# generalaization 

class student():
    def occupation_std(self):
        print("we do study ")

class engineer():
    def occupation_eng(self):
        print("we do innovation !")

class doctor():
    def occupation_doc(self):
        print("we save lifes !")

class human(student,engineer,doctor):
    def occupation(self):
        print("Human can be student , engineer or  doctor ")

h=human()
h.occupation()
h.occupation_std()
h.occupation_eng()
h.occupation_doc()
