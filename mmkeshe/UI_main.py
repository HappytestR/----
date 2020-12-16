from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(684, 259)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 190, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 190, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 30, 361, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 70, 361, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 72, 15))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.centralWidget)
        self.comboBox.setGeometry(QtCore.QRect(180, 130, 87, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralWidget)
        self.comboBox_2.setGeometry(QtCore.QRect(380, 130, 87, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(190, 110, 72, 15))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(390, 110, 72, 15))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "开始"))
        self.pushButton_2.setText(_translate("MainWindow", "退出"))
        self.label.setText(_translate("MainWindow", "显示省份"))
        self.label_2.setText(_translate("MainWindow", "显示城市"))
        self.label_3.setText(_translate("MainWindow", "选择省份"))
        self.label_4.setText(_translate("MainWindow", "选择城市"))


'''if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    '''
