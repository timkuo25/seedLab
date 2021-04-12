c = ["00 11 22 33 44 55 66 77 88 99 aa bb cc dd ee ff",

"f9 47 39 24 bd 62 ba 19 f2 dd 19 c3 09 28 94 77",

"65 78 6c 8d 49 72 fd 13 2e c9 7a 3a 3e 51 81 91",

"76 52 a0 dc 44 cb 49 38 81 bd d8 41 10 3b 8b ca",

"2d 48 24 ee f5 4b 30 6f 09 3b dc 5a 17 dc 9f 46",

"a8 62 21 7e cb 6b 80 24 4f db a9 0f bb 13 c7 2b",

"ab 3d e8 d9 65 3b e2 1d 63 5a 0f 8d 59 71 28 36",

"06 eb 64 c0 fb b9 22 af d9 db 00 7f 94 fb 9e 24",

"a8 99 a6 c0 a6 5b 68 7b 85 f4 5d 48 40 d4 7d f4",
]

host = 'http://140.122.185.210:8080/oracle/'

# modify prefix and the target
front = "00000000000000000000000000000000\
00000000000000000000000000000000\
00000000000000000000000000000000\
00000000000000000000000000000000\
00000000000000000000000000000000\
00000000000000000000000000000000"
target = "06eb64c0fbb922afd9db007f94fb9e24"

mid = ['00'] * 16
mie = ['00'] * 16

import requests
import time

for i in range(1,17):
	for j in range(256):
		test = "".join(mid[0: 16 - i]) + format(j, '02x') + "".join(mie[17 - i:])
		
		r = requests.get(host + front + test + target)
		if r.text == "valid":
			mid[16 - i] = format(int(format(j, '02x'),16)^i, '02x')
			print(mid[16 - i])
			
			for k in range(16):
				mie[k] = format(int(mid[k],16)^(i + 1), '02x')
			break
print(" ".join(mid))

#for decryption after getting mid value

inter = mid

# modify for each block
IV = c[6].split()

m = []
for i in range(len(IV)):
	IV[i] = int(IV[i], 16)
	inter[i] = int(inter[i], 16)
	m.append(chr(IV[i] ^ inter[i]))
print("".join(m))

# message: If you don't know where you want to go, then it doesn't matter which path you take. Lewis Carroll, Alice in Wonderland
