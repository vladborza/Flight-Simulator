
import struct

# struct_fmt = '=HHf255s'
# struct_len = struct.calcsize(struct_fmt)
# struct_unpack = struct.Struct(struct_fmt).unpack_from

# results = []
# enc = 'cp437'
# with open("DataBase/waypoint.si2", "rb") as f:
#     while True:
#         data = f.read(struct_len)
#         if not data: break
#         s = struct_unpack(data)
#         results.append(s)
# print(results)
f = open("DataBase/waypoint.si2", "rb")
datastring = ''
with open("DataBase/waypoint.si2", "rb") as f:
    data = f.read(8)
    print(data)

with open("out.txt", "w") as f:
    f.write("".join(map(str,data)));
    f.write('/n');


# datastring = str(f)

f.close()