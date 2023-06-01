import os

RGB = input()

R, G, B = RGB.split(",")

ret = str(hex(int(R)))[2:] + str(hex(int(G)))[2:] + str(hex(int(B)))[2:]
ret.split()
print(ret)

os.system('echo ' + ret + '| clip')