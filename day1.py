import numpy as np

class Depths(object):

    def __init__(self, depths):
        self.depths = {x:y for x, y in enumerate(depths)}

    def increase(self):
        increase = 0 
        for idx, measurement in self.depths.items():
            if idx == 0:
                continue
            if measurement > self.depths[idx-1]:
                increase += 1
        return increase

    def three_measure_window(self):
        sliding_window = []
        for idx, measurement in self.depths.items():
            try:
                summed_measure = np.sum([self.depths[idx], self.depths[idx+1], self.depths[idx+2]])            
                sliding_window.append(summed_measure)
            except KeyError:
                return sliding_window        

        

#input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
input = [int(x[:-1]) for x in open("input.day1").readlines()]

# Part 1
d = Depths(input)
print (d.increase())

# Part 2
print(Depths(d.three_measure_window()).increase())


