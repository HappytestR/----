import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication

from mmkeshe.UI_main import Ui_MainWindow
from mmkeshe.area import dictCity,dictProvince


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # 初始化省
        self.comboBox.clear()  # 清空items
        self.comboBox.addItem('请选择')
        for k, v in dictProvince.items():
            self.comboBox.addItem(v, k)  # 键、值反转

    @pyqtSlot(int)
    # 取市的键值
    def on_comboBox_activated(self, index):
        key = self.comboBox.itemData(index)
        print(key)
        self.comboBox_2.clear()  # 清空items
        if key:
            self.comboBox_2.addItem('请选择')
            # 初始化市
            for k, v in dictCity[key].items():
                self.comboBox_2.addItem(v, k)  # 键、值反转

    @pyqtSlot()
    def on_pushButton_clicked(self):
        # 获取当前选项框索引
        province_index = self.comboBox.currentIndex()
        city_index = self.comboBox_2.currentIndex()
        # 取当前省市县名称
        province_name = self.comboBox.itemText(province_index)
        city_name = self.comboBox_2.itemText(city_index)
        print(province_name, city_name)
        self.lineEdit.setText(province_name)  # 显示省份
        self.lineEdit_2.setText(city_name)  # 显示城市


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())