How to find document based on id:
id_to_find = '5a3629a500979c14785634e9'
Docs.objects.get(id = id_to_find)

How to delete the records:
Docs.objects(id = id_to_find).delete()
