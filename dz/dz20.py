import os

dir_name = 'work'
a_name = r'E:\python\work\F1'
b_name = r'E:\python\work\F2\F21'

objs = os.listdir(dir_name)
obi = os.listdir(a_name)
oba = os.listdir(b_name)
su = obi + objs + oba
# print(su)

for obj in su:
    p = os.path.join(dir_name, obj)
    c = os.path.join(a_name, obj)
    z = os.path.join(b_name, obj)

    if os.path.isfile(p):
        if os.path.getsize(p) > 0:
            print(f'{p} - {os.path.getsize(p)} bytes')
    if os.path.isfile(c):
        if os.path.getsize(c) > 0:
            print(f'{c} - {os.path.getsize(c)} bytes')
    if os.path.isfile(z):
        if os.path.getsize(z) > 0:
            print(f'{z} - {os.path.getsize(z)} bytes')

