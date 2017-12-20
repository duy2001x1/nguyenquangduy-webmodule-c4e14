from mlab import mlab_connect
from models.service import Service

mlab_connect()

all_services = Service.objects()

first_service = all_services[1]

for service in all_services:
    print(service.name)
