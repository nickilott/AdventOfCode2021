import numpy as np
import itertools

f = open("day4_input.tsv")

# read in the numbers
input_n = [float(x) for x in f.readline()[:-1].split(",")]

# read in the boards
input = [x for x in f.readlines() if x!= "\n" and x!=""]
formatted = []
for i in input:
    if i.startswith(" "):
        i = i.replace(" ", "", 1)
    else:
        i = i
    formatted.append(i)
input = formatted


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


# this took me ages and is horrible. Lots of spaces in
# the input
boards = []
for i in chunks(input, 5):
    bs = [x[:-1].split(" ") for x in i]
    new_bs = []
    for row in bs:
        row = [j for j in row if j!=""]
        row = [int(k) for k in row]
        new_bs.append(row)
    boards.append(new_bs)

class Board(object):

    def __init__(self, numbers):
        # numbers in a list of lists
        self.board = np.array(numbers, dtype=float)
        self.winner = False 

    def mark(self, number):
        # make NA if number is called
        idx = np.where(self.board == number)

        # not found
        if len(idx[0]) == 0:
            return(self.board)
        # mark it
        elif len(idx[0]) == 1:
            self.board[idx[0], idx[1]] = np.nan    


    def check_win(self):
        # check rows
        for i in range(len(self.board[0])):
            if np.isnan(np.nansum(self.board[i,])):
                self.winner = True
        # check columns
        for i in range(len(self.board)):
            if np.isnan(np.nansum(self.board[:,i])):
                self.winner = True

    def sum_unmarked(self):
        return(np.nansum(self.board))

def play_bingo(board, numbers):
    # play the game and return
    # the round at which it won
    b = Board(board)
    for i in range(len(numbers)):
        round = i
        n = numbers[i]
        # make a mark if number present
        b.mark(n)
        # check wil
        b.check_win()
        if b.winner:
            break
        else:
            continue    
    return([round, b.sum_unmarked()*n])

# by the time I had got this far and the input
# was ok I couldn't be bothered to sort the result
# so just scrolled through the 100 results :(
i = 0
for board in boards:
    i += 1
    result = play_bingo(board, input_n)
    print ("board %i" % i, result)
