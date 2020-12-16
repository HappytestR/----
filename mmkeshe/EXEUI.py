from mmkeshe.AES import AES,changedchr,changedint
from mmkeshe.DSS import DSS
from mmkeshe.ElGamalencry import EGencry
from mmkeshe.ElGamalSQ import ElGaSQ,verify
from mmkeshe.SHA1 import SHA1
from mmkeshe.RC4 import RC4
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
__version__='1.0.0'
__author__='named by Y'
class mainUI(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        #初始化界面
        layout=QVBoxLayout()
        self.resize(800,800)
        self.setWindowTitle("你好")
        self.btn2=QLabel()
        self.btn2.setText("本程序的使用说明如下：\n1.本程序适用于window平台，由python编程语言编写\n2.本程序通过选择算法进行算法的演示\n3.本程序__version__=1.0.0,__name__=YYY")
        self.btn3=QLabel()
        self.btn3.setOpenExternalLinks(True)
        self.btn3.setText("<a href='https://www.qt.io/'>欢迎访问Qt官网查看pythn QT5官方文档</a>")
        self.btn=QPushButton("运行算法")
        self.btn.setIcon(QIcon("1.ico"))
        self.btn.clicked.connect(self.runtest) #运行算法
        self.text1=QTextEdit()
        self.text2=QTextEdit()
        self.text2.setReadOnly(True)
        self.btn1=QComboBox()
        self.btn1.addItems(["AES","DSS","RC4","ELGamalencry","SHA1","ElGamalSQ","zero-knowledge 证明"])
        self.text1.setPlaceholderText("本文本框为算法的可能输入部分显示或输入")
        self.text2.setPlaceholderText("本文本框为算法的运算结果的显示，设置为仅读模式")
        layout.addWidget(self.btn2)
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn)
        layout.addWidget(self.text1)
        layout.addWidget(self.text2)
        layout.addWidget(self.btn3)
        self.setLayout(layout)
    def runtest(self):
        suan1=self.text1.toPlainText()           #得到文本框内容之后进行运算
        suan=self.btn1.currentText()
        if suan=='AES':
            str1='欢迎使用AES算法'
            str3,ok=QInputDialog.getText(self,'Text input Dialog','请输入AES加密密钥:')
            try:
                str4=str(str3)
                str4=changedint(str4)
                AEStest=AES(str4)
                str6=changedint(suan1)
                str5=AEStest.encrypt(str6)
                plain=AEStest.decrypt(str5)
                plain=changedchr(plain)
                self.text2.setText(str1+'\n您输入的密钥为：'+str(str3)+'\n您输入的明文为：'+suan1+'\n加密后的密文为：'+str(str5)+'\n解密后的明文为：'+plain)
            except Exception as e:
                print(e.__cause__)
        elif suan=='DSS':
            str1='欢迎使用DSS又称DSA算法,本算法采用L=1024,N=160'
            N=160;L=1024
            str2=""
            try:
                test = DSS()
                p, q, g = test.generate_params(L, N)
                if test.validate_params(p, q, g):
                    print("验证成功！")
                x, y = test.generate_keys(g, p, q)
                text = suan1
                M = str.encode(text, "ascii")
                r, s = test.sign(M, p, q, g, x)
                ve,re=test.verify(M, r, s, p, q, g, y)
                if ve==re:
                    str2="经过计算可得\n(v="+str(ve)+"\n(r="+str(re)+"\n消息M 验证成功 ，接受消息"
                else:
                    str2="经过计算可得\n(v="+str(ve)+"\n(r="+str(re)+"\n消息M 验证失败 ，拒绝消息"
                str3="(p="+str(p)+"\n(q="+str(q)+"\n(g="+str(g)+"\nx="+str(x)+"\n(y="+str(y)+"\n(r="+str(r)+"\n(s="+str(s)
                self.text2.setText(str1+"\n"+str3+"\n"+str2)
            except Exception as e:
                print(e.__context__)
        elif suan=='RC4':
            str1='欢迎使用RC4算法!'
            str2='初始化密钥key, S_BOX.'
            if suan1!="":
                test11=RC4()
                str3,ok=QInputDialog.getText(self,'Text Input Dialog','请输入RC4加密密钥:')
                str4=str(str3)
                try:
                    test11.set_key(str4)
                    str5=test11.encry(str(suan1))
                    plain=test11.dencry(str4,str5)
                    if ok:
                        self.text2.setText(str1+'\n'+str2+'\n您输入的密钥为：'+str4+'\n'+'加密后的密文为：'+str5+'\n解密后的明文为：'+plain)
                except Exception as e:
                    print(e.__context__)
            else:
                reply = QMessageBox.information(self, "提示", "请在text中输入明文", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        elif suan=='SHA1':
            str1='欢迎使用SHA1算法'
            test11=SHA1()
            try:
                test11.update(suan1.encode('utf-8'))
                str2=test11.hexdigest()
                self.text2.setText(str1+'\n'+'输入的明文为：'+suan1+'\n使用SHA1产生的hash值如下：\n'+str2)
            except Exception as e:
                print(e.__context__)
        elif suan=='ELGamalencry':
            str1='欢迎使用ElGamalencry算法'
            test11=EGencry()
            try:
                str12=test11.show_pub()
                s,cipher=test11.encry(suan1)
                plain=test11.dencry(cipher,s)
                plains=''.join(plain)
                self.text2.setText(str1+'\n您输入的明文为：'+suan1+str12+"\n加密后得到的密文为："+str(cipher)+"\n解密后得到的明文为："+plains)
            except Exception as e:
                print(e.__context__)
        elif suan=='zero-knowledge 证明':
            str1='欢迎使用zero-knowledge 证明'
            self.text2.setText(str1)
        else:
            str1='欢迎使用ElGamalSQ算法'
            str2=changedint(suan1)
            try:
                sign=ElGaSQ(int(str2))
                v = verify(sign.p, sign.g, sign.y, sign.m, sign.r, sign.s)
                str3=v.test()
                str4=v.verified()
                self.text2.setText(str1+'\n您输入的明文为：'+suan1+"\n签名如下所示：\n"+str3+"\n"+str4)
            except Exception as e:
                print(e.__context__)
if __name__=='__main__':
    app=QApplication(sys.argv)
    app.setWindowIcon(QIcon('1.ico'))
    test=mainUI()
    test.show()
    app.exit(app.exec_())