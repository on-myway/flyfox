from com.flyfox.py.demo.Human import Human;

class Student(Human):#继承Human类
#     def __init__(self,name,age,score):
#         self.__name = name;
#         self.__age = age;
#         self.__score = score;
    
    @property
    def name(self):
        return self.__name;
    @name.setter
    def name(self, name):
        self.__name = name;
    
    def setAge(self,age):
        self.__age = age;
    def getAge(self):
        return self.__age;
    
    def setScore(self,score):
        self.__score = score;
    def getScore(self):
        return self.__score;