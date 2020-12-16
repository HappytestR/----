#-*-coding=utf-8
__version__='1.0.0'
__author__='named by Y'
from random import randrange
from hashlib import sha1
import math
from gmpy2 import to_binary,xmpz,is_prime,powmod
class DSS:
    def __init__(self):         #DSS类的初始化函数
        print("欢迎使用数字签名标准DSS算法")
    def gcd(self,a,b,s):    #辅助求逆，使用欧几里得扩展算法来进行运算
        if a%b==0:
            return b,s
        q=a//b
        temp=s[1]
        s[1]=s[0]-q*s[1]
        s[0]=temp
        return self.gcd(b,a%b,s)
    def invert(self,a,b):   #求逆的运算，计算a*a^-1modb=1
        s=[1,0]
        self.gcd(a,b,s)
        if s[1]==0:
            return -1
        elif s[1]<0:
            return b+s[1]
        else:
            return s[1]
    def generate_p_q(self,L,N):   #生成一个素数因子
        g=N
        n=(L-1)//g
        b=(L-1)%g
        while True:
            while True:
                s=xmpz(randrange(1,2**(g)))       #生成一个大素数g
                a=sha1(to_binary(s)).hexdigest()
                zz=xmpz((s+1)%(2**g))
                z = sha1(to_binary(zz)).hexdigest()       #hash值为160bit，通过生成随机字符串将 | 链接起来新城新的字符串来实现p和q的生成
                U = int(a, 16) ^ int(z, 16)
                mask = 2 ** (N - 1) + 1
                q = U | mask
                if is_prime(q, 20):   #is_prime用来判断是否为素数因子
                    break
            # generate p         #生成p
            i = 0  # counter
            j = 2  # offset
            while i < 4096:
                V = []
                for k in range(n + 1):
                    arg = xmpz((s + j + k) % (2 ** g))
                    zzv = sha1(to_binary(arg)).hexdigest()
                    V.append(int(zzv, 16))
                W = 0
                for qq in range(0, n):
                    W += V[qq] * 2 ** (160 * qq)
                W += (V[n] % 2 ** b) * 2 ** (160 * n)
                X = W + 2 ** (L - 1)
                c = X % (2 * q)
                p = X - c + 1          # p = X - (c - 1)
                if p >= 2 ** (L - 1):
                    if is_prime(p, 10):
                        return p, q         #生成一个素数p:2^L-1<p<2^L,L为64的倍数   选取p-1的一个素数因子q,2^159<q<2^160
                i += 1
                j += n + 1
    def generate_g(self,p,q):               #生成g g=t^(p-1)/qmod p         1<t<p-1
        while True:
            h=randrange(2,p-1)          #随机选取t  1<h<p-1   h^(p-1)/qmodp>1成立的整数
            exp=xmpz((p-1)//q)
            g=powmod(h,exp,p)
            if g>1:
                break
        return g         #生成的一个g=h^(p-1)/q
    def generate_keys(self,g,p,q):      #生成私钥key，根据g,p,q来生成私钥key
        x=randrange(2,q)        #在这里随机生成的整数x   0<x<q
        y=powmod(g,x,p)    #计算私钥y=g^xmodp
        return x,y
    def generate_params(self,L,N):          #选取一个素数p：2^L-1<p<2^L ,L为64的倍数
        p,q=self.generate_p_q(L,N)
        g=self.generate_g(p,q)
        return p,q,g            #生成p,q,g
    def sign(self,M,p,q,g,x):        #新型数字签名
        if not self.validate_params(p,q,g):         #判断是否为素数
            raise Exception("Invalid params")
        while True:
            k=randrange(2,q)              #随机生成一个整数k  1<=k<q
            r=powmod(g,k,p)%q     #r=(g^kmodp)modq
            m=int(sha1(M).hexdigest(),16)    #在这里要先对消息进行散列值计算
            try:      #捕捉k,q没有逆的异常
                s=(self.invert(k,q)*(m+x*r))%q    #计算s=k^(-1)(h(m)+xr)modq
                return r,s        #返回计算出来的(r,s)作为对消息m的签名
            except ZeroDivisionError:
                pass                 #到此签名结束
    def verify(self,M,r,s,p,q,g,y):    #进行数字签名的认证
        if not self.validate_params(p, q, g):   #首先判断是否为素数
            raise Exception("Invalid params")
        if not self.validate_sign(r, s, q):    #判断签名是否合法，0<r<q,0<s<q是否成立，如果有一个不成立，则签名认证失败
            return 0,1
        try:               #捕捉不存在逆的情况
            w = self.invert(s, q)    #首先求的w,w=s^(-1)modq
        except ZeroDivisionError:
            return 0,1
        m = int(sha1(M).hexdigest(), 16)
        u1 = (m * w) % q            #求的u1 =h(m)*w mod q
        u2 = (r * w) % q            #求的u2=r*wmodq
        v = (powmod(g, u1, p) * powmod(y, u2, p)) % p % q  #求的v=((g^u1*y^u2)modp)modq
        #if v == r:          #验证，如果v=r，则Bob接受(r,s)是消息m的签名，否则，拒绝此签名
            #return True
        return v,r
    def validate_params(self,p,q,g):     #判断是否互素
        if is_prime(p) and is_prime(q):  #判断 p q是否都是素数，因为下面还要进行求逆
            return True
        if powmod(g,q,p)==1 and g>1 and (p-1)%q:
            return True
        return False
    def validate_sign(self,r,s,q):       #判断能否进行 签名运算
        if r<0 and r>q:   #如果r=0或s=0，则选取新的随机数k，重新计算出r和s.当一般来说，r=0或者s=0的出现的概率非常小
            return False
        if s<0 and s>q:
            return False
        return True
'''if __name__=='__main__':
    N = 160    #设置q为160bit的素数
    L = 1024   #设置密钥p为1024bit的数
    test=DSS()
    p, q, g = test.generate_params(L, N)
    if test.validate_params(p,q,g):
        print("验证成功！")
    x, y = test.generate_keys(g, p, q)
    text = "hello,world!"
    M = str.encode(text, "ascii")
    r, s = test.sign(M, p, q, g, x)
    if test.verify(M, r, s, p, q, g, y):
        print('All ok') '''

