#!/usr/bin/python3

import pwn
import sys


if __name__ == '__main__':
	answer, target = 0, None

	if len(sys.argv) < 2:
		print(f'usage: {__file__} <filename>')
		exit(1)
	elif len(sys.argv) != 3:
		target = pwn.process(sys.argv[1])				# use local file
	else:
		server, port = sys.argv[1], int(sys.argv[2])
		target = pwn.remote(server, port)				# connect to the server

	print(target.recvall().decode("utf-8", "ignore").strip())
