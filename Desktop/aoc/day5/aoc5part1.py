with open ('input.txt', 'r') as file:
    lines = file.read().split('\n')

    seeds_raw = lines[0][7::]

    seeds = seeds_raw.split(" ")

with open ('input.txt', 'r') as file:
    maps = file.read().split('\n\n')

map1 = maps[1].split('\n')[1::]
    
for i in range(len(map1)):
    map1[i] = map1[i].split(' ')

map2 = maps[2].split('\n')[1::]
    
for i in range(len(map2)):
    map2[i] = map2[i].split(' ')

map3 = maps[3].split('\n')[1::]

for i in range(len(map3)):
    map3[i] = map3[i].split(' ')

map4 = maps[4].split('\n')[1::]
    
for i in range(len(map4)):
    map4[i] = map4[i].split(' ')

map5 = maps[5].split('\n')[1::]
    
for i in range(len(map5)):
    map5[i] = map5[i].split(' ')

map6 = maps[6].split('\n')[1::]

for i in range(len(map6)):
    map6[i] = map6[i].split(' ')

map7 = maps[7].split('\n')[1::]
    
for i in range(len(map7)):
    map7[i] = map7[i].split(' ')


# Output the mapped seeds given a list of seeds, a map (list)
def map(seeds, maps):
    mapped_seeds = []

    # For each seed, check if it corresponds to a map
    for seed in seeds:
        mapped = False

        for map in maps:
            # Proceed to the next seed if mapped
            if mapped:
                continue
            
            # Ensure the seed is not smaller than the source number, and within the range length
            if int(seed) >= int(map[1]) and int(seed) - int(map[1]) < int(map[2]):
                mapped_seeds.append(int(map[0]) + int(seed) - int(map[1]))
                mapped = True

        # Add the original seed if not mapped after all maps
        if not mapped:
            mapped_seeds.append(seed)

    return mapped_seeds

# Map the seeds one by one
tmp = map(seeds, map1)
tmp = map(tmp, map2)
tmp = map(tmp, map3)
tmp = map(tmp, map4)
tmp = map(tmp, map5)
tmp = map(tmp, map6)
tmp = map(tmp, map7)


print(min(tmp))
