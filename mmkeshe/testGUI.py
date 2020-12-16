#-*-coding=utf-8
__version__='1.0.0'
__author__='named by Y'
#from . import RC4,DSS,ElGamalencry,ElGamalSQ,SHA1,zero_KLDPF
import sys
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox,QComboBox,QLabel
class Ui_Form(object):
    def setupUi(self,Form):
        Form.setObjectName('Form')
        Form.resize(800,800)
        self.setWindowIcon(QtGui.QIcon('1.ico'))
        self.comboBox=QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(100,700,200,50))   #行长度，列长度，长，宽
        self.comboBox.setObjectName('comboBox')
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.okButton=QtWidgets.QPushButton(Form)
        self.okButton.setGeometry(QtCore.QRect(450,700,200,50))
        self.okButton.setObjectName('okButton')
        self.testButton=QtWidgets.QPushButton(Form)
        self.testButton.setGeometry(QtCore.QRect(100,100,200,50))
        self.testButton.setObjectName("输入message")
        self.test1Button=QtWidgets.QPushButton(Form)
        self.test1Button.setGeometry(QtCore.QRect(450,100,200,50))
        self.test1Button.setObjectName("输出")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "密码学课程设计"))
        self.comboBox.setItemText(0, _translate("Form", "加密算法"))
        self.comboBox.setItemText(1, _translate("Form", "数字签名"))
        self.comboBox.setItemText(2, _translate("Form", "伪随机生成器"))
        self.comboBox.setItemText(3, _translate("Form", "Hash"))
        self.testButton.setText(_translate("From","输入message"))
        self.test1Button.setText(_translate("From","输出"))
        self.okButton.setText(_translate("Form", "确定"))


class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.okButton.clicked.connect(self.getComboxBoxValue)

    def getComboxBoxValue(self):
        select_value = self.comboBox.currentText()
        QMessageBox.information(self, "消息框标题", "欢迎使用%s,欢迎进入下一步！" % (select_value,), QMessageBox.Yes | QMessageBox.No)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())

