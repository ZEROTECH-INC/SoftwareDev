# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(305, 556)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"STYLE-SHEET-SOURCE-CODE_\n"
"/*EERO TECHNOLOGIES INC. /////////// */\n"
"/*SOFTWARE-DEVELOPMENT_ /////////// */\n"
"\n"
"* {\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #fff;\n"
"}\n"
"QMainWindow {\n"
"	background: tranparent;\n"
"	color: #ffeaea;\n"
"}\n"
"#centralwidget {	\n"
"	background-position: center;\n"
"	background: #131313;\n"
"	border-radius: 10px;\n"
"	padding: 25px;\n"
"	color: #ffeaea;\n"
"}\n"
"#widget_6 QPushButton, #widget_5 QPushButton, #widget_4 QPushButton {\n"
"	background: #131313;\n"
"	padding: 15px;\n"
"	border-radius: 10px;\n"
"	color: #ffeaea;\n"
"}\n"
"#widget_6 QPushButton:hover , #widget_5 QPushButton:hover {\n"
"	background-color: rgb(31, 24, 24);\n"
"	color: #ffeaea;\n"
"}\n"
"#widget_6 QPushButton:pressed, #widget_5 QPushButton:pressed {\n"
"	background-color: rgb(45, 0, 0);\n"
"	color: #ffeaea;\n"
"}\n"
"#widget_4 QPushButton:hover {\n"
"	background-color: rgb(31, 24, 24);\n"
"	color: #ffeaea;\n"
"}\n"
"#widget_4 QPushBut"
                        "ton:pressed {\n"
"	background-color: rgb(45, 0, 0);\n"
"	color: #ffeaea;\n"
"}\n"
"#widget QWidget {\n"
"	color: #ffeaea;\n"
"}\n"
"#mainHeadline {\n"
"	background: #131313;\n"
"	border-radius: 5px;\n"
"}\n"
"#mainHeadline #headlineButton {\n"
"	background: none;\n"
"	border: none;\n"
"	padding: 5px;\n"
"}\n"
"QWidget #notepadMain QPushButton {\n"
"	background: #131313;\n"
"	padding: 15px;\n"
"	border-radius: 10px;\n"
"	color: #ffeaea;\n"
"}\n"
"QWidget #notepadMain QPushButton:hover {\n"
"	background-color: rgb(31, 24, 24);\n"
"	color: #ffeaea;\n"
"}\n"
"QWidget #notepadMain QPushButton:pressed {\n"
"	background-color: rgb(45, 0, 0);\n"
"	color: #ffeaea;\n"
"}\n"
"QWidget #functions QPushButton {\n"
"	padding: 5px;\n"
"	color: #ffeaea;\n"
"	border-radius: 4px;\n"
"	background-color: rgb(72, 72, 72);\n"
"}\n"
"QWidget #functions QPushButton:hover {\n"
"	color: #ffeaea;\n"
"	background-color: rgb(83, 83, 83);\n"
"}\n"
"QWidget #functions QPushButton:pressed {\n"
"	color: #ffeaea;\n"
"	background-color: rgb(67, "
                        "67, 67);\n"
