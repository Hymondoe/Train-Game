class Train:
  def __init__(self, x, y, size, id, dir):
    self.x = x          #Row where train starts (highest position, closest to top/0): 0-6
    self.y = y          #Column where train starts (furthest left position): 0-6
    self.size = size    #Length of the train: 1-4(5?)
    self.id = id        #Number of train displayed to the player on the board: 1-9 (1 is the train to get out)
    slef.dir = dir      #Direction train is facing: v or h (vertical or horizontal)
    

board = [[0] * 7 for _ in range(7)]
