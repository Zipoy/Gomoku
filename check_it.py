import sys

def check_int(self, nb):
    try:
        tmp = int(nb)
        return (tmp)
    except ValueError:
        print("ERROR must be an int", flush=True)
        self.command()

def check_start(self, nb):
    try:
        tmp = int(nb)
        return (tmp)
    except ValueError:
        print("ERROR message - unsupported size or other error", flush=True)
        self.command()

def check_cmd(self, line):
    array = ["START", "TURN", "BOARD", "INFO", "END", "ABOUT", "BEGIN"]
    for i in array:
        if line[0].replace("\n", '') == i:
            return True
    print("UNKNOWN command not found", flush=True)
    return False

# def check_h(self, fo):
#     tmp1 = 0
#     tmp2 = 0
#     for i in self.map:
#         for y in i:
#             if y == 'o':
#                 tmp1 += 1
#                 if tmp1 == fo:
#                     return 'o'
#             else:
#                 tmp1 = 0
#             if y == 'x':
#                 tmp2 += 1
#                 if tmp2 == fo:
#                     return 'x'
#             else:
#                 tmp2 = 0
#     return 'a'

def take_h(self, y, x, nb):
    tmp = []
    it = 0
    while it != 5:
        tmp += self.map[y][x + it]
        it += 1
    return (tmp, nb)

def take_v(self, y, x, nb):
    tmp = []
    it = 0
    while it != 5:
        tmp += self.map[y + it][x]
        it += 1
    return (tmp, nb)

def check_h(self):
    arr_str = []
    it = 0
    nb = 0
    p = 0
    while it != self.size:
        p = 0
        while p != self.size:
            if (p + 5) < self.size:
                tmp = take_h(self, it, p, nb)
                nb += 1
                if tmp != ['a', 'a', 'a', 'a','a']:
                    arr_str.append(tmp)
            p += 1
        it += 1
    for i in arr_str:
        if i[0] == ['a','o','o','o','o'] or i[0] == ['o','o','o','o','a']:
            return i[1]
    return 0

def check_v(self):
    nb = 0
    arr_str = []
    it = 0
    p = 0
    while it != self.size:
        p = 0
        while p != self.size:
            if (it + 5) < self.size:
                tmp = take_v(self, it, p, nb)
                nb += 1
                if tmp != ['a', 'a', 'a', 'a','a']:
                    arr_str.append(tmp)
            p += 1
        it += 1
    for i in arr_str:
        if i[0] == ['a','o','o','o','o'] or i[0] == ['o','o','o','o','a']:
            return i[1]
    return 0

# def check_v(self):
#     tmp1 = 0
#     tmp2 = 0
#     for i in range(0, self.size):
#         for y in range(0, self.size):
#             if self.map[y][i] == 'o':
#                 tmp1 += 1
#                 if tmp1 == 5:
#                     return 'o'
#             else:
#                 tmp1 = 0
#             if self.map[y][i] == 'x':
#                 tmp2 += 1
#                 if tmp2 == 5:
#                     return 'x'
#             else:
#                 tmp2 = 0
#     return 'a'

def check_d(self):
    arr_str = []
    it = 0
    nb = 0
    nb2 = 0
    p = 0
    while it != self.size:
        p = 0
        while p != self.size:
            if (it + 5) < self.size and (p + 5) < self.size:
                tmp = self.put_plus(it, p, nb)
                nb += 1
                if tmp != ['a', 'a', 'a', 'a','a']:
                    arr_str.append(tmp)
            if (it - 5) >= 0 and (p - 5) >= 0:
                tmp = self.put_moins(it, p, nb2)
                nb2 += 1
                if tmp != ['a', 'a', 'a', 'a','a']:                
                    arr_str.append(tmp)
            p += 1
        it += 1
    for i in arr_str:
        if i[0] == ['a','o','o','o','o']:
            return i[1]
        if i[0] == ['o','o','o','o','a']:
            return i[1]
    return 0

#  if size < MIN_BOARD / 5 or size > MAX_BOARD / 100:
#         misc.printToProgram("ERROR message - Given size is {} but must be >= {} and <= {}".format(size, MIN_BOARD, MAX_BOARD))
#         sys.exit(84)

#il faut surement pas check qui gagne des deux joueurs mais seulement jouer le check win est simplement pour tester
def check_win(self):
    h = check_h(self)
    v = check_v(self)
    d = check_d(self)
    for i in (h,v,d):
        if i > 0:
            self.win == 1
            exit(0)