class Student:
    def __init__(self, name, age, classroom, test_results1, test_results2, test_results3,):

        self.name = name
        self.age = age
        self.classroom = classroom
        self.test_results1 = test_results1
        self.test_results2 = test_results2
        self.test_results3 = test_results3

        self.average_grade_mark = test_results1 + test_results2 + test_results3 / 3
        
student1 = Student("Jack", 22, "Classroom B12", 2, 20, 40)
student2 = Student("John", 21, "Classroom B11", 60, 50, 66)



print(student1.name, student1.age, student1.classroom, student1.average_grade_mark)
print(student2.name, student2.age, student2.classroom, student2.average_grade_mark)


class Bird:
    
    class Owl:
        def __init__(self, name, age, colour, habitat):
            self.name = name
            self.age = age
            self.colour = colour
            self.habitat = habitat


    class Dodo:
        def __init__(self, name, age, colour, habitat):
            self.name = name
            self.age = age
            self.colour = colour
            self.habitat = habitat

    owl_1 = Owl("Jack", 7, "Red and Black", "Forests of England")

    dodo_1 = Dodo("Johnny", 15, "Exotic Red/Yellow/Blue", "Jungle")

    print("This bird", owl_1.name, "is", owl_1.age,"years old is", owl_1.colour, "coloured and also lives in the", owl_1.habitat, ".")
    print("This bird", dodo_1.name, "is", dodo_1.age, "years old is", dodo_1.colour, "coloured and also lives/lived in the", dodo_1.habitat,".")




