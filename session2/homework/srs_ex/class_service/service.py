from mongoengine import Document, StringField, IntField, BooleanField

class Service(Document):
    account = StringField()
    password = IntField()
    game = StringField()
    price = StringField()
    contact = IntField()
    occupied = BooleanField()
