Threads are so cool! And secure! So secure that I store all my secrets there
Note 1: The flag is broken into chunks of 4 characters, like this:
`volatile __thread unsigned int flag1 = 'CCFT';`
The letters in the chunks are reversed for your convenience, and the chunks are defined in order. There are 6 chunks of 4 characters.
Note 2: The binary is intentionally not given.
Note 3: The program will read 0x1000 bytes of shellcode, stored into a mmap-ed region with RWX permissions

What is the flag?