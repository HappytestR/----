from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt,QDir
from PyQt5.QtGui import QPixmap,QPalette
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QFont,QIcon
import sys
import hashlib
class WindowDemo(QWidget):
    def __init__(self):
        super().__init__()
        label1=QLabel(self)
        label2=QLabel(self)
        label3=QLabel(self)
        label4=QLabel(self)
        #初始化标签控件
        label1.setText("这是一个文本标签.")
        label1.setAutoFillBackground(True)
        palette=QPalette()
        palette.setColor(QPalette.Window,Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)
        label2.setText("<a href='#'>欢迎使用python GUI</a>")
        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('这是一个图片标签')
        label3.setPixmap(QPixmap("10.jpg"))
        label4.setText("<a href='http://www.cnblogs.com/wangshuo1/'>欢迎访问信平的小屋</a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('这是一个超链接标签')
        vbox=QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addStretch()
        vbox.addWidget(label2)
        vbox.addStretch()
        vbox.addWidget(label3)
        vbox.addStretch()
        vbox.addWidget(label4)
        label1.setOpenExternalLinks(True)  #允许label1控制访问超链接
        #打开允许访问超链接，默认是不允许，需要使用setOpenExternaleLInks（True)
        label4.setOpenExternalLinks(True)
        label4.linkActivated.connect(self.link_clicked)
        label2.linkHovered.connect(self.link_hovered)
        label1.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.setLayout(vbox)
        self.setWindowTitle('你好')
    def link_hovered(self):
        print("当鼠标滑过label-2标签时，触发事件.")
    def link_clicked(self):
        print('当鼠标点击label_4标签时，触发事件。')
class QlabelDemo(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('你好')
        nameLb1=QLabel('&Name',self)
        nameEd1=QLineEdit(self)
        nameLb1.setBuddy(nameEd1)
        nameLb2=QLabel('&Password',self)
        nameEd2=QLineEdit(self)
        nameLb2.setBuddy(nameEd2)
        btnOk=QPushButton("&OK")
        btnCancel=QPushButton("&Cancel")
        mainLayout=QGridLayout(self)
        mainLayout.addWidget(nameLb1,0,0)
        mainLayout.addWidget(nameEd1,0,1,1,2)
        mainLayout.addWidget(nameLb2,1,0)
        mainLayout.addWidget(nameEd2,1,1,1,2)
        mainLayout.addWidget(btnOk,2,1)
        mainLayout.addWidget(btnCancel,2,2)

class lineEditDome(QWidget):
    def __init__(self,parent=None):
        super(lineEditDome,self).__init__(parent)
        self.setWindowTitle("你好")
        flo=QFormLayout()
        pNormalLineEdit=QLineEdit()
        pNoEchoLineEdit=QLineEdit()
        pPasswordLineEdit=QLineEdit()
        pPasswordEchoonEditLineEdit=QLineEdit()
        pIntLineEdit=QLineEdit()
        pIntValidator=QIntValidator(self)
        pIntValidator.setRange(1,99)
        flo.addRow("1-99",pIntLineEdit)
        flo.addRow("Normal",pNormalLineEdit)
        flo.addRow("NoEcho",pNoEchoLineEdit)
        flo.addRow('Password',pPasswordLineEdit)
        flo.addRow('PasswordEchoOnEdit',pPasswordEchoonEditLineEdit)
        pIntLineEdit.setPlaceholderText("1-99")
        pNormalLineEdit.setPlaceholderText("Normal")
        pNoEchoLineEdit.setPlaceholderText("NoEcho")
        pPasswordLineEdit.setPlaceholderText("Password")
        pPasswordEchoonEditLineEdit.setPlaceholderText("PasswordEchoOnEdit")
        #设置验证器
        pIntLineEdit.setValidator(pIntValidator)
        #设置显示效果
        pNormalLineEdit.setEchoMode(QLineEdit.Normal)
        pNoEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        pPasswordLineEdit.setEchoMode(QLineEdit.Password)
        pPasswordEchoonEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.setLayout(flo)
class LineEdit1(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("你好")
        e1=QLineEdit()
        e1.setValidator(QIntValidator())
        e1.setMaxLength(4)
        e1.setAlignment(Qt.AlignRight)
        e1.setFont(QFont("Arial",20))
        e2=QLineEdit()
        e2.setValidator(QDoubleValidator(0.99,99.99,2))
        flo=QFormLayout()
        flo.addRow("integer validator",e1)
        flo.addRow("Double validator",e2)
        e3=QLineEdit()
        e3.setInputMask('+99_9999_999999;A')
        flo.addRow("Input Mask",e3)
        e4=QLineEdit()
        e4.textChanged.connect(self.textchanged)
        flo.addRow("Text changed",e4)
        e5=QLineEdit()
        e5.setEchoMode(QLineEdit.Password)
        flo.addRow("Password",e5)
        e6=QLineEdit("hello PyQt5")
        e6.setReadOnly(True)
        flo.addRow("Read only",e6)
        e5.editingFinished.connect(self.enterPress)
        self.setLayout(flo)
    def textchanged(self,text):
        print("输入的内容为:"+text)
    def enterPress(self):
        print("已输入值")
class TextEditDemo(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("你好")
        self.resize(800,800)
        self.textEdit=QTextEdit()
        self.textEdit1=QTextEdit()
        self.btnPress1=QPushButton("提交文本")
        self.btnPress2=QPushButton("显示hash值")
        self.btnPress3=QPushButton("清空文本")
        self.btnPress3.setIcon(QIcon('1.ico'))
        layout=QVBoxLayout()
        self.test1="#"
        layout.addWidget(self.textEdit1)
        layout.addWidget(self.textEdit)
        layout.addWidget(self.btnPress1)
        layout.addWidget(self.btnPress2)
        layout.addWidget(self.btnPress3)
        self.setLayout(layout)
        self.btnPress1.clicked.connect(self.btnPress1_Clicked)
        self.btnPress2.clicked.connect(self.btnPress2_Clicked)
        self.btnPress3.clicked.connect(self.btnPress3_Clicked)
    def btnPress1_Clicked(self):
        self.test1=self.textEdit.toPlainText()
    def btnPress2_Clicked(self):
        md=hashlib.md5()
        md.update(self.test1.encode("utf-8"))
        self.textEdit.setPlainText(md.hexdigest())
    def btnPress3_Clicked(self):
        self.textEdit.clear()
class Form1(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        layout=QVBoxLayout()
        self.btn1=QPushButton("Button1")
        self.btn1.setCheckable(True)
        self.btn1.toggle()
        self.btn1.clicked.connect(lambda :self.whichbtn(self.btn1))
        self.btn1.clicked.connect(self.btnstate)
        layout.addWidget(self.btn1)
        self.btn2=QPushButton("image")
        self.btn2.setIcon(QIcon('1.ico'))
        self.btn2.clicked.connect(lambda :self.whichbtn(self.btn2))
        layout.addWidget(self.btn2)
        self.setLayout(layout)
        self.btn3=QPushButton("Disabled")
        self.btn3.setEnabled(False)
        layout.addWidget(self.btn3)
        self.btn4=QPushButton("&Download")
        self.btn4.setDefault(True)
        self.btn4.clicked.connect(lambda :self.whichbtn(self.btn4))
        layout.addWidget(self.btn4)
        self.btn5=QRadioButton("Button1")
        self.btn6=QRadioButton("Button2")
        self.btn5.setChecked(True)
        self.btn5.toggled.connect(lambda :self.btnstate1(self.btn5))
        layout.addWidget(self.btn5)
        self.btn6.toggled.connect(lambda :self.btnstate1(self.btn6))
        layout.addWidget(self.btn6)
        self.setLayout(layout)
        self.setWindowTitle("你好")
    def btnstate(self):
        if self.btn1.isChecked():
            print("button pressed")
        else:
            print("button released")
    def whichbtn(self,btn):
        print("clicked button is "+btn.text())
    def btnstate1(self,btn):
        if btn.text()=="Button1":
            print(btn.text()+"is selected")
        else:
            print(btn.text()+"is deselected")
        if btn.text()=="Button2":
            print(btn.text()+"is selected")
        else:
            print(btn.text()+"is deselected")
class checkBoxDemo(QWidget):
    def __init__(self, parent=None):
        super(checkBoxDemo, self).__init__(parent)
        groupBox=QGroupBox("Checkboxes")
        groupBox.setFlat(True)
        layout=QHBoxLayout()
        self.checkBox1= QCheckBox("&Checkbox1")
        self.checkBox1.setChecked(True)
        self.checkBox1.stateChanged.connect( lambda:self.btnstate(self.checkBox1))
        layout.addWidget(self.checkBox1)
        self.checkBox2=QCheckBox("Checkbox2")
        self.checkBox2.stateChanged.connect( lambda:self.btnstate(self.checkBox2))
        layout.addWidget(self.checkBox2)
        self.checkBox3=QCheckBox("Checkbox3")
        self.checkBox3.setTristate(True)
        self.checkBox3.setCheckState(Qt.PartiallyChecked)
        self.checkBox3.stateChanged.connect( lambda:self.btnstate(self.checkBox3))
        layout.addWidget(self.checkBox3)
        groupBox.setLayout(layout)
        mainLayout=QVBoxLayout()
        mainLayout.addWidget(groupBox)
        self.setLayout(mainLayout)
        self.setWindowTitle("你好")
    def btnstate(self,btn):
        chk1Status=self.checkBox1.text()+", isCHecked="+str(self.checkBox1.isChecked())+',checkState='+str(self.checkBox1.checkState())+"\n"
        chk2Status = self.checkBox2.text() + ", isCHecked=" + str(self.checkBox2.isChecked()) + ',checkState=' +\
        str(self.checkBox2.checkState()) + "\n"
        chk3Status = self.checkBox3.text() + ", isCHecked=" + str(self.checkBox3.isChecked()) + ',checkState=' +\
        str(self.checkBox3.checkState()) + "\n"
        print(chk1Status+chk2Status+chk3Status)

class CombixDemo(QWidget):
    def __init__(self,parent=None):
        super(CombixDemo,self).__init__(parent)
        self.setWindowTitle("你好")
        self.resize(300,90)
        Layout=QVBoxLayout()
        self.lb1=QLabel("")
        self.cb=QComboBox()
        self.cb.addItem("hash")
        self.cb.addItem("cipher")
        self.cb.addItem("DSA")
        self.cb.addItem("伪随机数生成器")
        self.cb.addItems(["java","c#","Python"])
        self.cb.currentIndexChanged.connect(self.selectionchange)
        Layout.addWidget(self.cb)
        Layout.addWidget(self.lb1)
        self.setLayout(Layout)
    def selectionchange(self,i):
        self.lb1.setText(self.cb.currentText())
        print("Item in the list are:")
        for count in range(self.cb.count()):
            print('item'+str(count)+'='+self.cb.itemText(count))
            print("Current index",i,"selection changed",self.cb.currentText())

class FonDialogDemo(QWidget):
    def __init__(self,parent=None):
        super(FonDialogDemo, self).__init__(parent)
        layout=QVBoxLayout()
        self.fontButton=QPushButton("choose font")
        self.fontButton.clicked.connect(self.getFont)
        layout.addWidget(self.fontButton)
        self.fontLineEdit=QLabel("hello,测试字体例子")
        layout.addWidget(self.fontLineEdit)
        self.setLayout(layout)
        self.setWindowTitle("你好")
    def getFont(self):
        font,ok=QFontDialog.getFont()
        if ok:
            self.fontLineEdit.setFont(font)
class filedialogdemo(QWidget):
    def __int__(self,parent=None):
        super(filedialogdemo,self).__init__(parent)
        layout=QVBoxLayout()
        self.btn=QPushButton("加载图片")
        self.btn.clicked.connect(self.getfile)
        layout.addWidget(self.btn)
        self.le=QLabel("")
        layout.addWidget(self.le)
        self.btn1=QPushButton("加载文本文件")
        self.btn1.clicked.connect(self.getfiles)
        layout.addWidget(self.btn1)
        self.contents=QTextEdit()
        layout.addWidget(self.contents)
        self.setLayout(layout)
        self.setWindowTitle("你好")
    def getfile(self):
        fname,_=QFileDialog.getOpenFileName(self,'Open file',"D:\\","Image files (*.jpg *.gif)")
        self.le.setPixmap(QPixmap(fname))
    def getfiles(self):
        dig=QFileDialog()
        dig.setFileMode(QFileDialog.AnyFile)
        dig.setFilter(QDir.Files)
        if dig.exec_():
            filename=dig.selectedFiles()
            f=open(filename[0],'r')
            with f:
                data=f.read()
                self.contents.setText(data)
if __name__=="__main__":
    app=QApplication(sys.argv)
    app.setWindowIcon(QIcon("1.ico"))
    win=filedialogdemo()
    win.show()
    app.exit(app.exec_())