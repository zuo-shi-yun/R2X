import os

RGB = input()

R, G, B = RGB.split(",")

R = format(int(R), "02x")
G = format(int(G), "02x")
B = format(int(B), "02x")

res = R + G + B

print(res)

os.system('echo ' + res + '| clip')
