#!/usr/bin/python

def decorator(self):
    print "bar"

def decorator(cls):
    cls.bar = func
    return cls


@decorator       ### ======> F = decorator(F)
class Foo():
    pass

foo = Foo()
foo.bar()
