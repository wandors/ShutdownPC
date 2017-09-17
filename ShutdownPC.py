# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Shutsui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!
import winreg
import subprocess
import Suts_rc
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(248, 90)
        self.disctop = QtWidgets.QApplication.desktop()
        Form.move(int(self.disctop.width() - 260), 380)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        Form.setWindowFlags(QtCore.Qt.Tool | QtCore.Qt.FramelessWindowHint)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 71, 71))
        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(2)
        self.shadow.setOffset(5)
        self.pushButton.setGraphicsEffect(self.shadow)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Rests.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(80, 80))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 10, 71, 71))
        self.shadow_2 = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow_2.setBlurRadius(2)
        self.shadow_2.setOffset(5)
        self.pushButton_2.setGraphicsEffect(self.shadow_2)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/sleep.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 10, 71, 71))
        self.shadow_3 = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow_3.setBlurRadius(2)
        self.shadow_3.setOffset(5)
        self.pushButton_3.setGraphicsEffect(self.shadow_3)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icons/Shuts.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.rest_)
        self.pushButton_2.clicked.connect(self.Sleep_)
        self.pushButton_3.clicked.connect(self.Shuts_)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

    def rest_(self):
        subprocess.Popen("shutdown -r -t 0 -f", shell=True)

    def Sleep_(self):
        subprocess.Popen(r'%windir%\system32\rundll32.exe powrprof.dll,SetSuspendState Hibernate', shell=True)

    def Shuts_(self):
        subprocess.Popen("shutdown -s -t 0 -f", shell=True)



if __name__ == "__main__":
    import sys
    try:
        regs = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
        mykeys = winreg.OpenKey(regs, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_ALL_ACCESS)
        winreg.DeleteValue(mykeys, 'ShutdownPC')
        winreg.CloseKey(self.mykeys)
    except:
        pass
    regs = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
    mykeys = winreg.OpenKey(regs, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(mykeys, 'ShutdownPC', 0, winreg.REG_SZ, '"' + sys.argv[0] + '"' + " Minimum")
    winreg.CloseKey(mykeys)
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

