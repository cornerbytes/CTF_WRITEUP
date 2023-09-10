from pwn import *

DATA = []

def find_num_1(data):
    res = []
    for idx, val in enumerate(data):
        for j, val_2 in enumerate(val):
            if val_2 == 1:
                res.append((idx, j))
    return res

def read_data(p):
    data = p.recvuntil(b'\n\n').decode().replace('\n\n', '').split('\n')
    data = [i.split(' ') for i in data]
    data = [list(map(int, i)) for i in data]
    return data

def search(matrix, sip):
    target = sip + 1 
    x, y = matrix

    # Kanan 
    if (y + 1 != 50) and (DATA[x][y+1] == target):
        return (x, y+1)
    
    # kiri
    if (y - 1 != -1) and (DATA[x][y-1] == target):
        return (x, y-1)

    # bawah
    if (x + 1 != 50) and (DATA[x+1][y] == target):
        return (x+1, y)

    # atas
    if (x - 1 != -1) and (DATA[x-1][y] == target):
        return (x-1, y)

    # kanan atas
    if (y + 1 != 50) and (x - 1 != -1):
        if DATA[x-1][y+1] == target:
            return (x-1, y+1)

    # kanan bawah
    if (y + 1 != 50) and (x + 1 != 50):
        if DATA[x+1][y+1] == target:
            return (x+1, y+1)
    
    # kiri atas
    if (y - 1 != -1) and (x -1 != -1):
        if DATA[x-1][y-1] == target:
            return (x-1, y-1)
    # kiri bawah 
    if (y -1 != -1) and (x +1 != 50):
        if DATA[x+1][y-1] == target:
            return (x+1, y-1)

    return False

def calculate(res):
    sip = 1
    while True:
        if any(res) == False:
            return sum(range(1, sip))
        res = [search(i, sip) for i in res if type(i) != bool]
        sip += 1

if __name__ == "__main__":
    p = remote("103.152.242.235", 26693)
    p.recv()

    while True:
        try:
            p.recvline()
            DATA = []
            DATA.extend(read_data(p))
            res = find_num_1(DATA)
            res = calculate(res)
            p.recv()
            p.sendline(str(res).encode())
            print(res)
        except EOFError:
            print('jawaban error coba lagi')
            break
        except ValueError as e:
            print(e, type(e))
            break
