from mlab import mlab_connect
from models.service import Service

mlab_connect()




id_to_find = "5a3629a500979c14785634e9"
# amber = Service.objects(id = id_to_find).first() #regular
amber = Service.objects().with_id(id_to_find) #for id only

if amber is None:
    print("Not found")
else:
    print(amber.name)
    #amber.delete()
    amber.update(set__occupied = True)
    amber.reload()
    print(amber.occupied)




filtered_services = Service.objects(gender = 0, height__gte = 160)
for filtered_service in filtered_services:
    print(filtered_service)

first_service = filtered_services.first()
print(first_service.name)
first_service.delete()

false_occupied_services = Service.objects(gender = 0, height__gte = 160, occupied = False).first()
if false_occupied_services is None:
    print("Not found")
else:
    false_occupied_services.update(set__occupied = True)
    false_occupied_services.reload()
    print(false_occupied_services)




# all_services = Service.objects()
#
# first_service = all_services[1]
#
# for service in all_services:
#     print(service.name)
