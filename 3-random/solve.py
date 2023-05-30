#!/usr/bin/python3

import pwn
import sys
import pytz
import datetime
import subprocess


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
	
	info = target.recvuntil(b'password: ').decode("utf-8", "ignore").strip()
	data = info.split(' >')[0].split(':')
	hour, minute, second = int(data[0]), int(data[1]), int(data[2])

	date = datetime.date.today()
	twn  = datetime.datetime.combine(date, datetime.time(hour, minute, second))
	utc  = twn.astimezone(pytz.utc)

	start = datetime.datetime(1970, 1, 1, tzinfo=pytz.utc)
	total = (utc - start).total_seconds()

	command = ['./getnum', str(total)]
	number = subprocess.run(command, stdout=subprocess.PIPE).stdout.strip()
	target.sendline(number)
	
	print(f'{info} {number.decode("utf-8")}')
	print(target.recvall().decode("utf-8", "ignore").strip())
