import sys

def check_NxtMoove(self):
    moove = None
    for pat in self.pattern:
        for y in range(0, self.size):
            for x in range(0, self.size):
                if self.map[y][x] == 'x' or self.map[y][x] == 'o':
                    moove = check_all(self, y, x, pat)
                    if moove != None:
                        self.x = moove[0]
                        self.y = moove[1]
                        self.add('o')
                        print("{0},{1}".format(self.x, self.y))
                        sys.stdout.flush()
                        self.command()
    if moove == None:
        self.default()

#check si il n'y a pas 1000 pion qui block le coup et empecherai de faire un x5
#surrement pb de inversion check que d'un seul coté
 #exemple si ooax alors non si ooaax non si ooaaax oui
def check_moove(self, moove, pat):
    i = 0
    check = False
    x = moove[0]
    y = moove[1]
    if moove[2] == 1:
        if moove[3] == 1:
            while i != len(pat):
                if pat[i] == 'a':
                    check = True
                    if i + 1 != len(pat):
                        x += 1
                        i += 1
                    else:
                        return True
                    continue
                if check == True:
                    if pat[i] == self.map[y][x]:
                        x += 1
                        i += 1
                        continue
                    else:
                        return False
                i += 1
        if moove[3] == 2:
            while i != len(pat):
                if pat[i] == 'a':
                    check = True
                    if i + 1 != len(pat):
                        x -= 1
                        i += 1
                    else:
                        return True
                    continue
                if check == True:
                    if pat[i] == self.map[y][x]:
                        x -= 1
                        i += 1
                        continue
                    else:
                        return False
                i += 1
    elif moove[2] == 2:
        if moove[3] == 1:
            while i != len(pat):
                if pat[i] == 'a':
                    check = True
                    if i + 1 != len(pat):
                        i += 1
                        y += 1
                        continue
                    else:
                        return True
                if check == True:
                    if pat[i] == self.map[y][x]:
                        y += 1
                        i += 1
                        continue
                    else:
                        return False
                i += 1
        if moove[3] == 2:
            while i != len(pat):
                if pat[i] == 'a':
                    check = True
                    if i + 1 != len(pat):
                        i += 1
                        y -= 1
                        continue
                    else:
                        return True
                if check == True:
                    if pat[i] == self.map[y][x]:
                        y -= 1
                        i += 1
                        continue
                    else:
                        return False
                i += 1
    elif moove[2] == 3:
        if moove[3] == 1:
            while i != len(pat):
                if pat[i] == 'a':
                    check = True
                    if i + 1 != len(pat):
                        y += 1
                        x += 1
                        i += 1
                    else:
                        return True
                    continue
                if check == True:
                    if pat[i] == self.map[y][x]:
                        y += 1
                        x += 1
                        i += 1
                        continue
                    else:
                        return False
                i += 1
        if moove[3] == 2:
            while i != len(pat):
                if pat[i] == 'a':
                    check = True
                    if i + 1 != len(pat):
                        y -= 1
                        x -= 1
                        i += 1
                    else:
                        return True
                    continue
                if check == True:
                    if pat[i] == self.map[y][x]:
                        y -= 1
                        x -= 1
                        i += 1
                        continue
                    else:
                        return False
                i += 1
    elif moove[2] == 4:
        if moove[3] == 1:
            while i != len(pat):
                if pat[i] == 'a':
                    check = True
                    if i + 1 != len(pat):
                        y += 1
                        x -= 1
                        i += 1
                    else:
                        return True
                    continue
                if check == True:
                    if pat[i] == self.map[y][x]:
                        y += 1
                        x -= 1
                        i += 1
                        continue
                    else:
                        return False
                i += 1
        if moove[3] == 2:
            while i != len(pat):
                if pat[i] == 'a':
                    check = True
                    if i + 1 != len(pat):
                        y -= 1
                        x += 1
                        i += 1
                    else:
                        return True
                    continue
                if check == True:
                    if pat[i] == self.map[y][x]:
                        y -= 1
                        x += 1
                        i += 1
                        continue
                    else:
                        return False
                i += 1
    return True

                
#     size = 0 #size patern
#     moove[4] == + ou - (de quel coté il faut regarder)
#     moove[3] == attack ou defense
#     if moove[2] == 1: #'h'
#         #check si oui ou non c'est viable en fonction de la tailler du pattern
#     elif moove[2] == 2: #'v'
#     elif moove[2] == 3: #'d up'
#     elif moove[2] == 4: #'d down'

#     return False

