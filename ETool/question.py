# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'question.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(734, 538)
        Dialog.setStyleSheet("image: url(:/backgrad/nezhno-gol.jpg);")
        self.textEdit_44 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_44.setGeometry(QtCore.QRect(90, 10, 601, 81))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.textEdit_44.setFont(font)
        self.textEdit_44.setObjectName("textEdit_44")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 100, 311, 71))
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(160, 210, 271, 91))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 200, 211, 101))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(80, 350, 561, 171))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(540, 210, 131, 91))
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(350, 110, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 100, 311, 71))
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textEdit_44.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Choose the the right translation for &lt;&gt;</span></p></body></html>"))
        self.label.setText(_translate("Dialog", "Ваш счёт:"))
        self.label_2.setText(_translate("Dialog", "OR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
