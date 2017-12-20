from mongoengine import Document, StringField, IntField, BooleanField

class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField() #0: Female, 1: Male
    height = IntField() #cm
    phone = StringField()
    occupied = BooleanField()