def check_hor(self, y, x, pat):
    if x + len(pat) < self.size:
        for p in range(x, x + len(pat)):
            it = p - x
            if self.map[y][p] == pat[it]:
                if self.map[y][p] == 'a':
                    return (p, y, 1, 1)
                else:
                    continue
            else:
                break
    if x - len(pat) >= 0:    
        for p in range(x, x - len(pat), -1):
            it = p - x
            if self.map[y][p] == pat[-it]:
                if self.map[y][p] == 'a':
                    return (p, y, 1, 2)
                else:
                    continue
            else:
                break
    return None


def check_ver(self, y, x, pat):
    if y + len(pat) < self.size:
        for p in range(y, y + len(pat)):
            it = p - y
            if self.map[p][x] == pat[it]:
                if self.map[p][x] == 'a':
                    return (x, p, 2, 1)
                else:
                    continue
            else:
                break
    if y - len(pat) >= 0:
        for p in range(y, y - len(pat), -1):
            it = p - y
            if self.map[p][x] == pat[-it]:
                if self.map[p][x] == 'a':
                    return (x, p, 2, 2)
                else:
                    continue
            else:
                break
    return None
#reuturn NONE + - range -1 + -it
def check_diagup(self, y, x, pat):
    if y + len(pat) < self.size and x + len(pat) < self.size:
        it = 0
        tmp = y
        tmp2 = x
        while it != len(pat):
            if self.map[tmp][tmp2] == pat[it]:
                if self.map[tmp][tmp2] == 'a':
                    return (tmp2, tmp, 3, 1)
                else:
                    it += 1
                    tmp += 1
                    tmp2 += 1
                    continue
            else:
                break
    if y - len(pat) >= 0 and x - len(pat) >= 0:
        it = 0
        tmp = y
        tmp2 = x
        while it != len(pat):
            if self.map[tmp][tmp2] == pat[it]:
                if self.map[tmp][tmp2] == 'a':
                    return (tmp2, tmp, 3, 2)
                else:
                    it += 1
                    tmp -= 1
                    tmp2 -= 1
                    continue
            else:
                break
    return None


def check_diagdown(self, y, x, pat):
    if y + len(pat) < self.size and x - len(pat) >= 0:
        it = 0
        tmp = y
        tmp2 = x
        while it != len(pat):
            if self.map[tmp][tmp2] == pat[it]:
                if self.map[tmp][tmp2] == 'a':
                    return (tmp2, tmp, 4, 1)
                else:
                    it += 1
                    tmp += 1
                    tmp2 -= 1
                    continue
            else:
                break
    if y - len(pat) >= 0 and x + len(pat) < self.size:
        it = 0
        tmp = y
        tmp2 = x
        while it != len(pat):
            if self.map[tmp][tmp2] == pat[it]:
                if self.map[tmp][tmp2] == 'a':
                    return (tmp2, tmp, 4, 2)
                else:
                    it += 1
                    tmp -= 1
                    tmp2 += 1
                    continue
            else:
                break
    return None


# def check_v(self, y, x, pat):
#     if y + len(pat) > self.size:
#     for p in range(y, y + len(pat)):
#         it = p - x
#         if self.map[y][p] == pat[it]:
#             if self.map[y][p] == 'a':
#                 return (x, y, 1)
#             else:
#                 continue
#         else:
#             break
#     return None

def check_pat(self, moove, pat):
    if pat == ['x','x','a','x'] or pat == ['o','o','a','o']:
        if moove[2] == 1 and moove[3] == 1:
            if moove[0] + 2 < self.size:
                if self.map[moove[1]][moove[0] + 2] != 'a':
                    return False
            else:
                return False
        elif moove[2] == 1 and moove [3] == 2:
            if moove[0] - 2 >= 0:
                if self.map[moove[1]][moove[0] - 2] != 'a':
                    return False
            else:
                return False
        if moove[2] == 2 and moove[3] == 1:
            if moove[1] + 2 < self.size:
                if self.map[moove[1] + 2][moove[0]] != 'a':
                    return False
            else:
                return False
        elif moove[2] == 2 and moove[3] == 2:
            if moove[1] - 2 >= 0:
                if self.map[moove[1] - 2][moove[0]] != 'a':
                    return False
            else:
                return False
    return True


def check_all(self, y, x, pat):
    moove = check_hor(self, y, x, pat)
    if moove != None and check_moove(self, moove, pat) == True:
        return moove
    moove = check_ver(self, y, x, pat)
    if moove != None and check_moove(self, moove, pat) == True:
        return moove
    moove = check_diagup(self, y, x, pat)
    if moove != None and check_moove(self, moove, pat) == True:
        return moove
    moove = check_diagdown(self, y, x, pat)
    if moove != None and check_moove(self, moove, pat) == True:
        return moove
    return None