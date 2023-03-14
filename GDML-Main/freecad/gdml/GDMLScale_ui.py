# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GDMLScale.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_GDMLScale(object):
    def setupUi(self, GDMLScale):
        GDMLScale.setObjectName("GDMLScale")
        GDMLScale.resize(403, 267)
        self.checkBox = QtWidgets.QCheckBox(GDMLScale)
        self.checkBox.setGeometry(QtCore.QRect(40, 160, 141, 22))
        self.checkBox.setObjectName("checkBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(GDMLScale)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 20, 341, 116))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.xlabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.xlabel.setObjectName("xlabel")
        self.horizontalLayout.addWidget(self.xlabel)
        self.xScale = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.xScale.setMinimum(0.01)
        self.xScale.setMaximum(100.0)
        self.xScale.setProperty("value", 1.0)
        self.xScale.setObjectName("xScale")
        self.horizontalLayout.addWidget(self.xScale)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.yLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.yLabel.setObjectName("yLabel")
        self.horizontalLayout_3.addWidget(self.yLabel)
        self.yScale = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.yScale.setMinimum(0.01)
        self.yScale.setMaximum(100.0)
        self.yScale.setProperty("value", 1.0)
        self.yScale.setObjectName("yScale")
        self.horizontalLayout_3.addWidget(self.yScale)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.zLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.zLabel.setObjectName("zLabel")
        self.horizontalLayout_4.addWidget(self.zLabel)
        self.zScale = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.zScale.setMinimum(0.01)
        self.zScale.setMaximum(100.0)
        self.zScale.setProperty("value", 1.0)
        self.zScale.setObjectName("zScale")
        self.horizontalLayout_4.addWidget(self.zScale)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.scaleButton = QtWidgets.QPushButton(GDMLScale)
        self.scaleButton.setGeometry(QtCore.QRect(90, 210, 88, 34))
        self.scaleButton.setObjectName("scaleButton")
        self.cancelButton = QtWidgets.QPushButton(GDMLScale)
        self.cancelButton.setGeometry(QtCore.QRect(200, 210, 88, 34))
        self.cancelButton.setObjectName("cancelButton")

        self.retranslateUi(GDMLScale)
        QtCore.QMetaObject.connectSlotsByName(GDMLScale)

    def retranslateUi(self, GDMLScale):
        _translate = QtCore.QCoreApplication.translate
        GDMLScale.setWindowTitle(_translate("GDMLScale", "Scale GDML solids"))
        self.checkBox.setText(_translate("GDMLScale", "Uniform scaling"))
        self.xlabel.setText(_translate("GDMLScale", "X factor"))
        self.yLabel.setText(_translate("GDMLScale", "Y factor"))
        self.zLabel.setText(_translate("GDMLScale", "Z factor"))
        self.scaleButton.setText(_translate("GDMLScale", "OK"))
        self.cancelButton.setText(_translate("GDMLScale", "Cancel"))