import binascii
from array import array

poly = 0xEDB88320

table = array('L')
for byte in range(256):
    crc = 0
    for bit in range(8):
        if (byte ^ crc) & 1:
            crc = (crc >> 1) ^ poly
        else:
            crc >>= 1
        byte >>= 1
    table.append(crc)

def crc32(string):
    value = 0xffffffff
    for ch in string:
        value = table[(ord(ch) ^ value) & 0xff] ^ (value >> 8)

    return -1 - value

def Calculer(message):
    message=bytes(message,'UTF-8')
    resultat = binascii.crc32(message)
    crcCode='%08x' % (resultat & 0xffffffff)
    return str(crcCode)
