import random
import copy

N = 10
null_field = [[0] * N for i in range(N)]
# ships = [3]
ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]


def print_field(f):
    print('')
    print('   a b c d e f g h i j')
    print('')
    for r in range(N):
        print('{:2} '.format(r + 1), end='')
        for c in range(N):
            z = '?'
            if f[r][c] == 0:
                z = '.'
            elif f[r][c] == 1:
                z = '#'
            elif f[r][c] == 2:
                z = '*'
            elif f[r][c] == 3:
                z = 'X'
            print(z, end=' ')
        print('')
    print('')


def print_enemy_field(f):
    print('')
    print('   a b c d e f g h i j')
    print('')
    for r in range(N):
        print('{:2} '.format(r + 1), end='')
        for c in range(N):
            z = '?'
            if f[r][c] == 2:
                z = '.'
            elif f[r][c] == 3:
                z = '*'
            print(z, end=' ')
        print('')
    print('')


def can_place(f, l, x, y, dx, dy):
    if x + dx * (l - 1) >= N or y + dy * (l - 1) >= N:
        return False
    for j in range(l):
        for zx in range(-1, 2):
            for zy in range(-1, 2):
                nx = x + dx * j + zx
                ny = y + dy * j + zy
                if nx >= 0 and ny >= 0 and nx < N and ny < N and f[ny][nx] != 0:
                    return False
    return True


def place_ship(f, l, x, y, dx, dy):
    for j in range(l):
        nx = x + dx * j
        ny = y + dy * j
        f[ny][nx] = 1


def gen_field():
    it1 = 10
    while it1 > 0:
        it1 -= 1
        ok = True
        f = copy.deepcopy(null_field)
        for i in range(len(ships)):
            l = ships[i]
            it = 20
            ok = False
            while it > 0 and not ok:
                it -= 1
                x = random.randrange(N)
                y = random.randrange(N)
                dx = random.randrange(2)
                dy = 1 - dx
                if can_place(f, l, x, y, dx, dy):
                    ok = True
            if not ok:
                break
            place_ship(f, l, x, y, dx, dy)
        if ok:
            return f
    assert False


def query_field():
    f = copy.deepcopy(null_field)
    print('Введите расположение ваших кораблей')
    for i in range(len(ships)):
        l = ships[i]
        while True:
            print_field(f)
            print('Размещаем ' + str(i + 1) + '-й корабль: ' + str(
                l) + '-палубный. Введите координаты левого верхнего угла (например, b 5) и направление (h или v):')
            try:
                x, y, v = input().split()
                x = 'abcdefghij'.index(x)
                y = int(y) - 1
            except:
                print('Неверный формат ввода')
                continue
            if v == 'h':
                dx, dy = 1, 0
            elif v == 'v':
                dx, dy = 0, 1
            else:
                continue
            if not can_place(f, l, x, y, dx, dy):
                print('Не удалось разместить корабль')
                continue
            place_ship(f, l, x, y, dx, dy)
            break
    return f


def is_dead(f, x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    for k in range(4):
        tx, ty = x, y
        while tx >= 0 and tx < N and ty >= 0 and ty < N:
            if f[ty][tx] == 1:
                return False
            if f[ty][tx] == 0 or f[ty][tx] == 2:
                break
            tx, ty = tx + dx[k], ty + dy[k]
    return True


def is_ship_possible(f, x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    if f[y][x] >= 2:
        return False
    for tx in range(x - 1, x + 2):
        for ty in range(y - 1, y + 2):
            if tx >= 0 and tx < N and ty >= 0 and ty < N:
                if f[ty][tx] == 3 and is_dead(f, tx, ty):
                    return False
    return True


def is_lost(f):
    for r in f:
        for c in r:
            if c == 1:
                return False
    return True


lx, ly = -1, -1
mode = 1


def gen_move(f):
    global lx, ly, mode
    if (lx, ly) != (-1, -1) and f[ly][lx] == 3 and not is_dead(f, lx, ly):
        l = []
        if (lx > 0 and f[ly][lx - 1] == 3) or (lx < N - 1 and f[ly][lx + 1] == 3):
            dx, dy = [-1, 1], [0, 0]
        elif (ly > 0 and f[ly - 1][lx] == 3) or (ly < N - 1 and f[ly + 1][lx] == 3):
            dx, dy = [0, 0], [-1, 1]
        else:
            dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
        for k in range(len(dx)):
            tx, ty = lx, ly
            while tx >= 0 and tx < N and ty >= 0 and ty < N:
                if f[ty][tx] < 2:
                    l += [(tx, ty)]
                    break
                elif f[ty][tx] == 2:
                    break
                tx, ty = tx + dx[k], ty + dy[k]
        return random.choice(l)
    else:
        if mode == 0:
            l = []
            for x in range(N):
                for y in range(N):
                    if f[y][x] < 2:
                        if is_ship_possible(f, x, y):
                            l += [(x, y)]
            return random.choice(l)
        elif mode == 1:
            o = []
            o += [(i, i) for i in range(10)]
            for t in [3, 6, 9, 2, 5, 8, 1, 4, 7]:
                o += [(i, i + t) for i in range(10 - t)]
                o += [(i + t, i) for i in range(10 - t)]
            for p in o:
                x, y = p
                if f[y][x] < 2:
                    if is_ship_possible(f, x, y):
                        return p


def query_move(f):
    print_enemy_field(f)
    while True:
        print('Введите ваш ход (например, c 7):')
        try:
            x, y = input().split()
            x = 'abcdefghij'.index(x)
            y = int(y) - 1
            if f[y][x] >= 2:
                print('Вы уже сюда стреляли')
                continue
        except:
            print('Неверный формат ввода')
            continue
        return x, y


def game():
    global lx, ly
    cf = gen_field()
    uf = query_field()
    move = 0
    while True:
        if move == 0:
            x, y = query_move(cf)
            if cf[y][x] == 0:
                print('Вы промахнулись')
                cf[y][x] = 2
                move = 1
                continue
            elif cf[y][x] == 1:
                print('Вы попали!')
                cf[y][x] = 3
                if is_dead(cf, x, y):
                    print('Убит!')
                else:
                    print('Ранен!')
                if is_lost(cf):
                    print('Вы выиграли!')
                    return
                continue
        else:
            x, y = gen_move(uf)
            print('Соперник стреляет в клетку ' + 'abcdefghij'[x] + ' ' + str(y + 1))
            if uf[y][x] == 0:
                print('Соперник промахнулся')
                uf[y][x] = 2
                print_field(uf)
                move = 0
                continue
            elif uf[y][x] == 1:
                print('Соперник попал')
                uf[y][x] = 3
                lx, ly = x, y
                if is_dead(uf, x, y):
                    print('Убит...')
                else:
                    print('Ранен')
                print_field(uf)
                if is_lost(uf):
                    print('Вы проиграли...')
                    return
                continue


game()