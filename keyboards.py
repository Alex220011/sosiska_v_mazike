import os, random

n = random.randint(1,10)
f= open(f'{n}', "w")
f.write('0')
f.close()

f = open(f'{n}', "r")
x = f.read(1)

print(x)