# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(560, 585)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(560, 585))
        MainWindow.setMaximumSize(QtCore.QSize(560, 585))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Include/icons/65827280.n0mg1vxzk7.W665.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background:#f5f8fa;\n"
"}")
        MainWindow.setIconSize(QtCore.QSize(22, 24))
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.page_5)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 541, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.dateEdit = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("#dateEdit{\n"
"  display: inline-block;\n"
"  font-weight:400;\n"
"  font-size: 14px;\n"
"  color: rgb(0,0,0,0.8);\n"
"  text-shadow: 0 -1px rgb(46,53,58);\n"
"  text-decoration: none;\n"
"  padding: 4px 1em;\n"
"  margin:3px 2px 2px 2px;\n"
"  outline: none;\n"
"  border: 1px solid rgba(33,43,52,1);\n"
"  border-radius: 3px;\n"
"  background:rgba(45,57,69, 0);\n"
"}\n"
"\n"
"\n"
"#dateEdit:focus{\n"
" border: 2px solid rgba(45,57,69,1);\n"
"  border-radius: 3px;\n"
"}")
        self.dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_4.addWidget(self.dateEdit)
        self.start_upload_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.start_upload_button.setStyleSheet("#start_upload_button{\n"
"  display: inline-block;\n"
"  font-weight:400;\n"
"  font-size: 15px;\n"
"  color: rgb(255,255,255,0.9);\n"
"  text-shadow: 0 -1px rgb(46,53,58);\n"
"  text-decoration: none;\n"
"  user-select: none;\n"
"  line-height: 2em;\n"
"  padding: 5px 1.5em;\n"
"  margin:6px 15px 6px 15px;\n"
"  outline: none;\n"
"  border: 1px solid rgba(33,43,52,1);\n"
"  border-radius: 3px;\n"
"  background:rgba(45,57,69, 1);\n"
"}\n"
"#start_upload_button:hover {\n"
"background:rgba(25,37,49,1);\n"
"color:white;\n"
"}")
        self.start_upload_button.setObjectName("start_upload_button")
        self.horizontalLayout_4.addWidget(self.start_upload_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_2.sizePolicy().hasHeightForWidth())
        self.textBrowser_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("#textBrowser_2{\n"
"  display: inline-block;\n"
"  font-weight:400;\n"
"  color: rgb(0,0,0,0.95);\n"
"  text-shadow: 0 -1px rgb(46,53,58);\n"
"  text-decoration: none;\n"
"  user-select: none;\n"
"  line-height: 1em;\n"
"  padding: 1px 1em;\n"
"  margin:2px 2px;\n"
"  outline: none;\n"
"  border: 1px solid rgba(33,43,52,1);\n"
"  border-radius: 3px;\n"
"  background:rgba(255,255,255, 1);\n"
"}")
        self.textBrowser_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.textBrowser_2.setOpenExternalLinks(False)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout_4.addWidget(self.textBrowser_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.back_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.back_button.setStyleSheet("#back_button{\n"
"  display: inline-block;\n"
"  font-weight:400;\n"
"  font-size: 14px;\n"
"  color: rgb(0,0,0,0.8);\n"
"  text-shadow: 0 -1px rgb(46,53,58);\n"
"  text-decoration: none;\n"
"  user-select: none;\n"
"  line-height: 2em;\n"
"  padding: 5px 1em;\n"
"  margin:2px 2px;\n"
"  outline: none;\n"
"  border: 1px solid rgba(33,43,52,1);\n"
"  border-radius: 3px;\n"
"  background:rgba(45,57,69, 0);\n"
"}\n"
"#back_button:hover{\n"
" border: 2px solid rgba(45,57,69,1);\n"
"  border-radius: 3px;\n"
"}")
        self.back_button.setObjectName("back_button")
        self.horizontalLayout_5.addWidget(self.back_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_6.sizePolicy().hasHeightForWidth())
        self.page_6.setSizePolicy(sizePolicy)
        self.page_6.setMaximumSize(QtCore.QSize(550, 16777215))
        self.page_6.setObjectName("page_6")
        self.layoutWidget = QtWidgets.QWidget(self.page_6)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 543, 573))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("#label{\n"
"margin-bottom: 5px;\n"
"font-weight: 400;\n"
"}")
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_3.sizePolicy().hasHeightForWidth())
        self.checkBox_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(12)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setStyleSheet("QCheckBox::indicator {\n"
"     width: 18px;\n"
"     height: 18px;\n"
" }\n"
"QCheckBox::indicator:unchecked\n"
"  {\n"
"    image: url(C:/Users/Roman/PycharmProjects/Lab2/venv/Include/icons/checkno.png);\n"
"  }\n"
"QCheckBox::indicator:checked\n"
"  {\n"
"    image: url(C:/Users/Roman/PycharmProjects/Lab2/venv/Include/icons/web-20180101142045553930yes.png);\n"
"  }\n"
"QCheckBox{\n"
"margin: 2px;\n"
"font-weight: 100;\n"
"}")
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_2.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(12)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setStyleSheet("QCheckBox::indicator {\n"
"     width: 18px;\n"
"     height: 18px;\n"
" }\n"
"QCheckBox::indicator:unchecked\n"
"  {\n"
"    image: url(C:/Users/Roman/PycharmProjects/Lab2/venv/Include/icons/checkno.png);\n"
"  }\n"
"QCheckBox::indicator:checked\n"
"  {\n"
"    image: url(C:/Users/Roman/PycharmProjects/Lab2/venv/Include/icons/web-20180101142045553930yes.png);\n"
"  }\n"
"QCheckBox{\n"
"margin: 2px;\n"
"font-weight: 100;\n"
"}")
        self.checkBox_4.setChecked(True)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_2.addWidget(self.checkBox_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(12)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("QCheckBox::indicator {\n"
"     width: 18px;\n"
"     height: 18px;\n"
" }\n"
"QCheckBox::indicator:unchecked\n"
"  {\n"
"    image: url(C:/Users/Roman/PycharmProjects/Lab2/venv/Include/icons/checkno.png);\n"
"  }\n"
"QCheckBox::indicator:checked\n"
"  {\n"
"    image: url(C:/Users/Roman/PycharmProjects/Lab2/venv/Include/icons/web-20180101142045553930yes.png);\n"
"  }\n"
"QCheckBox{\n"
"margin: 2px;\n"
"font-weight: 100;\n"
"}")
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_3.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(12)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setStyleSheet("QCheckBox::indicator {\n"
"     width: 18px;\n"
"     height: 18px;\n"
" }\n"
"QCheckBox::indicator:unchecked\n"
"  {\n"
"    image: url(C:/Users/Roman/PycharmProjects/Lab2/venv/Include/icons/checkno.png);\n"
"  }\n"
"QCheckBox::indicator:checked\n"
"  {\n"
"    image: url(C:/Users/Roman/PycharmProjects/Lab2/venv/Include/icons/web-20180101142045553930yes.png);\n"
"  }\n"
"QCheckBox{\n"
"margin: 2px;\n"
"font-weight: 100;\n"
"}")
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_3.addWidget(self.checkBox_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setStyleSheet("")
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_5.addWidget(self.line)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy)
        self.calendarWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.calendarWidget.setMaximumSize(QtCore.QSize(1677724, 16777212))
        palette = QtGui.QPalette()
        self.calendarWidget.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setStyleSheet("\n"
"QTableView {\n"
"    selection-background-color: #28828a;\n"
"    selection-color:white;\n"
"}\n"
"\n"
"QCalendarWidget QWidget{\n"
"background-color:#28828a;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton{\n"
"background-color:#28828a;\n"
"color: white;\n"
"icon-size: 30px;\n"
"}\n"
"QCalendarWidget QToolButton:hover{\n"
"background:rgba(255,255,255, 0.1);\n"
"border: 1px solid rgba(255,255,255,0);\n"
"color: white;\n"
"}\n"
"\n"
"QCalendarWidget QMenu{\n"
"background-color:#28828a;\n"
"color: white;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled{\n"
"background-color: white;\n"
"\n"
"}\n"
"/*\n"
"QCalendarWidget QAbstractItemView:disabled{\n"
"background-color: yellow;\n"
"color: white;\n"
"}\n"
"*/\n"
"QCalendarWidget QMenu{\n"
"    background-color: #154347;\n"
"    font-weight:600;\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox{\n"
"  display: inline-block;\n"
"  font-weight:600;\n"
"  font-size: 13px;\n"
"  color: rgb(255,255,255,1);\n"
"  text-shadow: 0 -1px rgb(46,53,58);\n"
"  text-decoration: none;\n"
"  padding: 4px 4px;\n"
"  margin:0px;\n"
"  outline: none;\n"
"  border: 1px solid rgba(255,255,255,0);\n"
"  border-radius: 3px;\n"
"  background:rgba(255,255,255, 0.1);\n"
"}\n"
"\n"
"#qt_calendar_prevmonth {\n"
"    icon-size: 30px;\n"
"    qproperty-icon: url(C:/Users/Roman/PycharmProjects/Lab2/venv/Include/icons/left.png);\n"
"}\n"
"#qt_calendar_nextmonth {\n"
"    icon-size: 30px;\n"
"    qproperty-icon: url(C:/Users/Roman/PycharmProjects/Lab2/venv/Include/icons/right.png);\n"
"}")
        self.calendarWidget.setMinimumDate(QtCore.QDate(2019, 1, 1))
        self.calendarWidget.setMaximumDate(QtCore.QDate(9999, 12, 31))
        self.calendarWidget.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setSelectionMode(QtWidgets.QCalendarWidget.SingleSelection)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.ISOWeekNumbers)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout_5.addWidget(self.calendarWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.timeEdit = QtWidgets.QTimeEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeEdit.sizePolicy().hasHeightForWidth())
        self.timeEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.timeEdit.setFont(font)
        self.timeEdit.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.timeEdit.setStyleSheet("#timeEdit{\n"
"  display: inline-block;\n"
"  font-weight:400;\n"
"  font-size: 14px;\n"
"  color: rgb(0,0,0,0.8);\n"
"  text-shadow: 0 -1px rgb(46,53,58);\n"
"  text-decoration: none;\n"
"  padding: 4px 1em;\n"
"  margin:2px 2px 2px 2px;\n"
"  outline: none;\n"
"  border: 1px solid rgba(33,43,52,1);\n"
"  border-radius: 3px;\n"
"  background:rgba(45,57,69, 0);\n"
"}\n"
"\n"
"\n"
"#timeEdit:focus{\n"
" border: 2px solid rgba(45,57,69,1);\n"
"  border-radius: 3px;\n"
"}")
        self.timeEdit.setSpecialValueText("")
        self.timeEdit.setDate(QtCore.QDate(2000, 1, 1))
        self.timeEdit.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.timeEdit.setCalendarPopup(False)
        self.timeEdit.setTimeSpec(QtCore.Qt.LocalTime)
        self.timeEdit.setTime(QtCore.QTime(23, 59, 59))
        self.timeEdit.setObjectName("timeEdit")
        self.horizontalLayout.addWidget(self.timeEdit)
        self.date_time_button = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.date_time_button.setFont(font)
        self.date_time_button.setStyleSheet("#date_time_button{\n"
"  display: inline-block;\n"
"  font-weight:400;\n"
"  font-size: 14px;\n"
"  color: rgb(0,0,0,0.8);\n"
"  text-shadow: 0 -1px rgb(46,53,58);\n"
"  text-decoration: none;\n"
"  user-select: none;\n"
"  line-height: 2em;\n"
"  padding: 5px 1em;\n"
"  margin:2px 2px;\n"
"  outline: none;\n"
"  border: 1px solid rgba(33,43,52,1);\n"
"  border-radius: 3px;\n"
"  background:rgba(45,57,69, 0);\n"
"}\n"
"#date_time_button:hover{\n"
" border: 2px solid rgba(45,57,69,1);\n"
"  border-radius: 3px;\n"
"}")
        self.date_time_button.setObjectName("date_time_button")
        self.horizontalLayout.addWidget(self.date_time_button)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.textBrowser = QtWidgets.QTextBrowser(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("#textBrowser{\n"
"  display: inline-block;\n"
"  font-weight:400;\n"
"  color: rgb(0,0,0,0.95);\n"
"  text-shadow: 0 -1px rgb(46,53,58);\n"
"  text-decoration: none;\n"
"  user-select: none;\n"
"  line-height: 1em;\n"
"  padding: 1px 1em;\n"
"  margin:2px 2px;\n"
"  outline: none;\n"
"  border: 1px solid rgba(33,43,52,1);\n"
"  border-radius: 3px;\n"
"  background:rgba(255,255,255, 1);\n"
"}")
        self.textBrowser.setPlaceholderText("")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_5.addWidget(self.textBrowser)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.update_button = QtWidgets.QPushButton(self.layoutWidget)
        self.update_button.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.update_button.setStyleSheet("#update_button{\n"
"  display: inline-block;\n"
"  font-weight:400;\n"
"  font-size: 15px;\n"
"  color: rgb(255,255,255,0.9);\n"
"  text-shadow: 0 -1px rgb(46,53,58);\n"
"  text-decoration: none;\n"
"  user-select: none;\n"
"  line-height: 2em;\n"
"  padding: 5px 1.5em;\n"
"  margin:6px 2px 6px 2px;\n"
"  outline: none;\n"
"  border: 1px solid rgba(33,43,52,1);\n"
"  border-radius: 3px;\n"
"  background:rgba(45,57,69, 1);\n"
"}\n"
"#update_button:hover {\n"
"background:rgba(25,37,49,1);\n"
"color:white;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Include/icons/update.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.update_button.setIcon(icon1)
        self.update_button.setObjectName("update_button")
        self.horizontalLayout_2.addWidget(self.update_button)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.StartButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StartButton.sizePolicy().hasHeightForWidth())
        self.StartButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.StartButton.setFont(font)
        self.StartButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.StartButton.setAutoFillBackground(False)
        self.StartButton.setStyleSheet("#StartButton{\n"
"  display: inline-block;\n"
"  font-weight:400;\n"
"  font-size: 15px;\n"
"  color: rgb(255,255,255,0.9);\n"
"  text-shadow: 0 -1px rgb(46,53,58);\n"
"  text-decoration: none;\n"
"  user-select: none;\n"
"  line-height: 2em;\n"
"  padding: 5px 1.5em;\n"
"  margin:6px 15px 6px 15px;\n"
"  outline: none;\n"
"  border: 1px solid rgba(33,43,52,1);\n"
"  border-radius: 3px;\n"
"  background:rgba(45,57,69, 1);\n"
"}\n"
"#StartButton:hover {\n"
"background:rgba(25,37,49,1);\n"
"color:white;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Include/icons/361-3612051_contact-search-icon-png.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.StartButton.setIcon(icon2)
        self.StartButton.setObjectName("StartButton")
        self.horizontalLayout_2.addWidget(self.StartButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.stackedWidget.addWidget(self.page_6)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ClassroomFinder"))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "dd.MM"))
        self.start_upload_button.setText(_translate("MainWindow", "Начать обновление"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.back_button.setText(_translate("MainWindow", "Назад"))
        self.label.setText(_translate("MainWindow", "Параметры аудитории:"))
        self.checkBox_3.setText(_translate("MainWindow", "Оборудована проектором"))
        self.checkBox_4.setText(_translate("MainWindow", "Компьютерный класс"))
        self.checkBox.setText(_translate("MainWindow", "Лабаратория"))
        self.checkBox_2.setText(_translate("MainWindow", "Аудитория общего фонда"))
        self.timeEdit.setDisplayFormat(_translate("MainWindow", "H:mm"))
        self.date_time_button.setText(_translate("MainWindow", "Вернуть текущую дату и время"))
        self.update_button.setText(_translate("MainWindow", "Обновить данные"))
        self.StartButton.setText(_translate("MainWindow", "Поиск "))
