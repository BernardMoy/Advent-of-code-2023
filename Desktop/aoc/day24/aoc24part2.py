import sympy

with open ('input.txt', 'r') as file:
    lines = file.read().split('\n')

for i in range(len(lines)):
    lines[i] = lines[i].replace(' @', ',')
    lines[i] = [int(x) for x in lines[i].split(', ')]

x,y,z,vx,vy,vz = sympy.symbols("x,y,z,vx,vy,vz")

equations = []

for [x1,y1,z1,sx1,sy1,sz1] in lines:
    equations.append((x-x1)*(sy1-vy) - (y-y1)*(sx1-vx))
    equations.append((y-y1)*(sz1-vz) - (z-z1)*(sy1-vy))

result = sympy.solve(equations)
print(result)
print(result[0][x] + result[0][y] + result[0][z])
