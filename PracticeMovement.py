#This is in Python3, if you're using regular Python the only change you should have to make it to delete the parentheses at all the print statements and add a space inbetween 'print' and what is being printed
class Train:
  def __init__(self, x, y, size, id, dir):
    self.x = x          #Row where train starts (highest position, closest to top/0): 0-6
    self.y = y          #Column where train starts (furthest left position): 0-6
    self.size = size    #Length of the train: 1-4(5?)
    self.id = id        #Number of train displayed to the player on the board: 1-9 (1 is the train to get out)
    self.dir = dir      #Direction train is facing: v or h (vertical or horizontal)
def redraw(trains, board):
    for i in range(s):
        for j in range(s):
            board[j][i] = '-'
        
    board[6][3] = 0
    for k in trains:
        if k.dir == 'h':
            for p in range(k.size):
                board[k.x + p][k.y] = k.id
        elif k.dir == 'v':
            for p in range(k.size):
                board[k.x][k.y + p] = k.id
        
    for i in range(s):
        for j in range(s):
            print(board[j][i], end = "")
        print("")
    return trains, board
trains = []
s = 7
board = [['-'] * 7 for _ in range(7)]
for i in range(s):
    for j in range(s):
        board[j][i] = '-'
        
board[6][3] = 0
trains.append(Train(2,3,3,1,'h'))
trains.append(Train(6,3,3,2,'v'))
for k in trains:
    if k.dir == 'h':
        for p in range(k.size):
            board[k.x + p][k.y] = k.id
    elif k.dir == 'v':
        for p in range(k.size):
            board[k.x][k.y + p] = k.id
        
for i in range(s):
    for j in range(s):
        print(board[j][i], end = "")
    print("")

while True:
    STRING = str(input("Enter the movement you want in this format: 'Train #' 'Direction you want it to move (W,A,S,D)' 'how far you want it to move'"))
    
    Info = STRING.split(' ')
    T = trains[int(Info[0]) - 1]
    if Info[1] == 'W':
        if T.dir == 'h':
            print("wrong way")
            break
        else:
            for i in range(int(Info[2])):
                if T.y - 1 >= 0 and (board[T.x][T.y - 1] == '-' or board[T.x][T.y - 1] == 0):
                    T.y -= 1
    if Info[1] == 'S':
        if T.dir == 'h':
            print("wrong way")
            break
        else:
            for i in range(int(Info[2])):
                if T.y + T.size < s and (board[T.x][T.y + T.size] == '-' or board[T.x][T.y + T.size] == 0):
                    T.y += 1
    if Info[1] == 'A':
        if T.dir == 'v':
            print("wrong way")
            break
        else:
            for i in range(int(Info[2])):
                if T.x - 1 >= 0 and (board[T.x - 1][T.y] == '-' or board[T.x - 1][T.y] == 0):
                    T.x -= 1
    if Info[1] == 'D':
        if T.dir == 'v':
            print("wrong way")
        else:
            for i in range(int(Info[2])):
                if T.x + T.size < s and (board[T.x + T.size][T.y] == '-' or board[T.x + T.size][T.y] == 0):
                    T.x += 1
    trains[int(Info[0]) - 1] = T
    trains, board = redraw(trains, board)
    if board[6][3] == 1:
        print("You Won!")
        break
