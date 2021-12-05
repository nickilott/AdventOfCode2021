import collections
import itertools

input = ["0,9 -> 5,9\n",
         "8,0 -> 0,8\n",
         "9,4 -> 3,4\n",
         "2,2 -> 2,1\n",
         "7,0 -> 7,4\n",
         "6,4 -> 2,0\n",
         "0,9 -> 2,9\n",
         "3,4 -> 1,4\n",
         "0,0 -> 8,8\n",
         "5,5 -> 8,2\n",
         "5,7 -> 7,9\n"]

input = open("day5_input.txt").readlines()

def formatLine(line):
    data = line[:-1].split(" -> ")
    x1, y1 = data[0].split(",")
    x2, y2 = data[1].split(",")
    return([x1, x2, y1, y2])


class Line(object):

    def __init__(self, x1, x2, y1, y2):
        self.coords = {"x1": int(x1), "x2": int(x2), "y1": int(y1), "y2": int(y2)}

        self.is_diagonal = False
        if abs(self.coords["x1"] - self.coords["x2"]) == abs(self.coords["y1"] - self.coords["y2"]):
            self.is_diagonal = True


    def bigy(self):
        if self.coords["y1"] > self.coords["y2"]:
            biggy, littley = "y1", "y2"
        elif self.coords["y2"] > self.coords["y1"]:
            biggy, littley = "y2", "y1"
        return([biggy, littley])

    def bigx(self):
        if self.coords["x1"] > self.coords["x2"]:
            biggx, littlex = "x1", "x2"
        elif self.coords["x2"] > self.coords["x1"]:
            biggx, littlex = "x2", "x1"
        return([biggx, littlex])

    def get_points(self):
        print(self.is_diagonal)
        if self.is_diagonal:
            xcoords = range(self.coords[self.bigx()[1]], self.coords[self.bigx()[0]]+1)
            ycoords = range(self.coords[self.bigy()[1]], self.coords[self.bigy()[0]]+1)
            if self.coords["x1"] < self.coords["x2"]:
                xcoords.reverse()
            if self.coords["y1"] < self.coords["y2"]:
                ycoords.reverse()

        elif not self.is_diagonal:
            if self.coords["x1"] == self.coords["x2"]:
                # y varies in this case
                ycoords = range(self.coords[self.bigy()[1]], self.coords[self.bigy()[0]]+1)
                xcoords = [x for x in itertools.repeat(self.coords["x1"], len(ycoords))]
            elif self.coords["y1"] == self.coords["y2"]:
                # x varies
                xcoords = range(self.coords[self.bigx()[1]], self.coords[self.bigx()[0]]+1)
                ycoords = [x for x in itertools.repeat(self.coords["y1"], len(xcoords))]
            else:
                xcoords = None
                ycoords = None

        if xcoords and ycoords:
            points = []
            for x in zip(xcoords, ycoords):
                points.append(x)
        else:
            points = None

        return(points)


def count_points(input):
    result = collections.defaultdict(int)
    for line in input:
        data = formatLine(line)
        l = Line(data[0], data[1], data[2], data[3])
        points = l.get_points()
        print(points)
        if points:
            for p in points:
                result[p] += 1
        else:
            continue
    return(result)

def get_dangerous(points):
    danger_zones = []
    for x,y in points.items():
        if y >= 2:
            danger_zones.append(x)
    return(danger_zones)


# part 1
print(len(get_dangerous(count_points(input))))
    
# part 2

