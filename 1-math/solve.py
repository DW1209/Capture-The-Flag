#!/usr/bin/python3

import pwn
import sys


if __name__ == '__main__':
	answer, number, target = 0, b'-1', None

	if len(sys.argv) < 2:
		print(f'usage: {__file__} <ip> <port>')
		exit(1)
	elif len(sys.argv) != 3:
		target = pwn.process(sys.argv[1])				# use local file
	else:
		server, port = sys.argv[1], int(sys.argv[2])
		target = pwn.remote(server, port)				# connect to the server

	target.sendline(number)
	print(target.recvall().decode("utf-8", "ignore").strip())
