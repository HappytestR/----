#-*-coding=utf-8
__version__='1.0.0'
__author__='named by Y'
import struct
import io
import sys
class SHA1:
    def __init__(self):
        self.__H = [       #设置临时寄存器，将5个32bit的常数赋给5个32bit的寄存器
            0x67452301,
            0xEFCDAB89,
            0x98BADCFE,
            0x10325476,
            0xC3D2E1F0
            ]
    def __str__(self):
        return ''.join((hex(h)[2:]).rjust(8, '0') for h in self.__H)
    @staticmethod
    def __ROTL(n, x, w=32):
        return ((x << n) | (x >> w - n))
    @staticmethod
    def __padding(stream):        #附加填充位
        l = len(stream)           #输入msg前以进行加码变为bytes
        hl = [int((hex(l*8)[2:]).rjust(16, '0')[i:i+2], 16)
              for i in range(0, 16, 2)]
        l0 = (56 - l) % 64    #附加消息为64bit，是消息的长度值
        if not l0:
            l0 = 64
        if isinstance(stream, str):       #isinstance判断是否为一个已知类型的常量,在这里判断是否为str类型的。
            stream += chr(0b10000000)
            stream += chr(0)*(l0-1)
            for a in hl:
                stream += chr(a)
        elif isinstance(stream, bytes):   #判断如果是bytes类型的，就在后面添加byte类型的。
            stream += bytes([0b10000000])
            stream += bytes(l0-1)
            stream += bytes(hl)
        return stream          #返回填充后的msg，进行第二部初始化缓存。
    @staticmethod
    def __prepare(stream):        #填充消息
        M = []
        n_blocks = len(stream) // 64
        stream = bytearray(stream)
        for i in range(n_blocks):  # 64 Bytes per Block
            m = []
            for j in range(16):  # 16 Words per Block
                n = 0
                for k in range(4):  # 4 Bytes per Word
                    n <<= 8
                    n += stream[i*64 + j*4 + k]
                m.append(n)
            M.append(m[:])
        return M
    @staticmethod
    def __debug_print(t, a, b, c, d, e):       #用于测试每轮的输出
        print('t = {0} : \t'.format(t),
              (hex(a)[2:]).rjust(8, '0'), #hex将10进制转化为16进制
              (hex(b)[2:]).rjust(8, '0'), #rjust右对齐，如果长度不够则填充0
              (hex(c)[2:]).rjust(8, '0'),
              (hex(d)[2:]).rjust(8, '0'),
              (hex(e)[2:]).rjust(8, '0')
              )
    def __process_block(self, block):   #进行SHA1压缩函数的运算
        MASK = 2**32-1
        W = block[:]
        for t in range(16, 80):
            W.append(SHA1.__ROTL(1, (W[t-3] ^ W[t-8] ^ W[t-14] ^ W[t-16]))
                     & MASK)
        a, b, c, d, e = self.__H[:]
        for t in range(80):          #压缩函数中非线性函数对3个32bit的变量B,C,D进行的操作
            if t <= 19:
                K = 0x5a827999
                f = (b & c) ^ (~b & d)
            elif t <= 39:
                K = 0x6ed9eba1
                f = b ^ c ^ d
            elif t <= 59:
                K = 0x8f1bbcdc
                f = (b & c) ^ (b & d) ^ (c & d)       #Kt在这里使用的是循环的额外常数，是固定的。
            else:
                K = 0xca62c1d6
                f = b ^ c ^ d
            T = ((SHA1.__ROTL(5, a) + f + e + K + W[t]) & MASK)
            e = d                                            #运算结束之后进行的循环赋值，即SHA1循环形式
            d = c
            c = SHA1.__ROTL(30, b) & MASK
            b = a
            a = T
            #SHA1.debug_print(t, a,b,c,d,e)
        self.__H[0] = (a + self.__H[0]) & MASK     #运算结束之后进行对缓冲区的更新赋值
        self.__H[1] = (b + self.__H[1]) & MASK
        self.__H[2] = (c + self.__H[2]) & MASK
        self.__H[3] = (d + self.__H[3]) & MASK
        self.__H[4] = (e + self.__H[4]) & MASK
    # Public methods for class use.
    def update(self, stream):
        stream = SHA1.__padding(stream)    #附加填充位
        stream = SHA1.__prepare(stream)
        for block in stream:
            self.__process_block(block)
    def digest(self):
        pass
    def hexdigest(self):   #返回5个寄存器中的值，即160bit的位数    160/4= 0x40(十六进制）
        s = ''
        for h in self.__H:
            s += (hex(h)[2:]).rjust(8, '0')
        return s
if  __name__=='__main__':
    test=SHA1()
    str1="123456"
    test.update(str1.encode('utf-8'))
    print(test.hexdigest())