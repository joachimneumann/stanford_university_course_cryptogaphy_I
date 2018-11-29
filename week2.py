#!/usr/bin/env python3

import sys
from MyAES import *
from binascii import hexlify, unhexlify

# iv         = b'0123456789abcdef'
# key        = unhexlify("36f18357be4dbd77f050515c73fcf9f2")
# plainText  = b'this is a test 1'
#
# print("plainText = {}".format(plainText))
# cipherText = CBC_encode_block(plainText)
# print("cipherText = {}".format(cipherText))
# decodedText = CBC_decode_block(cipherText)
# print("decodedText = {}".format(decodedText))

# plainText  = b'Yes, as I state above, this logic pads with nulls'
# print("plainText = {}".format(plainText))
# cipherText = CBC_encode(iv, plainText)
# cipherTextHex = "5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253"
# cipherText = unhexlify(cipherTextHex)
# print("cipherText = {}".format(cipherText))
# decodedText = CBC_decode(cipherText)
# print("decodedText = {}".format(decodedText))

# cipherText = CTR_encode(iv, plainText)



setKey(unhexlify("140b41b22a29beb4061bda66b6747e14"))
cipherText = unhexlify("4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81")
print(CBC_decode(cipherText))
cipherText = unhexlify("5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253")
print(CBC_decode(cipherText))
setKey(unhexlify("36f18357be4dbd77f050515c73fcf9f2"))
cipherText = unhexlify("69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329")
print(CTR_decode(cipherText))
cipherText = unhexlify("770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451")
print(CTR_decode(cipherText))
