import random
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont
from yeelight import Bulb, BulbException

lst = ['192.168.0.1', '192.168.0.2', '192.168.0.3']


class MyWindow(QtWidgets.QDialog):
    def __init__(self, lst, parent=None):
        self.lst = lst
        QtWidgets.QWidget.__init__(self, parent)

        self.labelTask = QtWidgets.QLabel(
            'Выберите устройство для управления.')
        self.labelTask.setWordWrap(True)
        self.labelTask.setAlignment(
            QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.labelTask.setFont(QFont('Times', 14))
        self.labelTask.setStyleSheet(
            "border: 1px dashed black; border-radius: 10px;")

        self.btnOn = QtWidgets.QPushButton("&On")
        self.btnOff = QtWidgets.QPushButton("Of&f")

        self.radBtn = QtWidgets.QVBoxLayout()
        self.radBtn_group = QtWidgets.QButtonGroup()
        self.btns = []
        for ip in self.lst:
            btn = QtWidgets.QRadioButton(ip)
            self.radBtn.addWidget(btn)
            self.radBtn_group.addButton(btn)
            self.btns.append(btn)
        self.btns[random.randint(
            0, len(self.lst)-1)].setChecked(True)

        self.hboxHor = QtWidgets.QHBoxLayout()
        self.hboxHor.addLayout(self.radBtn)

        self.hboxBtn = QtWidgets.QVBoxLayout()
        self.hboxBtn.addWidget(self.btnOn)
        self.hboxBtn.addWidget(self.btnOff)
        self.hboxHor.addLayout(self.hboxBtn)
        self.setLayout(self.hboxHor)
        self.setGeometry(400, 200, 325, 150)

        self.btnOn.clicked.connect(self.on_btnOn_clicked)
        self.btnOff.clicked.connect(self.on_btnOff_clicked)

    def on_btnOn_clicked(self):
        ip = self.radBtn_group.checkedButton().text()
        # print(ip)
        try:
            bulb = Bulb(ip)
            bulb.turn_on()
        except BulbException as e:
            # print(f"Ошибка управления лампой: {e}")
            QtWidgets.QMessageBox.information(
                        self, 'Message', f"Ошибка управления лампой: {e}")

    def on_btnOff_clicked(self):
        ip = self.radBtn_group.checkedButton().text()
        # print(ip)
        try:
            bulb = Bulb(ip)
            bulb.turn_off()
        except BulbException as e:
            # print(f"Ошибка управления лампой: {e}")
            QtWidgets.QMessageBox.information(
                        self, 'Message', f"Ошибка управления лампой: {e}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow(lst)
    window.setWindowTitle("Управление лампами")
    window.show()
    sys.exit(app.exec_())
