from mongoengine import Document, StringField, IntField, BooleanField

class Service(Document):
    account = StringField()
    password = IntField()
    game = StringField()
    price = StringField()
    contact = IntField()
    occupied = BooleanField()

    def __str__(self):
        return "{0} - {1} - {2} - {3} - {4} - {5}".format(self.account, self.password, self.game, self.price, self.contact, self.occupied)
