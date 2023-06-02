# Capture The Flag (CTF)

## Description
### math
- Learn about the details of C language
- Read the file **math.c** in the **1-math** directory

### string
- Learn to use `string` and `base64` to find and decode the encoded string
- Inspect the binary file **string** in the **2-string** directory 

### random
- Learn about the glibc PRNG
- Inspect the file **random.c** in the **3-random** directory

### meow
- Learn about the file format
- Inspect the file **meow.jpg** in the **4-meow** directory to check whether there are some additional bytes

### return2flag
- Learn about stack buffer overflow
- Inspect the file **return2flag.c** in the **5-return2flag** directory to find where the buffer overflow can occur, and also bypass the return address check in it

### echooo
- Learn about format string vulnerability
- Inspect the file **echooo.c** in the **6-echooo** directory to decide which conversion specifier can modify the variable `canLogin`

## Usage
### Build
```bash
$ make
```

### math
```bash
$ cd 1-math && ./solve.py 140.113.207.243 8881
```

### string
```bash
$ cd 2-string && ./solve.py ./solve.sh
```

### random
```bash
$ cd 3-random && ./solve.py 140.113.207.243 8883
```

### meow
```bash
$ cd 4-meow && ./solve.py ./solve.sh
```

### return2flag
```bash
$ cd 5-return2flag && ./solve.py 140.113.207.243 8885
```

### echooo
```bash
$ cd 6-echooo && ./solve.py 140.113.207.243 8886
```