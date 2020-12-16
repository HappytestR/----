#-*-coding=utf-8
__version__='1.0.0'
__author__='named by Y'
import math
import random
from gmpy2 import invert,powmod,is_prime
#x是私钥
class ElGaSQ:      #ElGamal数字签名算法
    def __init__(self,c):   #  c=msg  d=k
        #print('欢迎使用ElGamal数字签名算法验证！')
        #self.randoma=random.randint(2,10)
        self.p=self.gen_p()      #选取一个大素数p,g
        self.g=self.gen_g(self.p-2)         #self.alpha=self.g   self.beta=self.y
        self.__x=self.gen_key(self.p-1)   #生成私钥
        self.y=powmod(self.g,self.__x,self.p)    #计算y=g^xmodp    y是公钥，x是私钥
        self.m=int(c)                   #签名的消息
        self.__k=self.gen_key(self.p-1)      #随机选取的整数k
        self.r=self.createR()     #计算Sign(m)=(r,s)  r=g^kmodp
        self.s=self.createS()           #s=(m-xr)K^(-1)mode(p-1)
        #print("The Signed Message Rriplet gengrated is :("+str(self.m)+","+str(self.r)+","+str(self.s)+")")
        #print("("+str(self.p)+','+str(self.g)+','+str(self.y)+','+str(self.m)+','+str(self.__k)+','+str(self.r)+','+str(self.s)+")")
    def gcd(self,a,b):             #辗转相除法求最小公约数
        if a<b:
            return self.gcd(b,a)
        elif a%b==0:
            return b
        else:
            return self.gcd(b,a%b)
    def gen_p(self):         #生成一个大素数p
        a=random.randint(pow(10,20),pow(10,50))
        while True:
            if is_prime(a):
                break
            else:
                a=random.randint(pow(10,20),pow(10,50))
        return a
    def gen_g(self,a):           #生成一个素数g
        v=random.randint(2,a)
        while True:
            if is_prime(v):
                break
            else:
                v=random.randint(2,a)
        return v
    def gen_key(self,max):      #密钥生成(私钥的生成）
        if max<pow(10,20):
            print('error,the mode is not the security!')
        key=random.randint(pow(10,20),max)
        while self.gcd(max,key)!=1:
            key=random.randint(pow(10,20),max)
        return key
    def createR(self):      #计算r
        a=powmod(self.g,self.__k,self.p)
        return a%(self.p)
    def createS(self):       #计算s
        a=(invert(self.__k,self.p-1)*((self.m-(self.__x*self.r)%(self.p-1))%(self.p-1)))%(self.p-1)
        return a%(self.p-1)
class verify:
    def __init__(self,a,b,c,d,e,f):   #a=p  b=g   c=y  d=msg   e=r  f=s
        self.p=a
        self.g=b
        self.y=c
        self.m=int(d)
        self.r=e
        self.s=f
        #print("("+str(self.p)+','+str(self.g)+','+str(self.y)+','+str(self.m)+','+str(self.r)+','+str(self.s)+")")
    def test(self):
        str1="(p,g,y,m,r,s)=\n"+"("+str(self.p)+','+str(self.g)+','+str(self.y)+','+str(self.m)+','+str(self.r)+','+str(self.s)+")"
        return str1
    def v1(self,b,c,d):            #计算验证函数1   y^r * r^s mod p
        a=(powmod(b,c,self.p)*powmod(c,d,self.p))%self.p
        return a%self.p
    def v2(self,b,c):
        a=powmod(b,c,self.p)      #计算验证函数2  g^m mod p
        return a%self.p
    def verified(self):
        if(self.v1(self.y,self.r,self.s)==self.v2(self.g,self.m)):       #计算数字签名欸
            str1="正在使用ElGamal数字签名验证算法\n"
            str2="The value of v1=(y^r*r^s)modp:"+str(self.v1(self.y,self.r,self.s)%self.p)+"\n"
            str3="The value of v2=(g^m)modp:"+str(self.v2(self.g,self.m)%self.p)+"\n"
            str4=str1+str2+str3+"验证成功，ElGamal数字签名验证成功"
            return str4
        else:
            str1="Signature missmatch\n"                      #计算数字签名算法进行的运算
            str2 = "The value of v1=(y^r*r^s)modp:" + str(self.v1(self.y, self.r, self.s) % self.p) + "\n"
            str3 = "The value of v2=(g^m)modp:" + str(self.v2(self.g, self.m) % self.p) + "\n"
            str4=str1+str2+str3+"验证失败，ElGamal数字签名验证失败"
            return str4
    def power1(self,a,b,c):                   #求幂的运算，即(a^b%c),使用了莫平方重复算法来计算
        x=1
        y=a
        while b > 0:
            if b%2==0:
                x=(x*y)%c
                y=(y*y)%c
            b=int(b/2)
        return x%c
    def IPnumber(self,a):
        count=0
        for i in range(2,a):
            if is_prime(i):
                count=count+1
        return count
if __name__=='__main__':
    m = 5
    sign = ElGaSQ(m)
    print("Verification of Elgamal Signature")
    v = verify(sign.p, sign.g, sign.y, sign.m, sign.r, sign.s)
    v.verified()

