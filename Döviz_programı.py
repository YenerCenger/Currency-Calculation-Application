import sys
import os
from yardım_pencere import Ui_Form1
import requests
from PyQt5.QtWidgets import QWidget,QAction,QMainWindow,qApp,QTextEdit,QApplication,QRadioButton,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1042, 619)
        Form.setMinimumSize(QtCore.QSize(688, 331))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setMinimumSize(QtCore.QSize(666, 0))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 519))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.birinci_grup = QtWidgets.QComboBox(self.widget)
        self.birinci_grup.setObjectName("birinci_grup")
        self.birinci_grup.addItem("")
        self.birinci_grup.addItem("")
        self.birinci_grup.addItem("")
        self.birinci_grup.addItem("")
        self.birinci_grup.addItem("")
        self.birinci_grup.addItem("")
        self.birinci_grup.addItem("")
        self.birinci_grup.addItem("")
        self.birinci_grup.addItem("")
        self.birinci_grup.addItem("")
        self.birinci_grup.addItem("")
        self.birinci_grup.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.birinci_grup)
        self.birinci_text = QtWidgets.QPlainTextEdit(self.widget)
        self.birinci_text.setMinimumSize(QtCore.QSize(256, 0))
        self.birinci_text.setMaximumSize(QtCore.QSize(16777215, 192))
        self.birinci_text.setObjectName("birinci_text")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.birinci_text)
        self.ikinci_grup = QtWidgets.QComboBox(self.widget)
        self.ikinci_grup.setObjectName("ikinci_grup")
        self.ikinci_grup.addItem("")
        self.ikinci_grup.addItem("")
        self.ikinci_grup.addItem("")
        self.ikinci_grup.addItem("")
        self.ikinci_grup.addItem("")
        self.ikinci_grup.addItem("")
        self.ikinci_grup.addItem("")
        self.ikinci_grup.addItem("")
        self.ikinci_grup.addItem("")
        self.ikinci_grup.addItem("")
        self.ikinci_grup.addItem("")
        self.ikinci_grup.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.ikinci_grup)
        self.ikinci_text = QtWidgets.QPlainTextEdit(self.widget)
        self.ikinci_text.setMinimumSize(QtCore.QSize(256, 0))
        self.ikinci_text.setMaximumSize(QtCore.QSize(16777215, 192))
        self.ikinci_text.setObjectName("ikinci_text")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.ikinci_text)
        self.temizle = QtWidgets.QPushButton(self.widget)
        self.temizle.setObjectName("temizle")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.temizle)
        self.yardim = QtWidgets.QPushButton(self.widget)
        self.yardim.setObjectName("yardim")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.yardim)
        self.hesapla = QtWidgets.QPushButton(self.widget)
        self.hesapla.setObjectName("hesapla")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.hesapla)
        self.horizontalLayout.addLayout(self.formLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.sonuc = QtWidgets.QPlainTextEdit(self.widget)
        self.sonuc.setMinimumSize(QtCore.QSize(256, 0))
        self.sonuc.setMaximumSize(QtCore.QSize(16777215, 192))
        self.sonuc.setObjectName("sonuc")
        self.verticalLayout.addWidget(self.sonuc)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addWidget(self.widget, 0, QtCore.Qt.AlignHCenter)

        self.hesapla.clicked.connect(self.hesap)
        self.temizle.clicked.connect(self.temiz)
        self.yardim.clicked.connect(self.yardim_et)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle("Döviz Hesaplama Uygulaması")
        self.birinci_grup.setItemText(0, _translate("Form", "İlk Birimi Girin:"))
        self.birinci_grup.setItemText(1, _translate("Form", "Amerikan dolar (USD)"))
        self.birinci_grup.setItemText(2, _translate("Form", "Euro (EUR)"))
        self.birinci_grup.setItemText(3, _translate("Form", "Japon yeni (JPY)"))
        self.birinci_grup.setItemText(4, _translate("Form", "İngiliz sterlini (GBP)"))
        self.birinci_grup.setItemText(5, _translate("Form", "Avustralya doları (AUD)"))
        self.birinci_grup.setItemText(6, _translate("Form", "Kanada doları (CAD)"))
        self.birinci_grup.setItemText(7, _translate("Form", "İsviçre frangı (CHF) "))
        self.birinci_grup.setItemText(8, _translate("Form", "Hong Kong doları ( HKD)"))
        self.birinci_grup.setItemText(9, _translate("Form", "Singapur doları(SGD)"))
        self.birinci_grup.setItemText(10, _translate("Form", "Hindistan rupisi(INR)"))
        self.birinci_grup.setItemText(11, _translate("Form", "Türk lirası (TRY)"))
        self.ikinci_grup.setItemText(0, _translate("Form", "İkinci Birimi Girin:"))
        self.ikinci_grup.setItemText(1, _translate("Form", "Amerikan dolar (USD)"))
        self.ikinci_grup.setItemText(2, _translate("Form", "Euro (EUR)"))
        self.ikinci_grup.setItemText(3, _translate("Form", "Japon yeni (JPY)"))
        self.ikinci_grup.setItemText(4, _translate("Form", "İngiliz sterlini (GBP)"))
        self.ikinci_grup.setItemText(5, _translate("Form", "Avustralya doları (AUD)"))
        self.ikinci_grup.setItemText(6, _translate("Form", "Kanada doları (CAD)"))
        self.ikinci_grup.setItemText(7, _translate("Form", "İsviçre frangı (CHF) "))
        self.ikinci_grup.setItemText(8, _translate("Form", "Hong Kong doları ( HKD)"))
        self.ikinci_grup.setItemText(9, _translate("Form", "Singapur doları(SGD)"))
        self.ikinci_grup.setItemText(10, _translate("Form", "Hindistan rupisi(INR)"))
        self.ikinci_grup.setItemText(11, _translate("Form", "Türk lirası (TRY)"))
        self.temizle.setText(_translate("Form", "Temizle"))
        self.yardim.setText(_translate("Form", "Yardım!"))
        self.hesapla.setText(_translate("Form", "Hesapla"))
        self.hesapla.setShortcut("Ctrl+Q")

    def hesap(self):
        birinci_birim = (self.birinci_text.toPlainText()).upper().strip()
        ikinci_birim = (self.ikinci_text.toPlainText()).upper().strip()

        url = "http://data.fixer.io/api/latest?access_key=4af860b9155fafa2633ef7608277342c"

        response = requests.get(url)

        json = response.json()

        try:
            sonuç = str(json["rates"][birinci_birim] / json["rates"][ikinci_birim])
            self.sonuc.setPlainText("Bir " + ikinci_birim + " "+ sonuç +" "+ birinci_birim+"'dir")
        except KeyError as e:
            self.sonuc.setPlainText(f"Hata: {e}. Lütfen Para Birimlerini Doğru Giriniz")


    def temiz(self):
        self.birinci_text.clear()
        self.ikinci_text.clear()
        self.sonuc.clear()
    def yardim_et(self):
        self.window = QMainWindow(Form)
        self.ui = Ui_Form1()
        self.ui.setupUi(self.window)
        self.window.setStyleSheet(Form.styleSheet())
        self.window.show()

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

