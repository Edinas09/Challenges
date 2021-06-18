from array import *
# b	Represents signed integer of size 1 byte
# B	Represents unsigned integer of size 1 byte
# c	Represents character of size 1 byte
# i	Represents signed integer of size 2 bytes
# I	Represents unsigned integer of size 2 bytes
# f	Represents floating point of size 4 bytes
# d	Represents floating point of size 8 bytes
# arrayName = array(typecode, [Initializers])

array1 = array('i', [10, 20, 30, 40, 50])

for x in array1:
    print(x)

print(array1[0])
print(array1[2])

#insertion operation
array1.insert(1,60)
for x in array1:
    print(x)

#Deleting operation
array1.remove(40)
for x in array1:
    print(x)

# Search Operation
print(array1.index(30))

# update Operation
array1[2] = 80

for x in array1:
    print(x)


