#-*-coding=utf-8
__version__='1.0.0'
__author__='named by Y'
import base64
class RC4:
    def __init__(self):            #初始化RC4算法
        self.key='the_none_key'
        self.Sbox=list(range(256))
    def set_key(self,key):       #设置密钥
        if key!='':
            self.key=key
    def init_S(self):              #初始化S盒
        s_box=list(range(256))
        j=0
        for i in range(256):
            j=(j+s_box[i]+ord(self.key[i%len(self.key)]))%256
            s_box[i],s_box[j]=s_box[j],s_box[i]
        self.Sbox=s_box
    def encry(self,msg):               #对明文msg进行解密
        self.init_S()                  #初始化S盒
        res=[]                         #对明文开始进行加密
        i=j=0
        for s in msg:
            i=(i+i)%256
            j=(j+self.Sbox[i])%256
            self.Sbox[i],self.Sbox[j]=self.Sbox[j],self.Sbox[i]
            t=(self.Sbox[i]+self.Sbox[j])%256
            k=self.Sbox[t]
            res.append(chr(ord(s)^k))
        cipher=''.join(res)
        return cipher
    def dencry(self,key,cipher):
        self.set_key(key)
        self.init_S()
        plain=self.encry(cipher)
        return plain