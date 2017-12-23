from mlab import mlab_connect
from class_service.service import Service

from faker import Faker
from random import randint, choice

service_faker = Faker('en_US')
mlab_connect()

Service.drop_collection()

for a in range(100):
    service = Service(account = service_faker.name(),
                      password = randint(100000000, 999999999),
                      game = choice(["lol", "csgo", "pubg"]),
                      price = choice(["1000/h", "1500/h", "2000/h"]),
                      contact = 0 + randint(100000000, 999999999),
                      occupied = choice([True, False]))
    service.save()
