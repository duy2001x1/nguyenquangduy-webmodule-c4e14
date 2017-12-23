from mongoengine import Document, StringField, IntField

class River(Document):
    name = StringField()
    continent = StringField()
    length = IntField()

    def __str__(self):
        return self.name + ' - ' + self.continent + ' - ' + str(self.length)
