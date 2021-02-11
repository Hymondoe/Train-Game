class train:
    def __init__(self, body, number):
        self.body = body
        self.number = number
    
sizex, sizey =  (7,7)
map = [[0]* sizex]* sizey
for i in range(sizey):
    for j in range(sizex):
        print(str(map[i][j]) + ' ', end = "")
    print()




