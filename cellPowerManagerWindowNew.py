# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cellPowerManagerWindow.ui'
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

class Ui_cellPowerManagerWindow(object):
    def setupUi(self, cellPowerManagerWindow):
        cellPowerManagerWindow.setObjectName(_fromUtf8("cellPowerManagerWindow"))
        cellPowerManagerWindow.resize(813, 241)
        self.comboBoxTestType = QtGui.QComboBox(cellPowerManagerWindow)
        self.comboBoxTestType.setGeometry(QtCore.QRect(10, 10, 191, 22))
        self.comboBoxTestType.setObjectName(_fromUtf8("comboBoxTestType"))
        self.comboBoxTestType.addItem(_fromUtf8(""))
        self.comboBoxTestType.setItemText(0, _fromUtf8(""))
        self.comboBoxTestType.addItem(_fromUtf8(""))
        self.comboBoxTestType.addItem(_fromUtf8(""))
        self.comboBoxTestType.addItem(_fromUtf8(""))
        self.comboBoxTestType.addItem(_fromUtf8(""))
        self.groupBoxSign1 = QtGui.QGroupBox(cellPowerManagerWindow)
        self.groupBoxSign1.setEnabled(True)
        self.groupBoxSign1.setGeometry(QtCore.QRect(10, 40, 651, 91))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.groupBoxSign1.setFont(font)
        self.groupBoxSign1.setObjectName(_fromUtf8("groupBoxSign1"))
        self.lineEditStepSign1 = QtGui.QLineEdit(self.groupBoxSign1)
        self.lineEditStepSign1.setGeometry(QtCore.QRect(460, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditStepSign1.setFont(font)
        self.lineEditStepSign1.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEditStepSign1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditStepSign1.setObjectName(_fromUtf8("lineEditStepSign1"))
        self.horizontalSliderSign1 = QtGui.QSlider(self.groupBoxSign1)
        self.horizontalSliderSign1.setGeometry(QtCore.QRect(180, 39, 161, 20))
        self.horizontalSliderSign1.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderSign1.setObjectName(_fromUtf8("horizontalSliderSign1"))
        self.lineEditTimeSign1 = QtGui.QLineEdit(self.groupBoxSign1)
        self.lineEditTimeSign1.setGeometry(QtCore.QRect(580, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditTimeSign1.setFont(font)
        self.lineEditTimeSign1.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEditTimeSign1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditTimeSign1.setObjectName(_fromUtf8("lineEditTimeSign1"))
        self.lineEditMaxSign1 = QtGui.QLineEdit(self.groupBoxSign1)
        self.lineEditMaxSign1.setGeometry(QtCore.QRect(350, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditMaxSign1.setFont(font)
        self.lineEditMaxSign1.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEditMaxSign1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditMaxSign1.setObjectName(_fromUtf8("lineEditMaxSign1"))
        self.labelTimeSign1Name = QtGui.QLabel(self.groupBoxSign1)
        self.labelTimeSign1Name.setGeometry(QtCore.QRect(530, 23, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.labelTimeSign1Name.setFont(font)
        self.labelTimeSign1Name.setObjectName(_fromUtf8("labelTimeSign1Name"))
        self.labelStepSign1Name = QtGui.QLabel(self.groupBoxSign1)
        self.labelStepSign1Name.setGeometry(QtCore.QRect(420, 23, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.labelStepSign1Name.setFont(font)
        self.labelStepSign1Name.setObjectName(_fromUtf8("labelStepSign1Name"))
        self.lineEditMinSign1 = QtGui.QLineEdit(self.groupBoxSign1)
        self.lineEditMinSign1.setGeometry(QtCore.QRect(120, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditMinSign1.setFont(font)
        self.lineEditMinSign1.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEditMinSign1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditMinSign1.setObjectName(_fromUtf8("lineEditMinSign1"))
        self.labelBeginSign1 = QtGui.QLabel(self.groupBoxSign1)
        self.labelBeginSign1.setGeometry(QtCore.QRect(100, 10, 91, 16))
        self.labelBeginSign1.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBeginSign1.setObjectName(_fromUtf8("labelBeginSign1"))
        self.labelEndSign1 = QtGui.QLabel(self.groupBoxSign1)
        self.labelEndSign1.setGeometry(QtCore.QRect(330, 10, 91, 16))
        self.labelEndSign1.setAlignment(QtCore.Qt.AlignCenter)
        self.labelEndSign1.setObjectName(_fromUtf8("labelEndSign1"))
        self.labelStepSign1Unit = QtGui.QLabel(self.groupBoxSign1)
        self.labelStepSign1Unit.setGeometry(QtCore.QRect(460, 10, 41, 20))
        self.labelStepSign1Unit.setAlignment(QtCore.Qt.AlignCenter)
        self.labelStepSign1Unit.setObjectName(_fromUtf8("labelStepSign1Unit"))
        self.labelTimeSign1Unit = QtGui.QLabel(self.groupBoxSign1)
        self.labelTimeSign1Unit.setGeometry(QtCore.QRect(580, 10, 51, 20))
        self.labelTimeSign1Unit.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTimeSign1Unit.setObjectName(_fromUtf8("labelTimeSign1Unit"))
        self.comboBoxSign1 = QtGui.QComboBox(self.groupBoxSign1)
        self.comboBoxSign1.setGeometry(QtCore.QRect(10, 20, 69, 22))
        self.comboBoxSign1.setObjectName(_fromUtf8("comboBoxSign1"))
        self.comboBoxSign1.addItem(_fromUtf8(""))
        self.comboBoxSign1.addItem(_fromUtf8(""))
        self.comboBoxSign1.addItem(_fromUtf8(""))
        self.groupBoxSign2 = QtGui.QGroupBox(cellPowerManagerWindow)
        self.groupBoxSign2.setEnabled(True)
        self.groupBoxSign2.setGeometry(QtCore.QRect(10, 40, 651, 91))
        self.groupBoxSign2.setObjectName(_fromUtf8("groupBoxSign2"))
        self.labelStepSign2Name = QtGui.QLabel(self.groupBoxSign2)
        self.labelStepSign2Name.setGeometry(QtCore.QRect(420, 23, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.labelStepSign2Name.setFont(font)
        self.labelStepSign2Name.setObjectName(_fromUtf8("labelStepSign2Name"))
        self.lineEditMaxSign2 = QtGui.QLineEdit(self.groupBoxSign2)
        self.lineEditMaxSign2.setGeometry(QtCore.QRect(350, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditMaxSign2.setFont(font)
        self.lineEditMaxSign2.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEditMaxSign2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditMaxSign2.setObjectName(_fromUtf8("lineEditMaxSign2"))
        self.lineEditStepSign2 = QtGui.QLineEdit(self.groupBoxSign2)
        self.lineEditStepSign2.setGeometry(QtCore.QRect(460, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditStepSign2.setFont(font)
        self.lineEditStepSign2.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEditStepSign2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditStepSign2.setObjectName(_fromUtf8("lineEditStepSign2"))
        self.lineEditMinSign2 = QtGui.QLineEdit(self.groupBoxSign2)
        self.lineEditMinSign2.setGeometry(QtCore.QRect(120, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditMinSign2.setFont(font)
        self.lineEditMinSign2.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEditMinSign2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditMinSign2.setObjectName(_fromUtf8("lineEditMinSign2"))
        self.horizontalSliderSign2 = QtGui.QSlider(self.groupBoxSign2)
        self.horizontalSliderSign2.setGeometry(QtCore.QRect(180, 39, 161, 20))
        self.horizontalSliderSign2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderSign2.setObjectName(_fromUtf8("horizontalSliderSign2"))
        self.lineEditTimeSign2 = QtGui.QLineEdit(self.groupBoxSign2)
        self.lineEditTimeSign2.setGeometry(QtCore.QRect(580, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditTimeSign2.setFont(font)
        self.lineEditTimeSign2.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEditTimeSign2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditTimeSign2.setObjectName(_fromUtf8("lineEditTimeSign2"))
        self.labelTimeSign2Unit = QtGui.QLabel(self.groupBoxSign2)
        self.labelTimeSign2Unit.setGeometry(QtCore.QRect(580, 10, 51, 20))
        self.labelTimeSign2Unit.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTimeSign2Unit.setObjectName(_fromUtf8("labelTimeSign2Unit"))
        self.labelStepSign2Unit = QtGui.QLabel(self.groupBoxSign2)
        self.labelStepSign2Unit.setGeometry(QtCore.QRect(460, 10, 41, 20))
        self.labelStepSign2Unit.setAlignment(QtCore.Qt.AlignCenter)
        self.labelStepSign2Unit.setObjectName(_fromUtf8("labelStepSign2Unit"))
        self.labelBeginSign2 = QtGui.QLabel(self.groupBoxSign2)
        self.labelBeginSign2.setGeometry(QtCore.QRect(100, 10, 91, 16))
        self.labelBeginSign2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBeginSign2.setObjectName(_fromUtf8("labelBeginSign2"))
        self.labelEndSign2 = QtGui.QLabel(self.groupBoxSign2)
        self.labelEndSign2.setGeometry(QtCore.QRect(330, 10, 91, 16))
        self.labelEndSign2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelEndSign2.setObjectName(_fromUtf8("labelEndSign2"))
        self.comboBoxSign2 = QtGui.QComboBox(self.groupBoxSign2)
        self.comboBoxSign2.setGeometry(QtCore.QRect(10, 20, 69, 22))
        self.comboBoxSign2.setObjectName(_fromUtf8("comboBoxSign2"))
        self.comboBoxSign2.addItem(_fromUtf8(""))
        self.comboBoxSign2.addItem(_fromUtf8(""))
        self.comboBoxSign2.addItem(_fromUtf8(""))
        self.labelTimeSign2Name = QtGui.QLabel(self.groupBoxSign2)
        self.labelTimeSign2Name.setGeometry(QtCore.QRect(530, 23, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.labelTimeSign2Name.setFont(font)
        self.labelTimeSign2Name.setObjectName(_fromUtf8("labelTimeSign2Name"))
        self.groupBoxSignSynch = QtGui.QGroupBox(cellPowerManagerWindow)
        self.groupBoxSignSynch.setEnabled(True)
        self.groupBoxSignSynch.setGeometry(QtCore.QRect(10, 40, 651, 131))
        self.groupBoxSignSynch.setObjectName(_fromUtf8("groupBoxSignSynch"))
        self.labelStepSignSynchName = QtGui.QLabel(self.groupBoxSignSynch)
        self.labelStepSignSynchName.setGeometry(QtCore.QRect(420, 53, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.labelStepSignSynchName.setFont(font)
        self.labelStepSignSynchName.setObjectName(_fromUtf8("labelStepSignSynchName"))
        self.lineEditMaxSignSynch1 = QtGui.QLineEdit(self.groupBoxSignSynch)
        self.lineEditMaxSignSynch1.setGeometry(QtCore.QRect(350, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditMaxSignSynch1.setFont(font)
        self.lineEditMaxSignSynch1.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEditMaxSignSynch1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditMaxSignSynch1.setObjectName(_fromUtf8("lineEditMaxSignSynch1"))
        self.lineEditStepSignSynch = QtGui.QLineEdit(self.groupBoxSignSynch)
        self.lineEditStepSignSynch.setGeometry(QtCore.QRect(460, 60, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditStepSignSynch.setFont(font)
        self.lineEditStepSignSynch.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEditStepSignSynch.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditStepSignSynch.setObjectName(_fromUtf8("lineEditStepSignSynch"))
        self.lineEditMinSignSynch1 = QtGui.QLineEdit(self.groupBoxSignSynch)
        self.lineEditMinSignSynch1.setGeometry(QtCore.QRect(120, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditMinSignSynch1.setFont(font)
        self.lineEditMinSignSynch1.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEditMinSignSynch1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditMinSignSynch1.setObjectName(_fromUtf8("lineEditMinSignSynch1"))
        self.horizontalSliderSignSynch1 = QtGui.QSlider(self.groupBoxSignSynch)
        self.horizontalSliderSignSynch1.setGeometry(QtCore.QRect(180, 39, 161, 20))
        self.horizontalSliderSignSynch1.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderSignSynch1.setObjectName(_fromUtf8("horizontalSliderSignSynch1"))
        self.lineEditTimeSignSynch = QtGui.QLineEdit(self.groupBoxSignSynch)
        self.lineEditTimeSignSynch.setGeometry(QtCore.QRect(580, 60, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditTimeSignSynch.setFont(font)
        self.lineEditTimeSignSynch.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEditTimeSignSynch.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditTimeSignSynch.setObjectName(_fromUtf8("lineEditTimeSignSynch"))
        self.labelTimeSignSynchUnit = QtGui.QLabel(self.groupBoxSignSynch)
        self.labelTimeSignSynchUnit.setGeometry(QtCore.QRect(580, 40, 51, 20))
        self.labelTimeSignSynchUnit.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTimeSignSynchUnit.setObjectName(_fromUtf8("labelTimeSignSynchUnit"))
        self.labelStepSignSynchUnit = QtGui.QLabel(self.groupBoxSignSynch)
        self.labelStepSignSynchUnit.setGeometry(QtCore.QRect(460, 40, 41, 20))
        self.labelStepSignSynchUnit.setAlignment(QtCore.Qt.AlignCenter)
        self.labelStepSignSynchUnit.setObjectName(_fromUtf8("labelStepSignSynchUnit"))
        self.labelBeginSignSynch1 = QtGui.QLabel(self.groupBoxSignSynch)
        self.labelBeginSignSynch1.setGeometry(QtCore.QRect(100, 10, 91, 16))
        self.labelBeginSignSynch1.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBeginSignSynch1.setObjectName(_fromUtf8("labelBeginSignSynch1"))
        self.labelEndSignSynch1 = QtGui.QLabel(self.groupBoxSignSynch)
        self.labelEndSignSynch1.setGeometry(QtCore.QRect(330, 10, 91, 16))
        self.labelEndSignSynch1.setAlignment(QtCore.Qt.AlignCenter)
        self.labelEndSignSynch1.setObjectName(_fromUtf8("labelEndSignSynch1"))
        self.comboBoxSignSynch1 = QtGui.QComboBox(self.groupBoxSignSynch)
        self.comboBoxSignSynch1.setGeometry(QtCore.QRect(10, 20, 69, 22))
        self.comboBoxSignSynch1.setObjectName(_fromUtf8("comboBoxSignSynch1"))
        self.comboBoxSignSynch1.addItem(_fromUtf8(""))
        self.comboBoxSignSynch1.addItem(_fromUtf8(""))
        self.comboBoxSignSynch1.addItem(_fromUtf8(""))
        self.lineEditMinSignSynch2 = QtGui.QLineEdit(self.groupBoxSignSynch)
        self.lineEditMinSignSynch2.setGeometry(QtCore.QRect(120, 90, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditMinSignSynch2.setFont(font)
        self.lineEditMinSignSynch2.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEditMinSignSynch2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditMinSignSynch2.setObjectName(_fromUtf8("lineEditMinSignSynch2"))
        self.lineEditMaxSignSynch2 = QtGui.QLineEdit(self.groupBoxSignSynch)
        self.lineEditMaxSignSynch2.setGeometry(QtCore.QRect(350, 90, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditMaxSignSynch2.setFont(font)
        self.lineEditMaxSignSynch2.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEditMaxSignSynch2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditMaxSignSynch2.setObjectName(_fromUtf8("lineEditMaxSignSynch2"))
        self.labelBeginSignSynch2 = QtGui.QLabel(self.groupBoxSignSynch)
        self.labelBeginSignSynch2.setGeometry(QtCore.QRect(100, 70, 91, 16))
        self.labelBeginSignSynch2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBeginSignSynch2.setObjectName(_fromUtf8("labelBeginSignSynch2"))
        self.labelEndSignSynch2 = QtGui.QLabel(self.groupBoxSignSynch)
        self.labelEndSignSynch2.setGeometry(QtCore.QRect(330, 70, 91, 16))
        self.labelEndSignSynch2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelEndSignSynch2.setObjectName(_fromUtf8("labelEndSignSynch2"))
        self.horizontalSliderSignSynch2 = QtGui.QSlider(self.groupBoxSignSynch)
        self.horizontalSliderSignSynch2.setGeometry(QtCore.QRect(180, 99, 161, 20))
        self.horizontalSliderSignSynch2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderSignSynch2.setObjectName(_fromUtf8("horizontalSliderSignSynch2"))
        self.labelSliderSignSynch1Name = QtGui.QLabel(self.groupBoxSignSynch)
        self.labelSliderSignSynch1Name.setGeometry(QtCore.QRect(230, 20, 51, 16))
        self.labelSliderSignSynch1Name.setObjectName(_fromUtf8("labelSliderSignSynch1Name"))
        self.labelSliderSignSynch2Name = QtGui.QLabel(self.groupBoxSignSynch)
        self.labelSliderSignSynch2Name.setGeometry(QtCore.QRect(230, 70, 51, 16))
        self.labelSliderSignSynch2Name.setObjectName(_fromUtf8("labelSliderSignSynch2Name"))
        self.labelTimeSignSynchName = QtGui.QLabel(self.groupBoxSignSynch)
        self.labelTimeSignSynchName.setGeometry(QtCore.QRect(530, 50, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.labelTimeSignSynchName.setFont(font)
        self.labelTimeSignSynchName.setObjectName(_fromUtf8("labelTimeSignSynchName"))
        self.comboBoxSignSynch2 = QtGui.QComboBox(self.groupBoxSignSynch)
        self.comboBoxSignSynch2.setGeometry(QtCore.QRect(10, 80, 69, 22))
        self.comboBoxSignSynch2.setObjectName(_fromUtf8("comboBoxSignSynch2"))
        self.comboBoxSignSynch2.addItem(_fromUtf8(""))
        self.comboBoxSignSynch2.addItem(_fromUtf8(""))
        self.comboBoxSignSynch2.addItem(_fromUtf8(""))
        self.pushButtonSave = QtGui.QPushButton(cellPowerManagerWindow)
        self.pushButtonSave.setGeometry(QtCore.QRect(10, 190, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonSave.setFont(font)
        self.pushButtonSave.setObjectName(_fromUtf8("pushButtonSave"))
        self.labelTestDuration = QtGui.QLabel(cellPowerManagerWindow)
        self.labelTestDuration.setGeometry(QtCore.QRect(290, 10, 71, 21))
        self.labelTestDuration.setObjectName(_fromUtf8("labelTestDuration"))
        self.timeEditTestDuration = QtGui.QTimeEdit(cellPowerManagerWindow)
        self.timeEditTestDuration.setEnabled(False)
        self.timeEditTestDuration.setGeometry(QtCore.QRect(450, 190, 61, 22))
        font = QtGui.QFont()
        font.setKerning(True)
        self.timeEditTestDuration.setFont(font)
        self.timeEditTestDuration.setMouseTracking(False)
        self.timeEditTestDuration.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.timeEditTestDuration.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.timeEditTestDuration.setWrapping(False)
        self.timeEditTestDuration.setFrame(True)
        self.timeEditTestDuration.setAlignment(QtCore.Qt.AlignCenter)
        self.timeEditTestDuration.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.timeEditTestDuration.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToPreviousValue)
        self.timeEditTestDuration.setObjectName(_fromUtf8("timeEditTestDuration"))
        self.dateTimeEditTestEnd = QtGui.QDateTimeEdit(cellPowerManagerWindow)
        self.dateTimeEditTestEnd.setEnabled(False)
        self.dateTimeEditTestEnd.setGeometry(QtCore.QRect(540, 10, 121, 22))
        font = QtGui.QFont()
        font.setKerning(True)
        self.dateTimeEditTestEnd.setFont(font)
        self.dateTimeEditTestEnd.setMouseTracking(False)
        self.dateTimeEditTestEnd.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.dateTimeEditTestEnd.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.dateTimeEditTestEnd.setWrapping(False)
        self.dateTimeEditTestEnd.setFrame(True)
        self.dateTimeEditTestEnd.setAlignment(QtCore.Qt.AlignCenter)
        self.dateTimeEditTestEnd.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.dateTimeEditTestEnd.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToPreviousValue)
        self.dateTimeEditTestEnd.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 1, 3), QtCore.QTime(0, 0, 0)))
        self.dateTimeEditTestEnd.setDate(QtCore.QDate(2018, 1, 3))
        self.dateTimeEditTestEnd.setMaximumDate(QtCore.QDate(2080, 1, 1))
        self.dateTimeEditTestEnd.setMinimumDate(QtCore.QDate(2017, 1, 1))
        self.dateTimeEditTestEnd.setObjectName(_fromUtf8("dateTimeEditTestEnd"))
        self.labelTestEnd = QtGui.QLabel(cellPowerManagerWindow)
        self.labelTestEnd.setGeometry(QtCore.QRect(460, 10, 91, 21))
        self.labelTestEnd.setObjectName(_fromUtf8("labelTestEnd"))
        self.groupBoxLoop = QtGui.QGroupBox(cellPowerManagerWindow)
        self.groupBoxLoop.setGeometry(QtCore.QRect(670, 46, 131, 111))
        self.groupBoxLoop.setTitle(_fromUtf8(""))
        self.groupBoxLoop.setObjectName(_fromUtf8("groupBoxLoop"))
        self.labelLoopDelayUnit = QtGui.QLabel(self.groupBoxLoop)
        self.labelLoopDelayUnit.setGeometry(QtCore.QRect(70, 50, 51, 20))
        self.labelLoopDelayUnit.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLoopDelayUnit.setObjectName(_fromUtf8("labelLoopDelayUnit"))
        self.labelLoop = QtGui.QLabel(self.groupBoxLoop)
        self.labelLoop.setGeometry(QtCore.QRect(10, 10, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.labelLoop.setFont(font)
        self.labelLoop.setObjectName(_fromUtf8("labelLoop"))
        self.lineEditLoopDelay = QtGui.QLineEdit(self.groupBoxLoop)
        self.lineEditLoopDelay.setGeometry(QtCore.QRect(70, 70, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditLoopDelay.setFont(font)
        self.lineEditLoopDelay.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEditLoopDelay.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditLoopDelay.setObjectName(_fromUtf8("lineEditLoopDelay"))
        self.lineEditLoop = QtGui.QLineEdit(self.groupBoxLoop)
        self.lineEditLoop.setGeometry(QtCore.QRect(70, 10, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditLoop.setFont(font)
        self.lineEditLoop.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEditLoop.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditLoop.setObjectName(_fromUtf8("lineEditLoop"))
        self.labelLoopDelay = QtGui.QLabel(self.groupBoxLoop)
        self.labelLoopDelay.setGeometry(QtCore.QRect(10, 63, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.labelLoopDelay.setFont(font)
        self.labelLoopDelay.setObjectName(_fromUtf8("labelLoopDelay"))
        self.pushButtonClose = QtGui.QPushButton(cellPowerManagerWindow)
        self.pushButtonClose.setGeometry(QtCore.QRect(660, 190, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonClose.setFont(font)
        self.pushButtonClose.setObjectName(_fromUtf8("pushButtonClose"))
        self.lineEditTestDuration = QtGui.QLineEdit(cellPowerManagerWindow)
        self.lineEditTestDuration.setEnabled(False)
        self.lineEditTestDuration.setGeometry(QtCore.QRect(360, 10, 61, 22))
        self.lineEditTestDuration.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditTestDuration.setObjectName(_fromUtf8("lineEditTestDuration"))

        self.retranslateUi(cellPowerManagerWindow)
        QtCore.QObject.connect(self.pushButtonClose, QtCore.SIGNAL(_fromUtf8("clicked()")), cellPowerManagerWindow.close)
        QtCore.QMetaObject.connectSlotsByName(cellPowerManagerWindow)

    def retranslateUi(self, cellPowerManagerWindow):
        cellPowerManagerWindow.setWindowTitle(_translate("cellPowerManagerWindow", "Cell Power Manager", None))
        self.comboBoxTestType.setItemText(1, _translate("cellPowerManagerWindow", "Signaling 1", None))
        self.comboBoxTestType.setItemText(2, _translate("cellPowerManagerWindow", "Signaling 2", None))
        self.comboBoxTestType.setItemText(3, _translate("cellPowerManagerWindow", "Signaling 1 and 2 synchronously", None))
        self.comboBoxTestType.setItemText(4, _translate("cellPowerManagerWindow", "Signaling 1 and 2 not synchronously", None))
        self.groupBoxSign1.setTitle(_translate("cellPowerManagerWindow", "Signaling 1", None))
        self.lineEditStepSign1.setText(_translate("cellPowerManagerWindow", "0", None))
        self.lineEditTimeSign1.setText(_translate("cellPowerManagerWindow", "0", None))
        self.lineEditMaxSign1.setText(_translate("cellPowerManagerWindow", "-45", None))
        self.labelTimeSign1Name.setText(_translate("cellPowerManagerWindow", "Step \n"
"delay:", None))
        self.labelStepSign1Name.setText(_translate("cellPowerManagerWindow", "Step:", None))
        self.lineEditMinSign1.setText(_translate("cellPowerManagerWindow", "-140", None))
        self.labelBeginSign1.setText(_translate("cellPowerManagerWindow", "Begin [dBm]", None))
        self.labelEndSign1.setText(_translate("cellPowerManagerWindow", "End [dBm]", None))
        self.labelStepSign1Unit.setText(_translate("cellPowerManagerWindow", " [dBm]", None))
        self.labelTimeSign1Unit.setText(_translate("cellPowerManagerWindow", "[s]", None))
        self.comboBoxSign1.setItemText(0, _translate("cellPowerManagerWindow", "LTE", None))
        self.comboBoxSign1.setItemText(1, _translate("cellPowerManagerWindow", "WCDMA", None))
        self.comboBoxSign1.setItemText(2, _translate("cellPowerManagerWindow", "GSM", None))
        self.groupBoxSign2.setTitle(_translate("cellPowerManagerWindow", "Signaling 2", None))
        self.labelStepSign2Name.setText(_translate("cellPowerManagerWindow", "Step:", None))
        self.lineEditMaxSign2.setText(_translate("cellPowerManagerWindow", "-45", None))
        self.lineEditStepSign2.setText(_translate("cellPowerManagerWindow", "0", None))
        self.lineEditMinSign2.setText(_translate("cellPowerManagerWindow", "-140", None))
        self.lineEditTimeSign2.setText(_translate("cellPowerManagerWindow", "0", None))
        self.labelTimeSign2Unit.setText(_translate("cellPowerManagerWindow", "[s]", None))
        self.labelStepSign2Unit.setText(_translate("cellPowerManagerWindow", " [dBm]", None))
        self.labelBeginSign2.setText(_translate("cellPowerManagerWindow", "Begin [dBm]", None))
        self.labelEndSign2.setText(_translate("cellPowerManagerWindow", "End [dBm]", None))
        self.comboBoxSign2.setItemText(0, _translate("cellPowerManagerWindow", "LTE", None))
        self.comboBoxSign2.setItemText(1, _translate("cellPowerManagerWindow", "WCDMA", None))
        self.comboBoxSign2.setItemText(2, _translate("cellPowerManagerWindow", "GSM", None))
        self.labelTimeSign2Name.setText(_translate("cellPowerManagerWindow", "Step \n"
"delay:", None))
        self.groupBoxSignSynch.setTitle(_translate("cellPowerManagerWindow", "Signaling 1 and 2 synchronously", None))
        self.labelStepSignSynchName.setText(_translate("cellPowerManagerWindow", "Step:", None))
        self.lineEditMaxSignSynch1.setText(_translate("cellPowerManagerWindow", "-45", None))
        self.lineEditStepSignSynch.setText(_translate("cellPowerManagerWindow", "0", None))
        self.lineEditMinSignSynch1.setText(_translate("cellPowerManagerWindow", "-140", None))
        self.lineEditTimeSignSynch.setText(_translate("cellPowerManagerWindow", "0", None))
        self.labelTimeSignSynchUnit.setText(_translate("cellPowerManagerWindow", "[s]", None))
        self.labelStepSignSynchUnit.setText(_translate("cellPowerManagerWindow", " [dBm]", None))
        self.labelBeginSignSynch1.setText(_translate("cellPowerManagerWindow", "Begin [dBm]", None))
        self.labelEndSignSynch1.setText(_translate("cellPowerManagerWindow", "End [dBm]", None))
        self.comboBoxSignSynch1.setItemText(0, _translate("cellPowerManagerWindow", "LTE", None))
        self.comboBoxSignSynch1.setItemText(1, _translate("cellPowerManagerWindow", "WCDMA", None))
        self.comboBoxSignSynch1.setItemText(2, _translate("cellPowerManagerWindow", "GSM", None))
        self.lineEditMinSignSynch2.setText(_translate("cellPowerManagerWindow", "-45", None))
        self.lineEditMaxSignSynch2.setText(_translate("cellPowerManagerWindow", "-140", None))
        self.labelBeginSignSynch2.setText(_translate("cellPowerManagerWindow", "Begin [dBm]", None))
        self.labelEndSignSynch2.setText(_translate("cellPowerManagerWindow", "End [dBm]", None))
        self.labelSliderSignSynch1Name.setText(_translate("cellPowerManagerWindow", "Signaling 1", None))
        self.labelSliderSignSynch2Name.setText(_translate("cellPowerManagerWindow", "Signaling 2", None))
        self.labelTimeSignSynchName.setText(_translate("cellPowerManagerWindow", "Step \n"
"delay:", None))
        self.comboBoxSignSynch2.setItemText(0, _translate("cellPowerManagerWindow", "LTE", None))
        self.comboBoxSignSynch2.setItemText(1, _translate("cellPowerManagerWindow", "WCDMA", None))
        self.comboBoxSignSynch2.setItemText(2, _translate("cellPowerManagerWindow", "GSM", None))
        self.pushButtonSave.setText(_translate("cellPowerManagerWindow", "Save", None))
        self.labelTestDuration.setText(_translate("cellPowerManagerWindow", "Test duration:", None))
        self.dateTimeEditTestEnd.setDisplayFormat(_translate("cellPowerManagerWindow", "HH:mm:ss dd-MM-yyyy", None))
        self.labelTestEnd.setText(_translate("cellPowerManagerWindow", "Test will end at:", None))
        self.labelLoopDelayUnit.setText(_translate("cellPowerManagerWindow", "[s]", None))
        self.labelLoop.setText(_translate("cellPowerManagerWindow", "Loop:", None))
        self.lineEditLoopDelay.setText(_translate("cellPowerManagerWindow", "1", None))
        self.lineEditLoop.setText(_translate("cellPowerManagerWindow", "1", None))
        self.labelLoopDelay.setText(_translate("cellPowerManagerWindow", "Loop delay:", None))
        self.pushButtonClose.setText(_translate("cellPowerManagerWindow", "Close", None))
        self.lineEditTestDuration.setText(_translate("cellPowerManagerWindow", "00:00:00", None))
