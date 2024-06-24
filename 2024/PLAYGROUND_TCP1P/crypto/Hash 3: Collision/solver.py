from pwn import *

def solver(x: int):
    # d= 100
    pw = 'd'*(x//100)
    pw += chr(x%100)
    return pw

if __name__ == "__main__":
    p = remote('172.188.90.64', '21001')
    admin_pw = int(bytes.fromhex("32323931"))
    admin_pw = solver(admin_pw)
    print(f"admin password = {admin_pw}")
    
    p.recv()
    p.sendline(b'1')
    p.recv()
    p.sendline(b'admin')
    p.recv()
    p.sendline(admin_pw.encode())
    p.recv()
    p.sendline(b'1')
    print(p.recv().decode())
