#This is in Python3, if you're using regular Python the only change you should have to make it to delete the parentheses at all the print statements and add a space inbetween 'print' and what is being printed
class Train:
  def __init__(self, x, y, size, id, dir):
    self.x = x          #Row where train starts (highest position, closest to top/0): 0-6
    self.y = y          #Column where train starts (furthest left position): 0-6
    self.size = size    #Length of the train: 1-4(5?)
    self.id = id        #Number of train displayed to the player on the board: 1-9 (1 is the train to get out)
    self.dir = dir      #Direction train is facing: v or h (vertical or horizontal)
def redraw(Trains, board):
    for i in range(s):
        for j in range(s):
            board[j][i] = '-'
        
    board[6][3] = 0
    for k in Trains:
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
    return Trains, board
Trains = []
s = 7
board = [['-'] * 7 for _ in range(7)]
for i in range(s):
    for j in range(s):
        board[j][i] = '-'
        
board[6][3] = 0
Trains.append(Train(2,3,3,1,'h'))
Trains.append(Train(6,3,3,2,'v'))
for k in Trains:
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

EverythingYoullEverNeed = []
while True:
    STRING = str(input("Enter the movement you want in this format: 'Train #' 'Direction you want it to move (W,A,S,D)' 'how far you want it to move'"))
    
    Info = STRING.split(' ')
    print(Info[0])
    print(Info[1])
    print(Info[2])
    if Info[1] == 'W':
        if Trains[int(Info[0])-1].dir == 'h':
            print("can't move")
            break
        for i in range(int(Info[2])):
            if Trains[int(Info[0])-1].y == 0:
                print("cant't move 1")
            elif board[Trains[int(Info[0])-1].x][Trains[int(Info[0])-1].y - 1] == '-':
                Trains[int(Info[0])-1].y -= int(Info[2])
    if Info[1] == 'S':
        if Trains[int(Info[0])-1].dir == 'h':
            print("can't move")
            break
        for i in range(int(Info[2])):
            if Trains[int(Info[0])-1].y >= s:
                print("cant't move 1")
            elif board[Trains[int(Info[0])-1].x][Trains[int(Info[0])-1].y + 1] == '-':
                Trains[int(Info[0])-1].y -= int(Info[2])
    if Info[1] == 'A':
        if Trains[int(Info[0])-1].dir == 'v':
            print("can't move")
            break
        for i in range(int(Info[2])):
            if Trains[int(Info[0])-1].x == 0:
                print("cant't move 1")
            elif board[Trains[int(Info[0])-1].x - 1][Trains[int(Info[0])-1].y] == '-':
                Trains[int(Info[0])-1].y -= int(Info[2])
    if Info[1] == 'D':
        if Trains[int(Info[0])-1].dir == 'v':
            print("can't move")
        for i in range(int(Info[2])):
            if Trains[int(Info[0])-1].x >= s:
                print("cant't move 1")
            elif board[Trains[int(Info[0])-1].x + 1][Trains[int(Info[0])-1].y] == '-':
                Trains[int(Info[0])-1].y -= int(Info[2])
    Trains, board = redraw(Trains, board)
            
