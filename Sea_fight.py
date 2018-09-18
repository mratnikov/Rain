import random
import copy

N = 10
null_field = [[0] * N for i in range(N)]
# ships = [0, 0, 0, 1]
ships = [0, 4, 3, 2, 1]


def print_field(f):
    print('')
    print('   abcdefghij')
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
            print(z, end='')
        print('')
    print('')


def print_enemy_field(f):
    print('')
    print('   abcdefghij')
    print('')
    for r in range(N):
        print('{:2} '.format(r + 1), end='')
        for c in range(N):
            z = '?'
            if f[r][c] == 2:
                z = '.'
            elif f[r][c] == 3:
                z = '*'
            print(z, end='')
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
        for l in range(len(ships) - 1, 0, -1):
            for i in range(ships[l]):
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
            if not ok:
                break
        if ok:
            return f
    assert False


def query_field():
    f = copy.deepcopy(null_field)
    print('Введите расположение ваших кораблей')
    for l in range(len(ships)):
        for i in range(ships[l]):
            while True:
                print_field(f)
                print('Размещаем ' + str(i + 1) + '-й ' + str(
                    l) + '-палубный корабль. Введите координаты левого верхнего угла (например, b 5) и направление (h или v):')
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


def is_lost(f):
    for r in f:
        for c in r:
            if c == 1:
                return False
    return True


def gen_move(f):
    for x in range(N):
        for y in range(N):
            if f[y][x] < 2:
                return x, y


def query_move(f):
    print_enemy_field(f)
    while True:
        print('Введите ваш ход (например, c 7):')
        try:
            x, y = input().split()
            x = 'abcdefghij'.index(x)
            y = int(y) - 1
        except:
            print('Неверный формат ввода')
            continue
        if f[y][x] >= 2:
            print('Вы уже сюда стреляли')
            continue
        return x, y


def game():
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
                print_field(uf)
                if is_lost(uf):
                    print('Вы проиграли...')
                    return
                continue


game()