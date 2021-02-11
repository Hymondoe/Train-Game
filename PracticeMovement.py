class Train:
  def __init__(self, x, y, size, id, dir):
    self.x = x          #Row where train starts (highest position, closest to top/0): 0-6
    self.y = y          #Column where train starts (furthest left position): 0-6
    self.size = size    #Length of the train: 1-4(5?)
    self.id = id        #Number of train displayed to the player on the board: 1-9 (1 is the train to get out)
    self.dir = dir      #Direction train is facing: v or h (vertical or horizontal)
Trains = []
s = 7
board = [['-'] * 7 for _ in range(7)]
for i in range(s):
    for j in range(s):
        board[j][i] = 0
Trains.append(Train(2,3,3,1,'h'))
Trains.append(Train(6,0,4,2,'v'))
for k in Trains:
    if k.dir == 'h':
        for p in range(k.size):
            board[k.x + p][k.y] = k.id
    elif k.dir == 'v':
        for p in range(k.size):
            board[k.x][k.y + p] = k.id
        
for i in range(s):
    for j in range(s):
        print board[j][i],
    print ""
