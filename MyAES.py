#!/usr/bin/env python3
from Crypto.Cipher import AES
import math

EDB_cipher = 0
def setKey(key):
    global EDB_cipher
    EDB_cipher = AES.new(key, AES.MODE_ECB)

def pad(s):
    blocks = math.floor(len(s)/16)
    padding = 16*(blocks+1)-len(s)

    if padding == 0:
        padding = 16
    for p in range(0,padding):
        s += bytes([padding])
    return s

def unpad(s):
    lastByte = s[-1]
    return s[0:len(s)-lastByte]

def bxor(b1, b2): # use xor for bytes
    parts = []
    for b1, b2 in zip(b1, b2):
        parts.append(bytes([b1 ^ b2]))
    return b''.join(parts)

def CBC_encode_block(plainText):
    return EDB_cipher.encrypt(plainText)

def CBC_decode_block(cipherText):
    return EDB_cipher.decrypt(cipherText)

def CBC_encode(iv, plainText):
    padded = pad(plainText)
    blocks = int(len(padded)/16)
    cipherText = b''
    previous = iv
    for b in range(blocks):
        blockText = padded[16*b:16*(1+b)]
        xorText = bxor(blockText, previous)
        previous = CBC_encode_block(xorText)
        cipherText += previous
    return iv+cipherText

def CBC_decode(cipherText):
    blocks = int(len(cipherText)/16)
    plainText = b''
    for b in range(blocks-1):
        block         = cipherText[16*(blocks-b-1):16*(blocks-b  )]
        previousBlock = cipherText[16*(blocks-b-2):16*(blocks-b-1)]
        decodedXorBlock = CBC_decode_block(block)
        decodedBlock = bxor(decodedXorBlock, previousBlock)
        plainText = decodedBlock + plainText
    return unpad(plainText)

def CTR_encode(iv, plainText):
    padded = pad(plainText)
    blocks = int(len(padded)/16)
    cipherText = b''
    counter = int.from_bytes(iv, 'big')
    for b in range(blocks):
        blockText = padded[16*b:16*(1+b)]
        f_counter = CBC_encode_block(counter.to_bytes(16, byteorder='big'))
        xorText = bxor(blockText, f_counter)
        counter = counter + 1
        cipherText += xorText
    return iv+cipherText

def CTR_decode(cipherText):
    blocks = int(len(cipherText)/16)
    plainText = b''
    iv = cipherText[0:16]
    counter = int.from_bytes(iv, 'big')
    print("counter = {}".format(counter))
    for b in range(blocks):
        blockText = cipherText[16*(b+1):16*(b+2)]
        print("blockText = {}".format(blockText))
        f_counter = CBC_encode_block(counter.to_bytes(16, byteorder='big'))
        print("f_counter = {}".format(f_counter))
        xorText = bxor(blockText, f_counter)
        print("xorText = {}".format(xorText))
        counter = counter + 1
        print("counter = {}".format(counter))
        plainText += xorText
        print("plainText = {}".format(plainText))
    print("plainText = {}".format(plainText))
    return unpad(plainText)
