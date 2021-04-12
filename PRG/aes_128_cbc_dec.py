#!/usr/bin/python3
from Crypto.Cipher import AES

plaintext = bytearray.fromhex("255044462d312e350a25d0d4c5d80a34")
ciphertext = bytearray.fromhex("d06bf9d0dab8e8ef880660d2af65aa82")
iv = bytearray.fromhex("09080706050403020100A2B2C2D2E2F2")

f = open("keylist.txt", "r")

for k in f:
    cipher = AES.new(key=bytearray.fromhex(k), mode=AES.MODE_CBC, iv=iv)
    guess = cipher.encrypt(plaintext)
    if guess == ciphertext:
        print("key found:", k)
        break
f.close()
