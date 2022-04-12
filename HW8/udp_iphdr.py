import socket
import struct
import binascii

class UDPhdr:
    def __init__(self, srcpt, dstpt, len, chek):
        self.sourceport = srcpt
        self.destinationport = dstpt
        self.length = len
        self.checksum = chek

    def pack_UDPhdr(self):
        packed = b''
        packed += struct.pack('!H', self.sourceport)
        packed += struct.pack('!H', self.destinationport)
        packed += struct.pack('!H', self.length)
        packed += struct.pack('!H', self.checksum)
        return packed

def unpack_UDPhdr(buffer):
    unpacked = struct.unpack('!HHHH', buffer[:20])
    return unpacked
    
def getSrcPort(unpacked_ipheader):
    return unpacked_ipheader[0]

def getDstPort(unpacked_ipheader):
    return unpacked_ipheader[1]

def getLength(unpacked_ipheader):
    return unpacked_ipheader[2]

def getChecksum(unpacked_ipheader):
    return unpacked_ipheader[3]

ip = UDPhdr(5555, 80, 1000, 0xFFFF)
packed_iphdr = ip.pack_UDPhdr()
print(binascii.b2a_hex(packed_iphdr))

unpacked_iphdr = unpack_UDPhdr(packed_iphdr)
print(unpacked_iphdr)
print('Source Port:{} Destination Port:{} Port:{} Length:{}'\
    .format(getSrcPort(unpacked_iphdr), getDstPort(unpacked_iphdr), getLength(unpacked_iphdr), getChecksum(unpacked_iphdr)))