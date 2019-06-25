from peewee import *

database = MySQLDatabase('yummy', **{
    'charset': 'utf8', 
    'use_unicode': True, 
    'host': 'localhost', 
    'user': 'root',
    'password': 'Yy981211'
})

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

class AddressInfo(BaseModel):
    address = CharField()
    email = ForeignKeyField(backref='customer_email_set', column_name='email', field='email', model=Customer)
    id = BigAutoField()
    latitude = FloatField()
    longitude = FloatField()

    class Meta:
        table_name = 'address_info'

class EmailKey(BaseModel):
    email = ForeignKeyField(backref='customer_email_set', column_name='email', field='email', model=Customer, primary_key=True)
    key = CharField()

    class Meta:
        table_name = 'email_key'

class Restaurant(BaseModel):
    address = CharField()
    balance = FloatField(constraints=[SQL("DEFAULT 0")])
    description = CharField(null=True)
    id = CharField(primary_key=True)
    latitude = FloatField()
    longitude = FloatField()
    name = CharField()
    phone = CharField()
    pwd = CharField()
    type = CharField()
    valid = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'restaurant'

class Meal(BaseModel):
    description = CharField(null=True)
    end_date = DateField(column_name='endDate')
    id = BigAutoField()
    name = CharField()
    num = IntegerField()
    price = FloatField()
    restaurant = ForeignKeyField(backref='restaurant_restaurant_set', column_name='restaurant', field='id', model=Restaurant)
    start_date = DateField(column_name='startDate')
    type = CharField()

    class Meta:
        table_name = 'meal'

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
    oid = CharField(primary_key=True)
    stata = IntegerField(null=True)
    tid = CharField(null=True)
    time = DateTimeField(null=True)
    uid = CharField(null=True)

    class Meta:
        table_name = 'new_order'

class NewOrderlist(BaseModel):
    id = CharField(primary_key=True)
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

class Order(BaseModel):
    cancel_time = DateTimeField(column_name='cancelTime', null=True)
    complete_time = DateTimeField(column_name='completeTime', null=True)
    cost = FloatField()
    destination = ForeignKeyField(backref='address_info_destination_set', column_name='destination', field='id', model=AddressInfo)
    email = ForeignKeyField(backref='customer_email_set', column_name='email', field='email', model=Customer)
    id = BigAutoField()
    place_time = DateTimeField(column_name='placeTime', constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    restaurant = ForeignKeyField(backref='restaurant_restaurant_set', column_name='restaurant', field='id', model=Restaurant)
    state = IntegerField()

    class Meta:
        table_name = 'order'

class OrderItem(BaseModel):
    mid = ForeignKeyField(backref='meal_mid_set', column_name='mid', field='id', model=Meal)
    num = IntegerField(constraints=[SQL("DEFAULT 1")])
    oid = ForeignKeyField(backref='order_oid_set', column_name='oid', field='id', model=Order)

    class Meta:
        table_name = 'order_item'
        indexes = (
            (('oid', 'mid'), True),
        )
        primary_key = CompositeKey('mid', 'oid')

class PaymentAccount(BaseModel):
    balance = FloatField(constraints=[SQL("DEFAULT 0")])
    email = ForeignKeyField(backref='customer_email_set', column_name='email', field='email', model=Customer)
    id = CharField(primary_key=True)
    pwd = CharField()

    class Meta:
        table_name = 'payment_account'

class Promotion(BaseModel):
    amount = FloatField()
    discount = FloatField()
    end_date = DateField(column_name='endDate')
    restaurant = ForeignKeyField(backref='restaurant_restaurant_set', column_name='restaurant', field='id', model=Restaurant)
    start_date = DateField(column_name='startDate')

    class Meta:
        table_name = 'promotion'
        indexes = (
            (('restaurant', 'amount'), True),
        )
        primary_key = CompositeKey('amount', 'restaurant')

class Properties(BaseModel):
    name = CharField(primary_key=True)
    value = TextField(null=True)

    class Meta:
        table_name = 'properties'

class RestaurantDraft(BaseModel):
    address = CharField()
    description = CharField(null=True)
    id = ForeignKeyField(backref='restaurant_id_set', column_name='id', field='id', model=Restaurant, primary_key=True)
    latitude = FloatField()
    longitude = FloatField()
    name = CharField()
    phone = CharField()
    type = CharField()

    class Meta:
        table_name = 'restaurant_draft'

class Transaction(BaseModel):
    amount = FloatField()
    id = BigAutoField()
    in_account = CharField(column_name='inAccount')
    oid = ForeignKeyField(backref='order_oid_set', column_name='oid', field='id', model=Order)
    out_account = CharField(column_name='outAccount')
    time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'transaction'