"}\n"
"QWidget #mainHeadline_2 QPushButton {\n"
"	background: none;\n"
"	color: #ffeaea;\n"
"	border: none;\n"
"	padding: 5px;\n"
"}\n"
"QWidget #mainHeadline {\n"
"	background: none;\n"
"	border: none;\n"
"	padding: 5px;\n"
"}\n"
"#calculatorOut QWidget {\n"
"	color: #ffeaea;\n"
"}\n"
"QLineEdit{\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgb(83, 83, 83);\n"
"	padding: 3px;\n"
"	padding-right: 20px;\n"
"	background-color: transparent;\n"
"	color: #ffeaea;\n"
"}\n"
"QComboBox {\n"
"	padding: 2px;\n"
"	padding-left: 7px;\n"
"	color: #ffeaea;\n"
"	background: #131313;\n"
"	border: none;\n"
"}\n"
"#pushButton_15:hover, #pushButton_16:hover {\n"
"	background-color: rgb(83, 83, 83);\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"	border: none;\n"
"}\n"
"#menubar {\n"
"	background: #131313;\n"
"	border-radius: 10px;\n"
"	color: #ffeaea;\n"
"	padding: 5px;\n"
"}\n"
"#menubar QPushButton {\n"
"	border: 2px solid transparent ;\n"
"}\n"
"QMainWindow #windowTitle_2 {\n"
"	color: #ffeaea;\n"
"}")
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.menubar = QFrame(self.centralwidget)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setFrameShape(QFrame.StyledPanel)
        self.menubar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.menubar)
        self.horizontalLayout_10.setSpacing(2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(2, 2, 2, 2)
        self.windowTitle = QWidget(self.menubar)
        self.windowTitle.setObjectName(u"windowTitle")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.windowTitle.setFont(font)
        self.horizontalLayout_13 = QHBoxLayout(self.windowTitle)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.windowTitle_2 = QLabel(self.windowTitle)
        self.windowTitle_2.setObjectName(u"windowTitle_2")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        self.windowTitle_2.setFont(font1)

        self.horizontalLayout_13.addWidget(self.windowTitle_2, 0, Qt.AlignLeft)


        self.horizontalLayout_10.addWidget(self.windowTitle, 0, Qt.AlignLeft|Qt.AlignTop)

        self.widget_2 = QWidget(self.menubar)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.menuFrame = QWidget(self.widget_2)
        self.menuFrame.setObjectName(u"menuFrame")
        self.horizontalLayout_11 = QHBoxLayout(self.menuFrame)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.userButton = QPushButton(self.menuFrame)
        self.userButton.setObjectName(u"userButton")
        self.userButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"../thebride/images/icons/main-user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.userButton.setIcon(icon)

        self.horizontalLayout_11.addWidget(self.userButton)

        self.minimize = QPushButton(self.menuFrame)
        self.minimize.setObjectName(u"minimize")
        self.minimize.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"../thebride/images/icons/zoom-out-half.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize.setIcon(icon1)

        self.horizontalLayout_11.addWidget(self.minimize)

        self.closeButton = QPushButton(self.menuFrame)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"../thebride/images/icons/close-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon2)

        self.horizontalLayout_11.addWidget(self.closeButton)


        self.horizontalLayout_12.addWidget(self.menuFrame, 0, Qt.AlignRight)


        self.horizontalLayout_10.addWidget(self.widget_2, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.menubar, 0, Qt.AlignTop)

        self.background = QStackedWidget(self.centralwidget)
        self.background.setObjectName(u"background")
        self.background.setStyleSheet(u"")
        self.background.setFrameShape(QFrame.NoFrame)
        self.background.setFrameShadow(QFrame.Raised)
        self.currencyPage = QWidget()
        self.currencyPage.setObjectName(u"currencyPage")
        self.verticalLayout_2 = QVBoxLayout(self.currencyPage)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 5, 10)
        self.widget = QWidget(self.currencyPage)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 1)
        self.mainHeadline = QWidget(self.widget)
        self.mainHeadline.setObjectName(u"mainHeadline")
        self.horizontalLayout_2 = QHBoxLayout(self.mainHeadline)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.headlineButton = QPushButton(self.mainHeadline)
        self.headlineButton.setObjectName(u"headlineButton")
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(False)
        self.headlineButton.setFont(font2)
        icon3 = QIcon()
        icon3.addFile(u"../../../../Adobe-AI_Files/Png_Icons_/Eero-Tech-Inc-PNG-Art-Files_/4x/Asset 1@4x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.headlineButton.setIcon(icon3)
        self.headlineButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.headlineButton, 0, Qt.AlignLeft)


        self.verticalLayout_3.addWidget(self.mainHeadline, 0, Qt.AlignTop)

        self.output_1 = QWidget(self.widget)
        self.output_1.setObjectName(u"output_1")
        self.horizontalLayout_5 = QHBoxLayout(self.output_1)
        self.horizontalLayout_5.setSpacing(15)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 5, 0, 10)
        self.comboBox = QComboBox(self.output_1)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_5.addWidget(self.comboBox)


        self.verticalLayout_3.addWidget(self.output_1, 0, Qt.AlignLeft)

        self.currency_1 = QWidget(self.widget)
        self.currency_1.setObjectName(u"currency_1")
        font3 = QFont()
        font3.setPointSize(20)
        font3.setBold(True)
        self.currency_1.setFont(font3)
        self.horizontalLayout_3 = QHBoxLayout(self.currency_1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 0, 0, 0)
        self.lineEdit_2 = QLineEdit(self.currency_1)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_3.addWidget(self.lineEdit_2)


        self.verticalLayout_3.addWidget(self.currency_1, 0, Qt.AlignLeft)

        self.ouput_2 = QWidget(self.widget)
        self.ouput_2.setObjectName(u"ouput_2")
        self.horizontalLayout_6 = QHBoxLayout(self.ouput_2)
        self.horizontalLayout_6.setSpacing(15)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 10, 0, 10)
        self.comboBox_2 = QComboBox(self.ouput_2)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_6.addWidget(self.comboBox_2)


        self.verticalLayout_3.addWidget(self.ouput_2, 0, Qt.AlignLeft)

        self.currency_2 = QWidget(self.widget)
        self.currency_2.setObjectName(u"currency_2")
        self.horizontalLayout_4 = QHBoxLayout(self.currency_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 0, 0, 0)
        self.lineEdit_3 = QLineEdit(self.currency_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setDragEnabled(True)

        self.horizontalLayout_4.addWidget(self.lineEdit_3)


        self.verticalLayout_3.addWidget(self.currency_2, 0, Qt.AlignLeft)

        self.outputInfo = QWidget(self.widget)
        self.outputInfo.setObjectName(u"outputInfo")
        self.horizontalLayout_8 = QHBoxLayout(self.outputInfo)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label = QLabel(self.outputInfo)
        self.label.setObjectName(u"label")

        self.horizontalLayout_8.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.outputInfo)


        self.verticalLayout_2.addWidget(self.widget, 0, Qt.AlignTop)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(5, 0, 5, 0)
        self.widget_3 = QWidget(self.currencyPage)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_6 = QVBoxLayout(self.widget_4)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.emptyBtn = QPushButton(self.widget_4)
        self.emptyBtn.setObjectName(u"emptyBtn")
        self.emptyBtn.setStyleSheet(u"#emptyBtn:hover {\n"
"	background: none;\n"
"}")

        self.verticalLayout_6.addWidget(self.emptyBtn)

        self.bttn_7 = QPushButton(self.widget_4)
        self.bttn_7.setObjectName(u"bttn_7")
        self.bttn_7.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.bttn_7)

        self.bttn_4 = QPushButton(self.widget_4)
        self.bttn_4.setObjectName(u"bttn_4")
        self.bttn_4.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.bttn_4)

        self.bttn_1 = QPushButton(self.widget_4)
        self.bttn_1.setObjectName(u"bttn_1")
        self.bttn_1.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.bttn_1)

        self.emptyBtn_1 = QPushButton(self.widget_4)
        self.emptyBtn_1.setObjectName(u"emptyBtn_1")
        self.emptyBtn_1.setStyleSheet(u"#emptyBtn_1:hover {\n"
"	background: none;\n"
"}")

        self.verticalLayout_6.addWidget(self.emptyBtn_1)


        self.horizontalLayout.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_4 = QVBoxLayout(self.widget_5)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(1, 0, 0, 0)
        self.resetBtn = QPushButton(self.widget_5)
        self.resetBtn.setObjectName(u"resetBtn")
        self.resetBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.resetBtn)

        self.bttn_8 = QPushButton(self.widget_5)
        self.bttn_8.setObjectName(u"bttn_8")
        self.bttn_8.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.bttn_8)

        self.bttn_5 = QPushButton(self.widget_5)
        self.bttn_5.setObjectName(u"bttn_5")
        self.bttn_5.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.bttn_5)

        self.bttn_2 = QPushButton(self.widget_5)
        self.bttn_2.setObjectName(u"bttn_2")
        self.bttn_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.bttn_2)

        self.bttn_0 = QPushButton(self.widget_5)
        self.bttn_0.setObjectName(u"bttn_0")
        self.bttn_0.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.bttn_0)


        self.horizontalLayout.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.widget_3)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_5 = QVBoxLayout(self.widget_6)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(1, 0, 0, 0)
        self.deleteBtn = QPushButton(self.widget_6)
        self.deleteBtn.setObjectName(u"deleteBtn")
        self.deleteBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.deleteBtn)

        self.bttn_9 = QPushButton(self.widget_6)
        self.bttn_9.setObjectName(u"bttn_9")
        self.bttn_9.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.bttn_9)

        self.bttn_6 = QPushButton(self.widget_6)
        self.bttn_6.setObjectName(u"bttn_6")
        self.bttn_6.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.bttn_6)

        self.bttn_3 = QPushButton(self.widget_6)
        self.bttn_3.setObjectName(u"bttn_3")
        self.bttn_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.bttn_3)

        self.decimalBtn = QPushButton(self.widget_6)
        self.decimalBtn.setObjectName(u"decimalBtn")
        self.decimalBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.decimalBtn)


        self.horizontalLayout.addWidget(self.widget_6)


        self.gridLayout.addWidget(self.widget_3, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.background.addWidget(self.currencyPage)
        self.calculatorPage = QWidget()
        self.calculatorPage.setObjectName(u"calculatorPage")
        self.verticalLayout_7 = QVBoxLayout(self.calculatorPage)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 0, 5, 10)
        self.widget_7 = QWidget(self.calculatorPage)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_15 = QVBoxLayout(self.widget_7)
        self.verticalLayout_15.setSpacing(10)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(5, 0, 5, 1)
        self.secondHeadline = QWidget(self.widget_7)
        self.secondHeadline.setObjectName(u"secondHeadline")
        self.verticalLayout_12 = QVBoxLayout(self.secondHeadline)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.mainHeadline_2 = QWidget(self.secondHeadline)
        self.mainHeadline_2.setObjectName(u"mainHeadline_2")
        self.horizontalLayout_9 = QHBoxLayout(self.mainHeadline_2)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(5, 0, 0, 0)
        self.headlineButton_2 = QPushButton(self.mainHeadline_2)
        self.headlineButton_2.setObjectName(u"headlineButton_2")
        self.headlineButton_2.setFont(font2)
        self.headlineButton_2.setIcon(icon3)
        self.headlineButton_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_9.addWidget(self.headlineButton_2, 0, Qt.AlignLeft)


        self.verticalLayout_12.addWidget(self.mainHeadline_2, 0, Qt.AlignTop)


        self.verticalLayout_15.addWidget(self.secondHeadline, 0, Qt.AlignTop)

        self.lineEdit = QLineEdit(self.widget_7)
        self.lineEdit.setObjectName(u"lineEdit")
        font4 = QFont()
        font4.setPointSize(40)
        self.lineEdit.setFont(font4)
        self.lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_15.addWidget(self.lineEdit, 0, Qt.AlignTop)

        self.functions = QWidget(self.widget_7)
        self.functions.setObjectName(u"functions")
        self.verticalLayout_13 = QVBoxLayout(self.functions)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 5, 0, 2)
        self.funtionButton = QFrame(self.functions)
        self.funtionButton.setObjectName(u"funtionButton")
        self.funtionButton.setFrameShape(QFrame.StyledPanel)
        self.funtionButton.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.funtionButton)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_33 = QPushButton(self.funtionButton)
        self.pushButton_33.setObjectName(u"pushButton_33")

        self.gridLayout_3.addWidget(self.pushButton_33, 0, 0, 1, 1)

        self.pushButton_34 = QPushButton(self.funtionButton)
        self.pushButton_34.setObjectName(u"pushButton_34")

        self.gridLayout_3.addWidget(self.pushButton_34, 0, 1, 1, 1)

        self.pushButton_35 = QPushButton(self.funtionButton)
        self.pushButton_35.setObjectName(u"pushButton_35")

        self.gridLayout_3.addWidget(self.pushButton_35, 0, 2, 1, 1)

        self.pushButton_38 = QPushButton(self.funtionButton)
        self.pushButton_38.setObjectName(u"pushButton_38")

        self.gridLayout_3.addWidget(self.pushButton_38, 0, 3, 1, 1)

        self.pushButton_37 = QPushButton(self.funtionButton)
        self.pushButton_37.setObjectName(u"pushButton_37")

        self.gridLayout_3.addWidget(self.pushButton_37, 0, 4, 1, 1)

        self.pushButton_36 = QPushButton(self.funtionButton)
        self.pushButton_36.setObjectName(u"pushButton_36")
        icon4 = QIcon()
        icon4.addFile(u"../../../../Adobe-AI_Files/Png_Icons_/Eero-Tech-Inc-PNG-Art-Files_/arrow-down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_36.setIcon(icon4)
        self.pushButton_36.setIconSize(QSize(10, 10))

        self.gridLayout_3.addWidget(self.pushButton_36, 0, 5, 1, 1)


        self.verticalLayout_13.addWidget(self.funtionButton, 0, Qt.AlignBottom)


        self.verticalLayout_15.addWidget(self.functions, 0, Qt.AlignBottom)


        self.verticalLayout_7.addWidget(self.widget_7)

        self.notepadMain = QWidget(self.calculatorPage)
        self.notepadMain.setObjectName(u"notepadMain")
        self.verticalLayout_11 = QVBoxLayout(self.notepadMain)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(5, 0, 5, 0)
        self.widget_9 = QWidget(self.notepadMain)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_10 = QWidget(self.widget_9)
        self.widget_10.setObjectName(u"widget_10")
        self.verticalLayout_8 = QVBoxLayout(self.widget_10)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.subract = QPushButton(self.widget_10)
        self.subract.setObjectName(u"subract")

        self.verticalLayout_8.addWidget(self.subract)

        self.btn_7 = QPushButton(self.widget_10)
        self.btn_7.setObjectName(u"btn_7")
        self.btn_7.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_8.addWidget(self.btn_7)

        self.btn_4 = QPushButton(self.widget_10)
        self.btn_4.setObjectName(u"btn_4")
        self.btn_4.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_8.addWidget(self.btn_4)

        self.btn_1 = QPushButton(self.widget_10)
        self.btn_1.setObjectName(u"btn_1")
        self.btn_1.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_8.addWidget(self.btn_1)

        self.addition = QPushButton(self.widget_10)
        self.addition.setObjectName(u"addition")

        self.verticalLayout_8.addWidget(self.addition)

        self.division = QPushButton(self.widget_10)
        self.division.setObjectName(u"division")

        self.verticalLayout_8.addWidget(self.division)


        self.horizontalLayout_7.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.widget_9)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout_9 = QVBoxLayout(self.widget_11)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(1, 0, 0, 0)
        self.reset = QPushButton(self.widget_11)
        self.reset.setObjectName(u"reset")
        self.reset.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_9.addWidget(self.reset)

        self.btn_8 = QPushButton(self.widget_11)
        self.btn_8.setObjectName(u"btn_8")
        self.btn_8.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_9.addWidget(self.btn_8)

        self.btn_5 = QPushButton(self.widget_11)
        self.btn_5.setObjectName(u"btn_5")
        self.btn_5.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_9.addWidget(self.btn_5)

        self.btn_2 = QPushButton(self.widget_11)
        self.btn_2.setObjectName(u"btn_2")
        self.btn_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_9.addWidget(self.btn_2)

        self.btn_0 = QPushButton(self.widget_11)
        self.btn_0.setObjectName(u"btn_0")
        self.btn_0.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_9.addWidget(self.btn_0)

        self.multiplication = QPushButton(self.widget_11)
        self.multiplication.setObjectName(u"multiplication")

        self.verticalLayout_9.addWidget(self.multiplication)


        self.horizontalLayout_7.addWidget(self.widget_11)

        self.widget_12 = QWidget(self.widget_9)
        self.widget_12.setObjectName(u"widget_12")
        self.verticalLayout_10 = QVBoxLayout(self.widget_12)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(1, 0, 0, 0)
        self.delete_2 = QPushButton(self.widget_12)
        self.delete_2.setObjectName(u"delete_2")
        self.delete_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_10.addWidget(self.delete_2)

        self.btn_9 = QPushButton(self.widget_12)
        self.btn_9.setObjectName(u"btn_9")
        self.btn_9.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_10.addWidget(self.btn_9)

        self.btn_6 = QPushButton(self.widget_12)
        self.btn_6.setObjectName(u"btn_6")
        self.btn_6.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_10.addWidget(self.btn_6)

        self.btn_3 = QPushButton(self.widget_12)
        self.btn_3.setObjectName(u"btn_3")
        self.btn_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_10.addWidget(self.btn_3)

        self.decimal = QPushButton(self.widget_12)
        self.decimal.setObjectName(u"decimal")
        self.decimal.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_10.addWidget(self.decimal)

        self.eqaual = QPushButton(self.widget_12)
        self.eqaual.setObjectName(u"eqaual")

        self.verticalLayout_10.addWidget(self.eqaual)


        self.horizontalLayout_7.addWidget(self.widget_12)


        self.gridLayout_2.addWidget(self.widget_9, 0, 0, 1, 1)


        self.verticalLayout_11.addLayout(self.gridLayout_2)


        self.verticalLayout_7.addWidget(self.notepadMain)

        self.background.addWidget(self.calculatorPage)

        self.verticalLayout.addWidget(self.background, 0, Qt.AlignVCenter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        self.background.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.windowTitle_2.setText(QCoreApplication.translate("MainWindow", u"Modern - Calculator UI", None))
        self.userButton.setText("")
        self.minimize.setText("")
        self.closeButton.setText("")
        self.headlineButton.setText(QCoreApplication.translate("MainWindow", u" Currency", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Canada - Dollar", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"China - Yuan", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Ghana - Cedi", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Korean - Won", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Nigerian - Naira", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"United Kingdom - Pound", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"United States - Dollar", None))

        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"$ 0", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Canada - Dollar", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"China - Yuan", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Ghana - Cedi", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Korean - Won", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"Nigerian - Naira", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"United Kingdom - Pound", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("MainWindow", u"United States - Dollar", None))

        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"$ 0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"1 GHS = 0.08403 USD\n"
"Updated 11/16/2023 6:08 AM\n"
"Offline. Please check your Network Settings", None))
        self.emptyBtn.setText("")
        self.bttn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.bttn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.bttn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.emptyBtn_1.setText("")
        self.resetBtn.setText(QCoreApplication.translate("MainWindow", u"CE", None))
        self.bttn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.bttn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.bttn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.bttn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.deleteBtn.setText(QCoreApplication.translate("MainWindow", u"DEL", None))
        self.bttn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.bttn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.bttn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.decimalBtn.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.headlineButton_2.setText(QCoreApplication.translate("MainWindow", u" Calculator", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"MC", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"MR", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"M+", None))
        self.pushButton_38.setText(QCoreApplication.translate("MainWindow", u"M-", None))
        self.pushButton_37.setText(QCoreApplication.translate("MainWindow", u"MS", None))
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u" M", None))
        self.subract.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.addition.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.division.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.reset.setText(QCoreApplication.translate("MainWindow", u"CE", None))
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.multiplication.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.delete_2.setText(QCoreApplication.translate("MainWindow", u"DEL", None))
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.decimal.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.eqaual.setText(QCoreApplication.translate("MainWindow", u"=", None))
    # retranslateUi

