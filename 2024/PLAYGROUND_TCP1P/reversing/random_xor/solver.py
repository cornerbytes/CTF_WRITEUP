import ctypes

libc = ctypes.CDLL('/lib/x86_64-linux-gnu/libm.so.6')

if __name__ == "__main__":
    enc_flag_name = 'flag_enc.txt'
    enc_flag = bytes()
    flag = ""
    
    with open(enc_flag_name, 'rb') as f:    
        enc_flag = f.read()
    
    seed_r = int.from_bytes(enc_flag[:4], byteorder='little') # read the seed value from the first 4 bytes
    enc_flag = enc_flag[4:]

    libc.srand(seed_r) # set seed

    for i in enc_flag:
        x = libc.rand() % 256 # char or unsigned int
        flag += chr(i^x)
        libc.rand() # using rand() for obfuscation

    print(f"seed : {seed_r}")
    print(f"here your flag : {flag}")
