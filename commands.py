from check_it import *
from ai import check_NxtMoove
import sys


def turn(self, line):
    check = False
    for i in line[1]:
        if i == ',':
            check = True
    if check == False:
        print("ERROR message - unsupported coordinates", flush=True)
        self.command()
    tmp = line[1].split(",")
    self.x = check_int(self, tmp[0])
    self.y = check_int(self, tmp[1])
    if self.x >= self.size or self.y >= self.size:
        self.x = 0
        self.y = 0
        print("ERROR message - unsupported coordinates", flush=True)
        self.command()
    else:
        self.add('x')
        #check_win(self)
    check_NxtMoove(self)
    self.command()

def about():
    print("name=\"Gomoku\", version=\"1.0\", author=\"elliot khalife\", country=\"FR\", email=\"elliot.khalife@epitech.eu\"", flush=True)

def end():
    exit(0)

def begin(self):
    self.x = round(self.size / 2)
    self.y = round(self.size / 2)
    self.add('o')
    print("{0},{1}".format(self.x, self.y))
    sys.stdout.flush()
    self.command()

def start(self, line):
    if len(line) > 1:
        self.size = check_start(self, line[1])
    else:
        print("ERROR message - unsupported coordinates", flush=True)
    if self.size <= 0:
        print("ERROR message - unsupported coordinates", flush=True)
        self.command()
    else:
        print("OK", flush=True)
    self.create_map()
    self.did_we = True
    self.beg = True
    self.command()

def board(self, tmp):
    nb = 0
    tmp2 = []
    for i in tmp:
        self.board_data.append('')
        tmp2 = i.split(',')
        it = 0
        while it != len(tmp2):
            tmp2[it] = check_int(self, tmp2[it])
            it += 1
        self.board_data[nb] = tmp2
        nb += 1
    for i in self.board_data:
        self.x = i[0]
        self.y = i[1]
        if i[2] == 1:
            self.add('o')
        if i[2] == 2:
            self.add('x')
    check_NxtMoove(self)
    self.command()
    #board ne passe pas par la quand il return 
