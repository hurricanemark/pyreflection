#!/usr/bin/python
#-------------------------------------------------------------------------------------------------------
# introspection is the most important feature that set python apart
# this little program demonstrates the type checking (look back) that 
# is inherently one of the strong suite in Python
#-------------------------------------------------------------------------------------------------------
""" Testing python reflection with its ability to find out about type, class, attributes and methods of an object. """

import types, re, MySQLdb
import inspect,  sys

""" sample implementation of type checking for pass-in index of a list"""
from types import *
def delete(mylist, item):
    if type(item) is IntType:   #type checking param#2
       del mylist[item]
    else:
       mylist.remove(item)
       
def erase(mylist, item):    
    if isinstance(item, int):    #alternative way of type checking
       del mylist[item]
    else:
       mylist.remove(item)
       



#-------------------------------------------------------------------------------------------------------
# this outputs the list of builtin objects and functions:
# ['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
#-------------------------------------------------------------------------------------------------------
print(dir(__builtins__))

#--------------------------------------------------------------------------------------------------------
# while loop shoud exit with status zero if all tests in wile loop are true
#--------------------------------------------------------------------------------------------------------
try:    
    chk = True
    while   (chk == True):
        chk=type(__doc__) is None
        chk=type(__package__) is None
        chk=type(__spec__) is None
        chk=type(__loader__) is None
        
        chk=type(__file__) is str
        chk=type(__name__) is str
        chk=type(False) is bool
        chk=type(3) is int
        chk=type(set) is set
        chk=type(3.0) is float
        chk=type(10**10) is int       #is long in python2
        chk=type(1 + 1) is complex
        chk=type('mark') is str
        chk=type([1,4]) is list
        chk=type([1,(4,'mark')]) is list
        chk=type({'city': 'San Francisco', 'County': 'San Mateo'}) is dict
        chk=type((1,4)) is tuple
        chk=type(set()) is set
        chk=type(frozenset()) is frozenset
        chk=type(5).__name__==int
        chk=type('mark').__name__=="str"
    
        chk=type(re) is types.ModuleType
        chk=type(re.sub) is types.FunctionType
        chk=type(MySQLdb) is types.ModuleType
        
        async def ping_server(ip):  
            pass
        chk=type(ping_server) is types.FunctionType
        chk=inspect.iscoroutine(ping_server)
    
        class mamal: pass                #empty abstract class
        class bipad(mamal): pass    #empty subclass of empty class
        neanderthal=bipad()               #a new instance of bipad class derived from mamal
        chk=type(neanderthal).__name__ == "instance"
        chk=type(neanderthal).__class__.__name__ == "bipad"

        chk=issubclass(bipad, mamal)                    # True
        chk=isinstance(neanderthal,  object)          # True
        chk=isinstance(print,  object)                     # built-in function is an instance
        
except (chk.Error, e):
    print("Error %d: %s" % (e.args[0], e.args[1]))
    sys.exit(1)
finally:   
        print("All statements evaluated to True.  Well done pyreflection!")
