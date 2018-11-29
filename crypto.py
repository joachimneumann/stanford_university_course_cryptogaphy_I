#!/usr/bin/env python3

# datatype hex: list of N bytes as string
import sys
import binascii
from Crypto.Cipher import AES

def hexStringToHex(s):
    if len(s) / 2 * 2 != len(s):
        raise Exception("len not multiple of 2")
    hex = [s[2*i:2*i+2] for i in range(0, int(len(s)/2))]
    return hex

def asciiStringToHex(s):
    return binascii.unhexlify(s)

def hexToHexString(hex):
    return "".join(hex)

def hexToChr(hex):
    ret = ""
    for h in hex:
        n = int(h, 16)
        if n > 33:
            ret += chr(n)
        else:
            ret += " "
    return ret

def hexToBytes(hex):
    ba = bytearray()
    for h in hex:
        ba.append(int(h, 16))
    return bytes(ba)

def xor(hex1, hex2):
    l = min(len(hex1), len(hex2))
    ret = []
    for i in range(l):
        xor = int(hex1[i], 16) ^ int(hex2[i], 16)
        ret.append(format(xor, 'x'))
    return ret

from Crypto import Random

def CBC_encode_block(ivHex, keyHex, textHex): # cipher block chaining
    # key = b'Sixteen byte key'
    # iv = Random.new().read(AES.block_size)
    # cipher = AES.new(key, AES.MODE_CFB, iv)
    # msg = iv + cipher.encrypt(b'Attack at dawn')
    # print(msg)
    # plainText = cipher.decrypt(msg)
    # print(plainText[16:])

    if type(ivHex) != list:
        print("CBC_block wrong datatype in parameter ivHex")
        return
    if len(ivHex) != 16:
        print("iv not length 16 but "+str(len(ivHex)))
        return
    if type(textHex) != list:
        print("CBC_block wrong datatype in parameter textHex")
        return
    if len(textHex) != 16:
        print("text not length 16 but "+str(len(textHex)))
        return
    if type(keyHex) != list:
        print("CBC_block wrong datatype in parameter keyHex")
        return
    if len(keyHex) != 16:
        print("keyHex not length 16 but "+str(len(keyHex)))
        return
    inputToAES = xor(ivHex, textHex)
    iv = hexToBytes(ivHex)
    text = hexToBytes(textHex)
    print(text)
    key = hexToBytes(keyHex)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    msg = iv + cipher.encrypt(text)
    print(msg)
    plainText = cipher.decrypt(msg)
    print(plainText)
