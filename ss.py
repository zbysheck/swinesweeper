# import Tkinter


class Board:
    h = 0
    w = 0

    def __init__(self, h, w, mines):
        self.h = h
        self.w = w
        self.mines = mines
        self.board = self.generate_mines(h, w, mines)

    def generate_mines(self, h, w, mines):
        l = range(0, h*w)
        for i in range(mines):
            print "something"
        print l
        print mines
        return 0




b = Board(3,4,5)
b.generate_mines(3, 4, 5)