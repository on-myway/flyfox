'''
Created on 2018��1��15��

@author: huangl
'''
class Human(object):
    @property
    def id(self):
        return self.__id;
    @id.setter
    def id(self,id):
        self.__id = id;