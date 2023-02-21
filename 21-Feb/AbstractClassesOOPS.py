from abc import ABC, abstractclassmethod
''''
Method #1
Abstract Class and can't make objects for this class
'''


class Animals(ABC):
    @abstractclassmethod
    def num_legs(self):
        pass


class Humans(Animals):
    def num_legs(self):
        print('I Have 2 Legs')


H = Humans()
H.num_legs()


'''
Method #2
Using Subclassing
'''


class Polygon():
    def num_sides(self):
        pass


class Square(Polygon):
    def num_sides(self):
        print('I Have 4 sides')
