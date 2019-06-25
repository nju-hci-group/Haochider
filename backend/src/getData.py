from yummyModel import *


def getRes():
    return NewRes.select().limit(20)