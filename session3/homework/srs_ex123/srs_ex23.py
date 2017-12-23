from mlab import mlab_connect
from class_river.River import River

mlab_connect()

print("List of all rivers in Africa")
rivers1 = River.objects(continent = 'Africa')
if rivers1 is None:
    print("Not found")
else:
    for river1 in rivers1:
        print(river1)

print("List of all rivers in S.America and length less than 1000km")
rivers2 = River.objects(continent = 'S. America', length__lt = 1000)
if rivers2 is None:
    print("Not found")
else:
    for river2 in rivers2:
        print(river2)
