from yummyModel import *
from peewee import *

def getRes():
    return NewRes.select().limit(20)