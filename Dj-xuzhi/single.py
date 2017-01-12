#!/usr/bin/python

class Singleton(object):
    def __new__(cls,*args,**kw):
        if not hasattr(cls,'_instance'):
            orig = super(Singleton,cls)
            cls._instance = ofig.__new__(cls,*args,**kw)
        return cls,_instance

class Myclass(Singleton):
    a = 1

one = Myclass()
two = Myclass()

print id(one)
print id(two)

one.a = 3
print one.a
print two.a  
