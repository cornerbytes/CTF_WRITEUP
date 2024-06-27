key = ["22","11","75","e1","66","12","0a","75","e1","66"]
key = ["76", "22", "99", "f2", "11", "67", "fe", "66"]

if __name__ == "__main__":
    key = [int(i, 16) for i in key]

    with open('enc.txt', 'rb') as f:
        enc_f = f.read()[:-1] # remove last byte
        enc_f = list(enc_f)

    flag = ''
    for i in range(len(enc_f)):
        flag += chr(enc_f[i] ^ key[i % len(key)])
    print(f'here flag : {flag}')
