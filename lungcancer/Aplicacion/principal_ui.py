# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'principal.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LCDetection(object):
    def setupUi(self, LCDetection):
        LCDetection.setObjectName("LCDetection")
        LCDetection.resize(922, 590)
        self.slider_slices = QtWidgets.QSlider(LCDetection)
        self.slider_slices.setGeometry(QtCore.QRect(530, 130, 21, 351))
        self.slider_slices.setOrientation(QtCore.Qt.Vertical)
        self.slider_slices.setObjectName("slider_slices")
        self.comboBox = QtWidgets.QComboBox(LCDetection)
        self.comboBox.setGeometry(QtCore.QRect(170, 40, 191, 22))
        self.comboBox.setObjectName("comboBox")
        self.labelpaciente = QtWidgets.QLabel(LCDetection)
        self.labelpaciente.setGeometry(QtCore.QRect(50, 40, 121, 16))
        self.labelpaciente.setObjectName("labelpaciente")
        self.widget = mplWidget(LCDetection)
        self.widget.setGeometry(QtCore.QRect(39, 129, 461, 351))
        self.widget.setObjectName("widget")
        self.label_instrucciones = QtWidgets.QLabel(LCDetection)
        self.label_instrucciones.setGeometry(QtCore.QRect(40, 75, 431, 41))
        self.label_instrucciones.setText("")
        self.label_instrucciones.setObjectName("label_instrucciones")
        self.button_slice = QtWidgets.QPushButton(LCDetection)
        self.button_slice.setGeometry(QtCore.QRect(530, 100, 21, 23))
        self.button_slice.setObjectName("button_slice")
        self.button_3d = QtWidgets.QPushButton(LCDetection)
        self.button_3d.setEnabled(False)
        self.button_3d.setGeometry(QtCore.QRect(640, 180, 191, 31))
        self.button_3d.setObjectName("button_3d")
        self.label_3d = QtWidgets.QLabel(LCDetection)
        self.label_3d.setGeometry(QtCore.QRect(630, 250, 291, 191))
        self.label_3d.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3d.setText("")
        self.label_3d.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_3d.setObjectName("label_3d")
        self.buttons_acepta_segmentacion = QtWidgets.QDialogButtonBox(LCDetection)
        self.buttons_acepta_segmentacion.setGeometry(QtCore.QRect(670, 480, 161, 31))
        self.buttons_acepta_segmentacion.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttons_acepta_segmentacion.setObjectName("buttons_acepta_segmentacion")
        self.label_segmentacion = QtWidgets.QLabel(LCDetection)
        self.label_segmentacion.setGeometry(QtCore.QRect(630, 460, 251, 16))
        self.label_segmentacion.setText("")
        self.label_segmentacion.setObjectName("label_segmentacion")
        self.label_slice_seleccionado = QtWidgets.QLabel(LCDetection)
        self.label_slice_seleccionado.setGeometry(QtCore.QRect(200, 495, 111, 21))
        self.label_slice_seleccionado.setText("")
        self.label_slice_seleccionado.setObjectName("label_slice_seleccionado")
        self.label_max_slice = QtWidgets.QLabel(LCDetection)
        self.label_max_slice.setGeometry(QtCore.QRect(560, 130, 46, 13))
        self.label_max_slice.setText("")
        self.label_max_slice.setObjectName("label_max_slice")
        self.label_min_slice = QtWidgets.QLabel(LCDetection)
        self.label_min_slice.setGeometry(QtCore.QRect(560, 470, 46, 13))
        self.label_min_slice.setObjectName("label_min_slice")
        self.label_val_slider = QtWidgets.QLabel(LCDetection)
        self.label_val_slider.setGeometry(QtCore.QRect(510, 280, 20, 31))
        self.label_val_slider.setText("")
        self.label_val_slider.setObjectName("label_val_slider")

        self.retranslateUi(LCDetection)
        QtCore.QMetaObject.connectSlotsByName(LCDetection)

    def retranslateUi(self, LCDetection):
        _translate = QtCore.QCoreApplication.translate
        LCDetection.setWindowTitle(_translate("LCDetection", "LCDetection"))
        self.labelpaciente.setText(_translate("LCDetection", "Seleccione paciente"))
        self.button_slice.setText(_translate("LCDetection", "Ok"))
        self.button_3d.setText(_translate("LCDetection", "Ver en 3d"))
        self.label_min_slice.setText(_translate("LCDetection", "1"))

from mplwidget import mplWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LCDetection = QtWidgets.QWidget()
    ui = Ui_LCDetection()
    ui.setupUi(LCDetection)
    LCDetection.show()
    sys.exit(app.exec_())

