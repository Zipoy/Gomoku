#!/bin/python3
# gomoku

import sys
from check_it import *
from commands import *


class gomoku():
    def __init__(self):
        self.pattern = [['o','o','a','o','o'], ['o','o','o','o','a'], ['o','o','o','a','o'], ['x','x','a','x','x'], ['x','x','x','x','a'], ['x','x','x','a','x'], ['x','x','a','x'], ['x','x','x','a'], ['o','o','a','o'], ['o','o','o','a'], ['o','o','a'], ['o','a','o'], ['o','a']]
        self.size = 0
        self.win = 0
        self.beg = False
        self.did_we = False
        self.player = 'x'
        self.bot = 'o'
        self.x = 0
        self.y = 0
        self.map = []
        #map need to be char less memory
        self.board_data = []
        self.key = ""
        self.value = 0

    def init(self):
        self.command()

    def command(self):
        try:
            tmp = []
            for line in sys.stdin:
                if line == "":
                    continue
                # if check_h(self) == 1:
                #     print("WORKING")
                # if check_v(self) != 0:
                #     print("THats work")
                # if check_d(self) == 1:
                #     print("WORKING")
                if check_cmd(self, line.split(' ')) == False:
                    continue
                if self.did_we == True and line.split("\n")[0] == "BOARD":
                    for line in sys.stdin:
                        if line.split("\n")[0] == "DONE":
                            self.beg = False
                            board(self, tmp)
                            break
                        tmp.append(line.split("\n")[0])
                for var in line.split():
                    if var == "ABOUT":
                        about()
                    if var == "END":
                        end()
                    if self.did_we == False and var == "START":
                        start(self, line.split())
                    if self.did_we == True:
                        if var == "TURN":
                            self.beg = False
                            turn(self, line.split())
                        elif var == "BEGIN":
                            if self.beg == True:
                                begin(self)
                            else:
                                print("ERROR message", flush=True)
        except KeyboardInterrupt:
            exit(0)


    def put_plus(self, i, y, ok):
        string = ['a', 'a', 'a', 'a', 'a']
        check = i
        nb = 0
        while i != check + 5:
            string[nb] = self.map[i][y]
            nb += 1
            i += 1
            y += 1
        return (string, ok)

    def put_moins(self, i, y, ok):
        string = ['a', 'a', 'a', 'a', 'a']
        check = i
        nb = 0
        while i != check - 5:
            string[nb] = self.map[i][y]
            nb += 1
            i -= 1
            y -= 1
        return (string, ok)

# algo avec elage

    def create_map(self):
        self.map = [['a' for _ in range(self.size)] for _ in range(self.size)]

    def add(self, p):
        if self.map[self.y][self.x] == 'a':
            self.map[self.y][self.x] = p
            # for i in self.map:
            #     print(i)
            # print("////////////////////////////////////////////")
            # for i in self.map:
            #     print(i)
            #check_win(self)
        else:
            print("ERROR message - unsupported coordinates", flush=True)
            self.command()

    # def put_it(self, x, y, t):
    #     it = 0
    #     if t == 'h':
    #         while it != 5:
    #             if self.map[y][x + it] == 'a':
    #                 self.x = x + it
    #                 self.y = y
    #                 self.add('o')
    #     if t == 'd':
    #         nb = 0
    #         if (y + 5) < self.size and (x + 5) < self.size:
    #             while 
    #             if tmp != ['a', 'a', 'a', 'a','a']:
    #                 arr_str.append(tmp)
    #         if (it - 5) >= 0 and (p - 5) >= 0:
    #             tmp = self.put_moins(it, p, nb2)
    #             nb2 += 1
    #             if tmp != ['a', 'a', 'a', 'a','a']:                
    #                 arr_str.append(tmp)
    #     if t == 'v':
    #         while it != 5:
    #             if self.map[y + it][x] == 'a':
    #                 self.x = x
    #                 self.y = y + it
    #                 self.add('o')

    # def first_a(self, nb, t):
    #     x = 0
    #     y = 0
    #     it = 0
    #     while y != self.size:
    #         x = 0
    #         while x != self.size:
    #             if (it == nb):
    #                 self.put_it(x, y, t)
    #             x += 1
    #             it += 1
    #         y += 1

    def put_around(self, y, x):
        if y + 1 < self.size:
            if self.map[y + 1][x] == 'a':
                self.x = x
                self.y = y + 1
                self.add('o')
                print("{0},{1}".format(self.x, self.y))
                sys.stdout.flush()
                self.command()
        if y - 1 >=  0:
            if self.map[y - 1][x] == 'a':
                self.x = x
                self.y = y - 1
                self.add('o')
                print("{0},{1}".format(self.x, self.y))
                sys.stdout.flush()
                self.command()
        if x + 1 < self.size:
            if self.map[y][x + 1] == 'a':
                self.x = x + 1
                self.y = y
                self.add('o')
                print("{0},{1}".format(self.x, self.y))
                sys.stdout.flush()
                self.command()
        if x - 1 >= 0:
            if self.map[y][x - 1] == 'a':
                self.x = x - 1
                self.y = y
                self.add('o')
                print("{0},{1}".format(self.x, self.y))
                sys.stdout.flush()
                self.command()

    def default(self):
        for y in range(len(self.map)):
            x = 0
            for x in range(len(self.map[y])):
                if self.map[y][x] == 'x':
                    self.put_around(y, x)
                x += 1
            y += 1
        for y in range(len(self.map)):
            x = 0
            for x in range(len(self.map[y])):
                if self.map[y][x] == 'a':
                    self.x = x
                    self.y = y
                    self.add('o')
                    print("{0},{1}".format(self.x, self.y))
                    sys.stdout.flush()
                    self.command()
                x += 1
            y += 1

# board to do error manage 2 virgule avec des int entre, 

if __name__ == '__main__':
    g = gomoku()
    g.init()
    exit(0)
