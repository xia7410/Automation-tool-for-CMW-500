# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cmw500autoMW.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_CMW500AutomationTool(object):
    def setupUi(self, CMW500AutomationTool):
        CMW500AutomationTool.setObjectName(_fromUtf8("CMW500AutomationTool"))
        CMW500AutomationTool.setWindowModality(QtCore.Qt.WindowModal)
        CMW500AutomationTool.resize(790, 270)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nirmala UI"))
        CMW500AutomationTool.setFont(font)
        CMW500AutomationTool.setWindowOpacity(1.0)
        self.centralwidget = QtGui.QWidget(CMW500AutomationTool)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 791, 581))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Triangular)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.AttenuationManager = QtGui.QWidget()
        self.AttenuationManager.setObjectName(_fromUtf8("AttenuationManager"))
        self.groupBoxRF2 = QtGui.QGroupBox(self.AttenuationManager)
        self.groupBoxRF2.setEnabled(True)
        self.groupBoxRF2.setGeometry(QtCore.QRect(10, 89, 641, 71))
        self.groupBoxRF2.setTitle(_fromUtf8(""))
        self.groupBoxRF2.setObjectName(_fromUtf8("groupBoxRF2"))
        self.checkBoxRF2 = QtGui.QCheckBox(self.groupBoxRF2)
        self.checkBoxRF2.setGeometry(QtCore.QRect(40, 50, 16, 17))
        self.checkBoxRF2.setText(_fromUtf8(""))
        self.checkBoxRF2.setObjectName(_fromUtf8("checkBoxRF2"))
        self.labelRF2Step = QtGui.QLabel(self.groupBoxRF2)
        self.labelRF2Step.setGeometry(QtCore.QRect(420, 23, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelRF2Step.setFont(font)
        self.labelRF2Step.setObjectName(_fromUtf8("labelRF2Step"))
        self.lineEditRF2max = QtGui.QLineEdit(self.groupBoxRF2)
        self.lineEditRF2max.setGeometry(QtCore.QRect(350, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditRF2max.setFont(font)
        self.lineEditRF2max.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEditRF2max.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditRF2max.setObjectName(_fromUtf8("lineEditRF2max"))
        self.lineEditRF2Step = QtGui.QLineEdit(self.groupBoxRF2)
        self.lineEditRF2Step.setGeometry(QtCore.QRect(460, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditRF2Step.setFont(font)
        self.lineEditRF2Step.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEditRF2Step.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditRF2Step.setObjectName(_fromUtf8("lineEditRF2Step"))
        self.labelRF2Time = QtGui.QLabel(self.groupBoxRF2)
        self.labelRF2Time.setGeometry(QtCore.QRect(530, 23, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelRF2Time.setFont(font)
        self.labelRF2Time.setObjectName(_fromUtf8("labelRF2Time"))
        self.lineEditRF2min = QtGui.QLineEdit(self.groupBoxRF2)
        self.lineEditRF2min.setGeometry(QtCore.QRect(120, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditRF2min.setFont(font)
        self.lineEditRF2min.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEditRF2min.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditRF2min.setObjectName(_fromUtf8("lineEditRF2min"))
        self.horizontalSliderRF2 = QtGui.QSlider(self.groupBoxRF2)
        self.horizontalSliderRF2.setGeometry(QtCore.QRect(180, 39, 161, 20))
        self.horizontalSliderRF2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderRF2.setObjectName(_fromUtf8("horizontalSliderRF2"))
        self.labelRF2 = QtGui.QLabel(self.groupBoxRF2)
        self.labelRF2.setGeometry(QtCore.QRect(10, 13, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelRF2.setFont(font)
        self.labelRF2.setObjectName(_fromUtf8("labelRF2"))
        self.lineEditRF2Time = QtGui.QLineEdit(self.groupBoxRF2)
        self.lineEditRF2Time.setGeometry(QtCore.QRect(580, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditRF2Time.setFont(font)
        self.lineEditRF2Time.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEditRF2Time.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditRF2Time.setObjectName(_fromUtf8("lineEditRF2Time"))
        self.label_5 = QtGui.QLabel(self.groupBoxRF2)
        self.label_5.setGeometry(QtCore.QRect(580, 10, 51, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.groupBoxRF2)
        self.label_6.setGeometry(QtCore.QRect(460, 10, 41, 20))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.groupBoxRF2)
        self.label_7.setGeometry(QtCore.QRect(100, 10, 91, 16))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.groupBoxRF2)
        self.label_8.setGeometry(QtCore.QRect(330, 10, 91, 16))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.groupBoxRF1 = QtGui.QGroupBox(self.AttenuationManager)
        self.groupBoxRF1.setEnabled(True)
        self.groupBoxRF1.setGeometry(QtCore.QRect(10, 10, 641, 71))
        self.groupBoxRF1.setTitle(_fromUtf8(""))
        self.groupBoxRF1.setObjectName(_fromUtf8("groupBoxRF1"))
        self.lineEditRF1Step = QtGui.QLineEdit(self.groupBoxRF1)
        self.lineEditRF1Step.setGeometry(QtCore.QRect(460, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditRF1Step.setFont(font)
        self.lineEditRF1Step.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEditRF1Step.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditRF1Step.setObjectName(_fromUtf8("lineEditRF1Step"))
        self.horizontalSliderRF1 = QtGui.QSlider(self.groupBoxRF1)
        self.horizontalSliderRF1.setGeometry(QtCore.QRect(180, 39, 161, 20))
        self.horizontalSliderRF1.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderRF1.setObjectName(_fromUtf8("horizontalSliderRF1"))
        self.checkBoxRF1 = QtGui.QCheckBox(self.groupBoxRF1)
        self.checkBoxRF1.setGeometry(QtCore.QRect(40, 50, 16, 17))
        self.checkBoxRF1.setText(_fromUtf8(""))
        self.checkBoxRF1.setObjectName(_fromUtf8("checkBoxRF1"))
        self.lineEditRF1Time = QtGui.QLineEdit(self.groupBoxRF1)
        self.lineEditRF1Time.setGeometry(QtCore.QRect(580, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditRF1Time.setFont(font)
        self.lineEditRF1Time.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEditRF1Time.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditRF1Time.setObjectName(_fromUtf8("lineEditRF1Time"))
        self.lineEditRF1max = QtGui.QLineEdit(self.groupBoxRF1)
        self.lineEditRF1max.setGeometry(QtCore.QRect(350, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditRF1max.setFont(font)
        self.lineEditRF1max.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEditRF1max.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditRF1max.setObjectName(_fromUtf8("lineEditRF1max"))
        self.labelRF1Time = QtGui.QLabel(self.groupBoxRF1)
        self.labelRF1Time.setGeometry(QtCore.QRect(530, 23, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelRF1Time.setFont(font)
        self.labelRF1Time.setObjectName(_fromUtf8("labelRF1Time"))
        self.labelRF1Step = QtGui.QLabel(self.groupBoxRF1)
        self.labelRF1Step.setGeometry(QtCore.QRect(420, 23, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelRF1Step.setFont(font)
        self.labelRF1Step.setObjectName(_fromUtf8("labelRF1Step"))
        self.lineEditRF1min = QtGui.QLineEdit(self.groupBoxRF1)
        self.lineEditRF1min.setGeometry(QtCore.QRect(120, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditRF1min.setFont(font)
        self.lineEditRF1min.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEditRF1min.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditRF1min.setObjectName(_fromUtf8("lineEditRF1min"))
        self.labelRF1 = QtGui.QLabel(self.groupBoxRF1)
        self.labelRF1.setGeometry(QtCore.QRect(10, 13, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelRF1.setFont(font)
        self.labelRF1.setObjectName(_fromUtf8("labelRF1"))
        self.label = QtGui.QLabel(self.groupBoxRF1)
        self.label.setGeometry(QtCore.QRect(100, 10, 91, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBoxRF1)
        self.label_2.setGeometry(QtCore.QRect(330, 10, 91, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBoxRF1)
        self.label_3.setGeometry(QtCore.QRect(460, 10, 41, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBoxRF1)
        self.label_4.setGeometry(QtCore.QRect(580, 10, 51, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButtonStart = QtGui.QPushButton(self.AttenuationManager)
        self.pushButtonStart.setEnabled(False)
        self.pushButtonStart.setGeometry(QtCore.QRect(530, 170, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonStart.setFont(font)
        self.pushButtonStart.setObjectName(_fromUtf8("pushButtonStart"))
        self.pushButtonConnect = QtGui.QPushButton(self.AttenuationManager)
        self.pushButtonConnect.setGeometry(QtCore.QRect(20, 170, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonConnect.setFont(font)
        self.pushButtonConnect.setObjectName(_fromUtf8("pushButtonConnect"))
        self.labelDisconect = QtGui.QLabel(self.AttenuationManager)
        self.labelDisconect.setEnabled(False)
        self.labelDisconect.setGeometry(QtCore.QRect(140, 175, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelDisconect.setFont(font)
        self.labelDisconect.setTextFormat(QtCore.Qt.AutoText)
        self.labelDisconect.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDisconect.setTextInteractionFlags(QtCore.Qt.TextEditable)
        self.labelDisconect.setObjectName(_fromUtf8("labelDisconect"))
        self.pushButtonClose = QtGui.QPushButton(self.AttenuationManager)
        self.pushButtonClose.setGeometry(QtCore.QRect(660, 170, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonClose.setFont(font)
        self.pushButtonClose.setObjectName(_fromUtf8("pushButtonClose"))
        self.labelLoop = QtGui.QLabel(self.AttenuationManager)
        self.labelLoop.setGeometry(QtCore.QRect(670, 50, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelLoop.setFont(font)
        self.labelLoop.setObjectName(_fromUtf8("labelLoop"))
        self.lineEditLoop = QtGui.QLineEdit(self.AttenuationManager)
        self.lineEditLoop.setGeometry(QtCore.QRect(720, 57, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditLoop.setFont(font)
        self.lineEditLoop.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEditLoop.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditLoop.setObjectName(_fromUtf8("lineEditLoop"))
        self.tabWidget.addTab(self.AttenuationManager, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        CMW500AutomationTool.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(CMW500AutomationTool)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        CMW500AutomationTool.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(CMW500AutomationTool)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 790, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        CMW500AutomationTool.setMenuBar(self.menubar)

        self.retranslateUi(CMW500AutomationTool)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.pushButtonClose, QtCore.SIGNAL(_fromUtf8("clicked()")), CMW500AutomationTool.close)
        QtCore.QMetaObject.connectSlotsByName(CMW500AutomationTool)

    def retranslateUi(self, CMW500AutomationTool):
        CMW500AutomationTool.setWindowTitle(_translate("CMW500AutomationTool", "CMW500 Automation Tool", None))
        self.labelRF2Step.setText(_translate("CMW500AutomationTool", "Step:", None))
        self.lineEditRF2max.setText(_translate("CMW500AutomationTool", "-110", None))
        self.lineEditRF2Step.setText(_translate("CMW500AutomationTool", "5", None))
        self.labelRF2Time.setText(_translate("CMW500AutomationTool", "Time:", None))
        self.lineEditRF2min.setText(_translate("CMW500AutomationTool", "-90", None))
        self.labelRF2.setText(_translate("CMW500AutomationTool", "LTE SIG 2", None))
        self.lineEditRF2Time.setText(_translate("CMW500AutomationTool", "1", None))
        self.label_5.setText(_translate("CMW500AutomationTool", "[s]", None))
        self.label_6.setText(_translate("CMW500AutomationTool", " [dBm]", None))
        self.label_7.setText(_translate("CMW500AutomationTool", "Begin [dBm]", None))
        self.label_8.setText(_translate("CMW500AutomationTool", "End [dBm]", None))
        self.lineEditRF1Step.setText(_translate("CMW500AutomationTool", "5", None))
        self.lineEditRF1Time.setText(_translate("CMW500AutomationTool", "1", None))
        self.lineEditRF1max.setText(_translate("CMW500AutomationTool", "-90", None))
        self.labelRF1Time.setText(_translate("CMW500AutomationTool", "Time:", None))
        self.labelRF1Step.setText(_translate("CMW500AutomationTool", "Step:", None))
        self.lineEditRF1min.setText(_translate("CMW500AutomationTool", "-110", None))
        self.labelRF1.setText(_translate("CMW500AutomationTool", "LTE SIG 1", None))
        self.label.setText(_translate("CMW500AutomationTool", "Begin [dBm]", None))
        self.label_2.setText(_translate("CMW500AutomationTool", "End [dBm]", None))
        self.label_3.setText(_translate("CMW500AutomationTool", " [dBm]", None))
        self.label_4.setText(_translate("CMW500AutomationTool", "[s]", None))
        self.pushButtonStart.setText(_translate("CMW500AutomationTool", "Start", None))
        self.pushButtonConnect.setText(_translate("CMW500AutomationTool", "Connect", None))
        self.labelDisconect.setText(_translate("CMW500AutomationTool", "Disconnect", None))
        self.pushButtonClose.setText(_translate("CMW500AutomationTool", "Close", None))
        self.labelLoop.setText(_translate("CMW500AutomationTool", "Loop:", None))
        self.lineEditLoop.setText(_translate("CMW500AutomationTool", "1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AttenuationManager), _translate("CMW500AutomationTool", "Attenuation Manager", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("CMW500AutomationTool", "Tab 2", None))

