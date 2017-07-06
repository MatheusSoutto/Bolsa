import struct


indexFormat = "14sLL"
indexStruct = struct.Struct(indexFormat)
print indexStruct.size
print struct.calcsize(indexFormat)