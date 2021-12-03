
#input = ["00100",
#         "11110",
#         "10110",
#         "10111",
#         "10101",
#         "01111",
#         "00111",
#         "11100",
#         "10000",
#         "11001",
#         "00010",
#         "01010"]


# some weird newlines introduced into input
input = [x[:-1] for x in open("day3_input.tsv").readlines() if x != '\n']

import collections

def countit(l, element="0"):
    return(l.count(element))


class Diagnostic(object):

    def __init__(self, report):
        self.report = report
        self.positions = collections.defaultdict(list)
        for binary in self.report:
            for i in range(len(binary)):
                self.positions[i].append(binary[i])
        self.gamma_rate = None
        self.epsilon_rate = None

    def gamma(self):
        result = []
        for position, binaries in self.positions.items():        
            if countit(binaries, "0") > countit(binaries, "1"):
                result.append("0")
            else:
                result.append("1")
        result = "".join(result)
        return(int(result, 2))

    def epsilon(self):
        result = []
        for position, binaries in self.positions.items():        
            if countit(binaries, "0") < countit(binaries, "1"):
                result.append("0")
            else:
                result.append("1")
        result = "".join(result)
        return(int(result, 2))


def oxygen(input):

    d = Diagnostic(input)
    keep = d.report
    positions = d.positions
    binaries = d.positions.values()
    positions = positions.keys()

    for position in positions:
        if countit(binaries[position], "0") > countit(binaries[position], "1"):
            d = Diagnostic([x for x in keep if str(x[position]) == "0"])
        elif countit(binaries[position], "1") > countit(binaries[position], "0"):
            d = Diagnostic([x for x in keep if str(x[position]) == "1"])
        elif countit(binaries[position], "1") == countit(binaries[position], "0"):
            d = Diagnostic([x for x in keep if str(x[position]) == "1"])
        keep = d.report
        binaries = d.positions.values()
        if len(keep) == 1:
            break
    return(int(keep[0], 2))

def co2(input):

    d = Diagnostic(input)
    keep = d.report
    positions = d.positions
    binaries = d.positions.values()
    positions = positions.keys()

    for position in positions:
        if countit(binaries[position], "0") > countit(binaries[position], "1"):
            d = Diagnostic([x for x in keep if str(x[position]) == "1"])
        elif countit(binaries[position], "1") > countit(binaries[position], "0"):
            d = Diagnostic([x for x in keep if str(x[position]) == "0"])
        elif countit(binaries[position], "1") == countit(binaries[position], "0"):
            d = Diagnostic([x for x in keep if str(x[position]) == "0"])
        keep = d.report
        binaries = d.positions.values()
        if len(keep) == 1:
            break
    return(int(keep[0], 2))



# part 1
d = Diagnostic(input)
power_consumption = d.gamma()*d.epsilon()
print(power_consumption)

# part 2
print(oxygen(input)*co2(input))
