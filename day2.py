
#input = [("forward", 5),
#          ("down", 5),
#          ("forward", 8),
#          ("up", 3),
#          ("down", 8),
#          ("forward", 2)]

f = open("day2_input.tsv")
input = []
for line in f.readlines():
    data = line[:-1].split(" ")
    input.append((data[0], int(data[1])))

class Course(object):

    def __init__(self, instructions):
        self.instructions = instructions

    def hpos(self):
        hpos = 0
        for instruction in self.instructions:
            if instruction[0] == "forward":
                hpos += instruction[1]
            else:
                continue
        return hpos
               
    def vpos(self):
        vpos = 0
        for instruction in self.instructions:
            if instruction[0] == "down":
                vpos += instruction[1]
            elif instruction[0] == "up":
                vpos -= instruction[1]
                
            else:
                continue
        return vpos
    
    def pos_with_aim(self):
        vpos = 0
        hpos = 0
        aim = 0
        for instruction in self.instructions:
            if instruction[0] == "down":
                aim += instruction[1]
            elif instruction[0] == "up":
                aim -= instruction[1]
            elif instruction[0] == "forward":                
                hpos += instruction[1]
                vpos += instruction[1]*aim
            else:
                continue
        return [vpos,hpos,aim]
        

# part 1
c = Course(input)
print(c.hpos()*c.vpos())

# part 2
pos = c.pos_with_aim()
answer = pos[0]*pos[1]
print(answer)
