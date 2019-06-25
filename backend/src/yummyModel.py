from peewee import *

database = MySQLDatabase('yummy', **{'charset': 'utf8', 'use_unicode': True, 'host': 'localhost', 'user': 'root', 'password': 'Yy981211'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Customer(BaseModel):
    email = CharField(primary_key=True)
    level = IntegerField(constraints=[SQL("DEFAULT 0")])
    name = CharField()
    phone = CharField()
    pwd = CharField()
    valid = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'customer'

class NewArea(BaseModel):
    aid = CharField(primary_key=True)
    area = CharField(null=True)
    des = CharField(null=True)

    class Meta:
        table_name = 'new_area'

class NewMeal(BaseModel):
    des = CharField(null=True)
    name = CharField(null=True)
    nid = CharField(primary_key=True)
    photo = CharField(null=True)
    price = FloatField(null=True)
    rid = CharField(null=True)
    type = CharField(null=True)

    class Meta:
        table_name = 'new_meal'

class NewOrder(BaseModel):
    cost = FloatField(null=True)
    oid = AutoField()
    stata = IntegerField(null=True)
    tid = CharField(null=True)
    time = DateTimeField(null=True)
    uid = CharField(null=True)

    class Meta:
        table_name = 'new_order'

class NewOrderlist(BaseModel):
    mid = CharField(null=True)
    num = IntegerField(null=True)
    oid = CharField(null=True)

    class Meta:
        table_name = 'new_orderlist'

class NewPromotion(BaseModel):
    amount = FloatField(null=True)
    discount = FloatField(null=True)
    promotionid = CharField(primary_key=True)

    class Meta:
        table_name = 'new_promotion'

class NewRes(BaseModel):
    area = CharField(null=True)
    dc = CharField(null=True)
    des = CharField(null=True)
    mda = CharField(null=True)
    name = CharField(null=True)
    photo = CharField(null=True)
    promotion = CharField(null=True)
    rid = CharField(primary_key=True)
    stars = CharField(null=True)

    class Meta:
        table_name = 'new_res'

class NewTag(BaseModel):
    tagid = CharField(primary_key=True)
    tagname = CharField(null=True)

    class Meta:
        table_name = 'new_tag'

class NewTagRes(BaseModel):
    rid = CharField(null=True)
    tagid = CharField(null=True)

    class Meta:
        table_name = 'new_tag_res'

