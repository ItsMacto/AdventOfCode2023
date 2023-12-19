

def star1():
    with open("input.txt") as fp:
    # with open("example.txt") as fp:
        lines = fp.readlines()
        seeds = [int(num) for num in lines[0].strip("seeds: ").split()]
        
        
        maps = [[]]
        i = 3 
        mapNum = 0
        while i < len(lines):
            if lines[i] == "\n":
                i += 2
                mapNum += 1
                maps.append([])
            else:
                maps[mapNum].append([int(num) for num in lines[i].strip("\n").split()])
                i += 1 
        # print(seeds)
        # print(maps)
        locations = [] 
        for seed in seeds:
            location = seed
            for category in maps:
                for map in category:
                    if location in range(map[1], map[1] + map[2]):
                        difference = location - map[1]
                        location = map[0] + difference
                        # print(seed, location)
                        break
            locations.append(location)
                        
        return min(locations)



# def star2():
#     # with open("input.txt") as fp:
#     with open("example.txt") as fp:
#         lines = fp.readlines()
#         line = [int(num) for num in lines[0].strip("seeds: ").split()]
#         seedRanges = []
#         for start, range in zip(line[::2], line[1::2]):
#             seedRanges.append([start, range])

#         print(seedRanges)
        
#         maps = [[]]
#         i = 3 
#         mapNum = 0
#         while i < len(lines):
#             if lines[i] == "\n":
#                 i += 2
#                 mapNum += 1
#                 maps.append([])
#             else:
#                 maps[mapNum].append([int(num) for num in lines[i].strip("\n").split()])
#                 i += 1 

#         for category in maps:
#             destination = []     
#             for range in category:
#                 for seedRange in seedRanges:
#                     # if the seed range is withing all or part of the map range
#                     # seedRange[0] start [1] range
#                     # range[1] start [2] range
#                     if 
#                         # destanation.append(new range)
#             seedRange = destination
#         return min(seedRange)
        
        
def star2():
    with open("input.txt") as fp:
        lines = fp.readlines()
        line = [int(num) for num in lines[0].strip("seeds: ").split()]
        seedRanges = [(line[i], line[i + 1]) for i in range(0, len(line), 2)]

        maps = [[]]
        i = 3
        mapNum = 0
        while i < len(lines):
            if lines[i] == "\n":
                i += 2
                mapNum += 1
                maps.append([])
            else:
                maps[mapNum].append([int(num) for num in lines[i].strip("\n").split()])
                i += 1

        for category in maps:
            # print(seedRanges)
            new_seedRanges = []
            for seedRange in seedRanges:
                seed_start, seed_len = seedRange
                seed_end = seed_start + seed_len
                range_mapped = False

                for map_range in category:
                    dest_start, src_start, range_len = map_range
                    src_end = src_start + range_len

                    # Check overlap
                    print(seed_start, seed_end, src_start, src_end)
                    if seed_start < src_end and seed_end > src_start:
                        range_mapped = True
                        overlap_start = max(seed_start, src_start)
                        overlap_end = min(seed_end, src_end)

                        # Calculate new range
                        offset = dest_start - src_start
                        new_start = overlap_start + offset
                        new_len = overlap_end - overlap_start
                        new_seedRanges.append((new_start, new_len))
                
                if not range_mapped:
                    new_seedRanges.append(seedRange)

            seedRanges = new_seedRanges
            min_location = min(seedRange[0] for seedRange in seedRanges)
            print(seedRanges)
            print(min_location)
        # Find the minimum location
        # print(seedRanges)
        min_location = min(seedRange[0] for seedRange in seedRanges)
        return min_location



        
        

        
if __name__ == "__main__":
    # print(star1())
    print(star2())