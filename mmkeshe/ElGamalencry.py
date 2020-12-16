#-*-coding=utf-8
__version__='1.0.0'
__author__='named by Y'
import random
from math import pow   #计算幂次
class EGencry:        #ElGamalencry椭圆加密算法
    def __init__(self):                              #初始化一个加密算法时变初始化了公钥和私钥
        self.randoma=random.randint(2,10)
        self.pubp=random.randint(pow(10,20),pow(10,50))     #生成大素数p
        self.pubg=random.randint(2,self.pubp)               #生成一个随机数g
        self.pri=self.gen_key(self.pubp)                    #生成私钥d
        self.pub=self.power(self.pubg,self.pri,self.pubp)                    #用私钥生成公钥pub=g^d
        #print('欢迎使用ElGamalencry加密算法!,调用一次变初始化大素数p和私钥d！')
    def gcd(self,a,b):             #辗转相除法求最小公约数
        if a<b:
            return self.gcd(b,a)
        elif a%b==0:
            return b
        else:
            return self.gcd(b,a%b)
    def gen_key(self,max):      #密钥生成(私钥的生成）
        if max<pow(10,20):
            print('error,the mode is not the security!')
        key=random.randint(pow(10,20),max)
        while self.gcd(max,key)!=1:
            key=random.randint(pow(10,20),max)
        return key
    def power(self,a,b,c):                   #求幂的运算，即(a^b%c),使用了莫平方重复算法来计算
        x=1
        y=a
        while b > 0:
            if b%2==0:
                x=(x*y)%c
                y=(y*y)%c
            b=int(b/2)
        return x%c
    def show_pub(self):
        str1=""
        str1="初始化生成的公钥为：（y,g,p)="+str1+"("+str(self.pub)+","+str(self.pubg)+","+str(self.pubp)+")\n"
        #print('初始化生成的公钥为：(y,g,p)=（{}，{}，{}）'.format(self.pub,self.pubg,self.pubp))
        return str1
    def encry(self,msg):
        cipher=[]
        pubr=self.gen_key(self.pubp)                     #生成r
        s=self.power(self.pubg,pubr,self.pubp)            #求解g^rmodp
        p=self.power(self.pub,pubr,self.pubp)             #求解y^rmodp
        for i in range(0,len(msg)):
            cipher.append(msg[i])
        for i in range(0,len(cipher)):              #求解c'=my^rmodp
            cipher[i]=p*ord(cipher[i])
        return s,cipher       #返回(c,c')
    def dencry(self,cipher,s):      #解密需要c'、c和d
        plain=[]
        h=self.power(s,self.pri,self.pubp)        #求解c'^dmodp
        for i in range(0,len(cipher)):
            plain.append(chr(int(cipher[i]/h)))
        return plain