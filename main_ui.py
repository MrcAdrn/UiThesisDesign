
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1160, 840)
        font = QtGui.QFont()
        font.setPointSize(20)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.icons_details_widget = QtWidgets.QWidget(self.centralwidget)
        self.icons_details_widget.setMinimumSize(QtCore.QSize(130, 150))
        self.icons_details_widget.setMaximumSize(QtCore.QSize(150, 16777215))
        self.icons_details_widget.setStyleSheet(" background-color: #FEF6E4;\n"
"  \n"
"")
        self.icons_details_widget.setObjectName("icons_details_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.icons_details_widget)
        self.verticalLayout_3.setContentsMargins(5, -1, 5, 35)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.icon_Acc = QtWidgets.QLabel(self.icons_details_widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.icon_Acc.setFont(font)
        self.icon_Acc.setText("")
        self.icon_Acc.setPixmap(QtGui.QPixmap(":/icons/icon/logo.png"))
        self.icon_Acc.setAlignment(QtCore.Qt.AlignCenter)
        self.icon_Acc.setObjectName("icon_Acc")
        self.verticalLayout_3.addWidget(self.icon_Acc)
        self.dashboardbutton = QtWidgets.QPushButton(self.icons_details_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dashboardbutton.sizePolicy().hasHeightForWidth())
        self.dashboardbutton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.dashboardbutton.setFont(font)
        self.dashboardbutton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.dashboardbutton.setStyleSheet("QPushButton:hover {\n"
"    background-color: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #FEF6E4, stop: 1 #ADD8E6);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(254, 246, 228);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
" \n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icon/dashboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dashboardbutton.setIcon(icon)
        self.dashboardbutton.setCheckable(True)
        self.dashboardbutton.setAutoRepeat(False)
        self.dashboardbutton.setAutoExclusive(True)
        self.dashboardbutton.setObjectName("dashboardbutton")
        self.verticalLayout_3.addWidget(self.dashboardbutton)
        self.peoplebutton = QtWidgets.QPushButton(self.icons_details_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.peoplebutton.sizePolicy().hasHeightForWidth())
        self.peoplebutton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.peoplebutton.setFont(font)
        self.peoplebutton.setStyleSheet("QPushButton:hover {\n"
"    background-color: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #FEF6E4, stop: 1 #ADD8E6);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(254, 246, 228);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
" \n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icon/people.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.peoplebutton.setIcon(icon1)
        self.peoplebutton.setCheckable(True)
        self.peoplebutton.setAutoExclusive(True)
        self.peoplebutton.setObjectName("peoplebutton")
        self.verticalLayout_3.addWidget(self.peoplebutton)
        self.acbutton = QtWidgets.QPushButton(self.icons_details_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.acbutton.sizePolicy().hasHeightForWidth())
        self.acbutton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.acbutton.setFont(font)
        self.acbutton.setStyleSheet("QPushButton:hover {\n"
"    background-color: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #FEF6E4, stop: 1 #ADD8E6);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(254, 246, 228);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
" \n"
"}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icon/Ac.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.acbutton.setIcon(icon2)
        self.acbutton.setCheckable(True)
        self.acbutton.setAutoExclusive(True)
        self.acbutton.setObjectName("acbutton")
        self.verticalLayout_3.addWidget(self.acbutton)
        self.electricfanbutton = QtWidgets.QPushButton(self.icons_details_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.electricfanbutton.sizePolicy().hasHeightForWidth())
        self.electricfanbutton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.electricfanbutton.setFont(font)
        self.electricfanbutton.setStyleSheet("QPushButton:hover {\n"
"    background-color: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #FEF6E4, stop: 1 #ADD8E6);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(254, 246, 228);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
" \n"
"}\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icon/icons8-fan-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.electricfanbutton.setIcon(icon3)
        self.electricfanbutton.setCheckable(True)
        self.electricfanbutton.setAutoExclusive(True)
        self.electricfanbutton.setObjectName("electricfanbutton")
        self.verticalLayout_3.addWidget(self.electricfanbutton)
        self.lightsbutton = QtWidgets.QPushButton(self.icons_details_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lightsbutton.sizePolicy().hasHeightForWidth())
        self.lightsbutton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lightsbutton.setFont(font)
        self.lightsbutton.setStyleSheet("QPushButton:hover {\n"
"    background-color: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #FEF6E4, stop: 1 #ADD8E6);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(254, 246, 228);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
" \n"
"}\n"
"")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icon/light.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lightsbutton.setIcon(icon4)
        self.lightsbutton.setCheckable(True)
        self.lightsbutton.setAutoExclusive(True)
        self.lightsbutton.setObjectName("lightsbutton")
        self.verticalLayout_3.addWidget(self.lightsbutton)
        self.doorbutton = QtWidgets.QPushButton(self.icons_details_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doorbutton.sizePolicy().hasHeightForWidth())
        self.doorbutton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.doorbutton.setFont(font)
        self.doorbutton.setStyleSheet("QPushButton:hover {\n"
"    background-color: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #FEF6E4, stop: 1 #ADD8E6);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(254, 246, 228);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
" \n"
"}\n"
"")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icon/icons8-door-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.doorbutton.setIcon(icon5)
        self.doorbutton.setCheckable(True)
        self.doorbutton.setAutoExclusive(True)
        self.doorbutton.setObjectName("doorbutton")
        self.verticalLayout_3.addWidget(self.doorbutton)
        self.powerconsumptionbutton = QtWidgets.QPushButton(self.icons_details_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.powerconsumptionbutton.sizePolicy().hasHeightForWidth())
        self.powerconsumptionbutton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.powerconsumptionbutton.setFont(font)
        self.powerconsumptionbutton.setStyleSheet("QPushButton:hover {\n"
"    background-color: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #FEF6E4, stop: 1 #ADD8E6);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(254, 246, 228);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
" \n"
"}\n"
"")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icon/Pc.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.powerconsumptionbutton.setIcon(icon6)
        self.powerconsumptionbutton.setCheckable(True)
        self.powerconsumptionbutton.setAutoExclusive(True)
        self.powerconsumptionbutton.setObjectName("powerconsumptionbutton")
        self.verticalLayout_3.addWidget(self.powerconsumptionbutton)
        spacerItem = QtWidgets.QSpacerItem(1, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.infobutton = QtWidgets.QPushButton(self.icons_details_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infobutton.sizePolicy().hasHeightForWidth())
        self.infobutton.setSizePolicy(sizePolicy)
        self.infobutton.setMinimumSize(QtCore.QSize(0, 0))
        self.infobutton.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.infobutton.setFont(font)
        self.infobutton.setStyleSheet("QPushButton:hover {\n"
"    background-color: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #FEF6E4, stop: 1 #ADD8E6);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(254, 246, 228);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
" \n"
"}\n"
"")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icon/icons8-about-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.infobutton.setIcon(icon7)
        self.infobutton.setCheckable(True)
        self.infobutton.setAutoExclusive(True)
        self.infobutton.setObjectName("infobutton")
        self.verticalLayout_3.addWidget(self.infobutton)
        self.exitbutton = QtWidgets.QPushButton(self.icons_details_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitbutton.sizePolicy().hasHeightForWidth())
        self.exitbutton.setSizePolicy(sizePolicy)
        self.exitbutton.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.exitbutton.setFont(font)
        self.exitbutton.setStyleSheet("QPushButton:hover {\n"
"    background-color: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #FEF6E4, stop: 1 #ADD8E6);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(254, 246, 228);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
" \n"
"}\n"
"")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/icon/icons8-exit-35.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitbutton.setIcon(icon8)
        self.exitbutton.setCheckable(True)
        self.exitbutton.setAutoExclusive(True)
        self.exitbutton.setObjectName("exitbutton")
        self.verticalLayout_3.addWidget(self.exitbutton)
        self.gridLayout.addWidget(self.icons_details_widget, 0, 1, 1, 1)
        self.icon_only_widget = QtWidgets.QWidget(self.centralwidget)
        self.icon_only_widget.setMinimumSize(QtCore.QSize(65, 0))
        self.icon_only_widget.setMaximumSize(QtCore.QSize(65, 16777215))
        self.icon_only_widget.setStyleSheet(" background-color: #FEF6E4;\n"
"  \n"
"")
        self.icon_only_widget.setObjectName("icon_only_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.icon_only_widget)
        self.verticalLayout.setContentsMargins(10, 20, 10, 50)
        self.verticalLayout.setSpacing(40)
        self.verticalLayout.setObjectName("verticalLayout")
        self.icon_only_Acc = QtWidgets.QLabel(self.icon_only_widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.icon_only_Acc.setFont(font)
        self.icon_only_Acc.setObjectName("icon_only_Acc")
        self.verticalLayout.addWidget(self.icon_only_Acc)
        self.dashboardbutton_2 = QtWidgets.QPushButton(self.icon_only_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dashboardbutton_2.sizePolicy().hasHeightForWidth())
        self.dashboardbutton_2.setSizePolicy(sizePolicy)
        self.dashboardbutton_2.setStyleSheet("QPushButton:hover {\n"
"    background-color: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #FEF6E4, stop: 1 #ADD8E6);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(254, 246, 228);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
" \n"
"}\n"
"")
        self.dashboardbutton_2.setText("")
        self.dashboardbutton_2.setIcon(icon)
        self.dashboardbutton_2.setCheckable(True)
        self.dashboardbutton_2.setAutoExclusive(True)
        self.dashboardbutton_2.setObjectName("dashboardbutton_2")
        self.verticalLayout.addWidget(self.dashboardbutton_2)
        self.peoplebutton_2 = QtWidgets.QPushButton(self.icon_only_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.peoplebutton_2.sizePolicy().hasHeightForWidth())
        self.peoplebutton_2.setSizePolicy(sizePolicy)
        self.peoplebutton_2.setStyleSheet("QPushButton:hover {\n"
"    background-color: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #FEF6E4, stop: 1 #ADD8E6);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(254, 246, 228);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
" \n"
"}\n"
"")
        self.peoplebutton_2.setText("")
        self.peoplebutton_2.setIcon(icon1)
        self.peoplebutton_2.setCheckable(True)
        self.peoplebutton_2.setAutoExclusive(True)
        self.peoplebutton_2.setObjectName("peoplebutton_2")
        self.verticalLayout.addWidget(self.peoplebutton_2)
        self.acbutton_2 = QtWidgets.QPushButton(self.icon_only_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.acbutton_2.sizePolicy().hasHeightForWidth())
        self.acbutton_2.setSizePolicy(sizePolicy)
        self.acbutton_2.setStyleSheet("QPushButton:hover {\n"
"    background-color: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #FEF6E4, stop: 1 #ADD8E6);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(254, 246, 228);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
" \n"
"}\n"
"")
        self.acbutton_2.setText("")
        self.acbutton_2.setIcon(icon2)
        self.acbutton_2.setCheckable(True)
        self.acbutton_2.setAutoExclusive(True)
        self.acbutton_2.setObjectName("acbutton_2")
        self.verticalLayout.addWidget(self.acbutton_2)
        self.eclectricfanbutton = QtWidgets.QPushButton(self.icon_only_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eclectricfanbutton.sizePolicy().hasHeightForWidth())
        self.eclectricfanbutton.setSizePolicy(sizePolicy)
        self.eclectricfanbutton.setStyleSheet("QPushButton:hover {\n"
"    background-color: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #FEF6E4, stop: 1 #ADD8E6);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(254, 246, 228);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
" \n"
"}\n"
"")
        self.eclectricfanbutton.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/icon/electricfan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.eclectricfanbutton.setIcon(icon9)
        self.eclectricfanbutton.setCheckable(True)
        self.eclectricfanbutton.setAutoExclusive(True)
        self.eclectricfanbutton.setObjectName("eclectricfanbutton")
        self.verticalLayout.addWidget(self.eclectricfanbutton)
        self.lightsbutton_2 = QtWidgets.QPushButton(self.icon_only_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lightsbutton_2.sizePolicy().hasHeightForWidth())
        self.lightsbutton_2.setSizePolicy(sizePolicy)
        self.lightsbutton_2.setStyleSheet("QPushButton:hover {\n"
"    background-color: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #FEF6E4, stop: 1 #ADD8E6);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(254, 246, 228);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
" \n"
"}\n"
"")
        self.lightsbutton_2.setText("")
        self.lightsbutton_2.setIcon(icon4)
        self.lightsbutton_2.setCheckable(True)
        self.lightsbutton_2.setAutoExclusive(True)
        self.lightsbutton_2.setObjectName("lightsbutton_2")
        self.verticalLayout.addWidget(self.lightsbutton_2)
        self.doorbutton_2 = QtWidgets.QPushButton(self.icon_only_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doorbutton_2.sizePolicy().hasHeightForWidth())
        self.doorbutton_2.setSizePolicy(sizePolicy)
        self.doorbutton_2.setStyleSheet("QPushButton:hover {\n"
"    background-color: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #FEF6E4, stop: 1 #ADD8E6);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(254, 246, 228);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
" \n"
"}\n"
"")
        self.doorbutton_2.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/icon/door.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.doorbutton_2.setIcon(icon10)
        self.doorbutton_2.setCheckable(True)
        self.doorbutton_2.setAutoExclusive(True)
        self.doorbutton_2.setObjectName("doorbutton_2")
        self.verticalLayout.addWidget(self.doorbutton_2)
        self.powerconsumptionbutton_2 = QtWidgets.QPushButton(self.icon_only_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.powerconsumptionbutton_2.sizePolicy().hasHeightForWidth())
        self.powerconsumptionbutton_2.setSizePolicy(sizePolicy)
        self.powerconsumptionbutton_2.setStyleSheet("QPushButton:hover {\n"
"    background-color: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #FEF6E4, stop: 1 #ADD8E6);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(254, 246, 228);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
" \n"
"}\n"
"")
        self.powerconsumptionbutton_2.setText("")
        self.powerconsumptionbutton_2.setIcon(icon6)
        self.powerconsumptionbutton_2.setCheckable(True)
        self.powerconsumptionbutton_2.setAutoExclusive(True)
        self.powerconsumptionbutton_2.setObjectName("powerconsumptionbutton_2")
        self.verticalLayout.addWidget(self.powerconsumptionbutton_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 26, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.infobutton_2 = QtWidgets.QPushButton(self.icon_only_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infobutton_2.sizePolicy().hasHeightForWidth())
        self.infobutton_2.setSizePolicy(sizePolicy)
        self.infobutton_2.setStyleSheet("QPushButton:hover {\n"
"    background-color: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #FEF6E4, stop: 1 #ADD8E6);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(254, 246, 228);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
" \n"
"}\n"
"")
        self.infobutton_2.setText("")
        self.infobutton_2.setIcon(icon7)
        self.infobutton_2.setCheckable(True)
        self.infobutton_2.setAutoExclusive(True)
        self.infobutton_2.setObjectName("infobutton_2")
        self.verticalLayout.addWidget(self.infobutton_2)
        self.exitbutton_2 = QtWidgets.QPushButton(self.icon_only_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitbutton_2.sizePolicy().hasHeightForWidth())
        self.exitbutton_2.setSizePolicy(sizePolicy)
        self.exitbutton_2.setStyleSheet("QPushButton:hover {\n"
"    background-color: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #FEF6E4, stop: 1 #ADD8E6);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(254, 246, 228);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
" \n"
"}\n"
"")
        self.exitbutton_2.setText("")
        self.exitbutton_2.setIcon(icon8)
        self.exitbutton_2.setCheckable(True)
        self.exitbutton_2.setAutoExclusive(True)
        self.exitbutton_2.setObjectName("exitbutton_2")
        self.verticalLayout.addWidget(self.exitbutton_2)
        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.topWidget = QtWidgets.QWidget(self.widget)
        self.topWidget.setStyleSheet("")
        self.topWidget.setObjectName("topWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.topWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_10 = QtWidgets.QPushButton(self.topWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        self.pushButton_10.setStyleSheet("QPushButton:hover {\n"
"    background-color: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #FEF6E4, stop: 1 #ADD8E6);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(254, 246, 228);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
" \n"
"}\n"
"")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/icon/backward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon11)
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setAutoExclusive(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout.addWidget(self.pushButton_10)
        spacerItem2 = QtWidgets.QSpacerItem(413, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.topWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem3 = QtWidgets.QSpacerItem(413, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.gridLayout_2.addWidget(self.topWidget, 0, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.stackedWidget.setStyleSheet("QWidget {\n"
"    background: qlineargradient(spread:pad, x2:1, y1:1, x1:1, y1:2, stop:0 #FEF6E4, stop:1 #ffffff);\n"
"    border: 1px solid black;\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.dasboardpage = QtWidgets.QWidget()
        self.dasboardpage.setObjectName("dasboardpage")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.dasboardpage)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lights = QtWidgets.QWidget(self.dasboardpage)
        self.lights.setMinimumSize(QtCore.QSize(240, 200))
        self.lights.setStyleSheet("background-color: transparent;\n"
"border: 1px solid #000000; \n"
"border-radius: 5px;\n"
"")
        self.lights.setObjectName("lights")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.lights)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_11 = QtWidgets.QLabel(self.lights)
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap(":/icons/icon/light.png"))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.lights)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.label_8 = QtWidgets.QLabel(self.lights)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(255, 110, 110);\n"
"")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.gridLayout_3.addWidget(self.lights, 3, 0, 1, 1)
        self.aircon = QtWidgets.QWidget(self.dasboardpage)
        self.aircon.setMinimumSize(QtCore.QSize(240, 200))
        self.aircon.setMaximumSize(QtCore.QSize(240, 200))
        self.aircon.setStyleSheet("background-color: transparent;\n"
"border: 1px solid #000000; \n"
"border-radius: 5px;\n"
"")
        self.aircon.setObjectName("aircon")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.aircon)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_13 = QtWidgets.QLabel(self.aircon)
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap(":/icons/icon/Ac.png"))
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_5.addWidget(self.label_13)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_12 = QtWidgets.QLabel(self.aircon)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_7.addWidget(self.label_12)
        self.label_9 = QtWidgets.QLabel(self.aircon)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgb(255, 110, 110);\n"
"")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_7.addWidget(self.label_9)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.gridLayout_3.addWidget(self.aircon, 2, 1, 1, 1)
        self.electricfan = QtWidgets.QWidget(self.dasboardpage)
        self.electricfan.setMinimumSize(QtCore.QSize(240, 200))
        self.electricfan.setMaximumSize(QtCore.QSize(240, 200))
        self.electricfan.setStyleSheet("background-color: transparent;\n"
"border: 1px solid #000000; \n"
"border-radius: 5px;\n"
"")
        self.electricfan.setObjectName("electricfan")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.electricfan)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.electricfan)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/icons/icon/icons8-fan-50.png"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.electricfan)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_14 = QtWidgets.QLabel(self.electricfan)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: rgb(255, 110, 110);\n"
"")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_2.addWidget(self.label_14)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.gridLayout_3.addWidget(self.electricfan, 2, 2, 1, 1)
        self.door = QtWidgets.QWidget(self.dasboardpage)
        self.door.setMinimumSize(QtCore.QSize(240, 200))
        self.door.setStyleSheet("background-color: transparent;\n"
"border: 1px solid #000000; \n"
"border-radius: 5px;\n"
"")
        self.door.setObjectName("door")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.door)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.door)
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/icons/icon/door.png"))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_15 = QtWidgets.QLabel(self.door)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_5.addWidget(self.label_15)
        self.label_10 = QtWidgets.QLabel(self.door)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgb(255, 110, 110);\n"
"")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_5.addWidget(self.label_10)
        self.horizontalLayout_7.addLayout(self.verticalLayout_5)
        self.gridLayout_3.addWidget(self.door, 3, 1, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.dasboardpage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(20, 20))
        self.widget_2.setMaximumSize(QtCore.QSize(400, 60))
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_19 = QtWidgets.QLabel(self.widget_2)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout_9.addWidget(self.label_19, 0, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.widget_2)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout_9.addWidget(self.label_20, 1, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.widget_2)
        self.label_17.setStyleSheet("background-color: rgb(255, 110, 110);\n"
"")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.gridLayout_9.addWidget(self.label_17, 1, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.widget_2)
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.gridLayout_9.addWidget(self.label_16, 0, 1, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_9, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.widget_2, 1, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.dasboardpage)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("border-radius: 11px; ")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 1, 0, 1, 1)
        self.powerconsumption = QtWidgets.QWidget(self.dasboardpage)
        self.powerconsumption.setMinimumSize(QtCore.QSize(240, 200))
        self.powerconsumption.setMaximumSize(QtCore.QSize(240, 200))
        self.powerconsumption.setStyleSheet("background-color: transparent;\n"
"border: 1px solid #000000; \n"
"border-radius: 5px;\n"
"")
        self.powerconsumption.setObjectName("powerconsumption")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.powerconsumption)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.powerconsumption)
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/icons/icon/Pc.png"))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_8.addWidget(self.label_7)
        self.tableView = QtWidgets.QTableView(self.powerconsumption)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_8.addWidget(self.tableView)
        self.gridLayout_3.addWidget(self.powerconsumption, 3, 2, 1, 1)
        self.dashboard = QtWidgets.QWidget(self.dasboardpage)
        self.dashboard.setMinimumSize(QtCore.QSize(240, 200))
        self.dashboard.setMaximumSize(QtCore.QSize(240, 200))
        self.dashboard.setStyleSheet("background-color: transparent;\n"
"border: 1px solid #000000; \n"
"border-radius: 5px;\n"
"")
        self.dashboard.setObjectName("dashboard")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.dashboard)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(self.dashboard)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/icon/people.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.lcdNumber = QtWidgets.QLCDNumber(self.dashboard)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(3)
        self.lcdNumber.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setProperty("value", 26.0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout_6.addWidget(self.lcdNumber)
        self.gridLayout_3.addWidget(self.dashboard, 2, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.dasboardpage)
        self.label_21.setStyleSheet("")
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.gridLayout_3.addWidget(self.label_21, 1, 2, 1, 1)
        self.stackedWidget.addWidget(self.dasboardpage)
        self.peoplepage = QtWidgets.QWidget()
        self.peoplepage.setObjectName("peoplepage")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.peoplepage)
        self.gridLayout_5.setContentsMargins(0, 20, 0, 10)
        self.gridLayout_5.setHorizontalSpacing(0)
        self.gridLayout_5.setVerticalSpacing(10)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem4, 4, 1, 1, 1)
        self.people_counter_widget = QtWidgets.QWidget(self.peoplepage)
        self.people_counter_widget.setObjectName("people_counter_widget")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.people_counter_widget)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.peoplelabel_16 = QtWidgets.QLabel(self.people_counter_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.peoplelabel_16.sizePolicy().hasHeightForWidth())
        self.peoplelabel_16.setSizePolicy(sizePolicy)
        self.peoplelabel_16.setText("")
        self.peoplelabel_16.setPixmap(QtGui.QPixmap(":/icons/icon/people.png"))
        self.peoplelabel_16.setAlignment(QtCore.Qt.AlignCenter)
        self.peoplelabel_16.setObjectName("peoplelabel_16")
        self.verticalLayout_9.addWidget(self.peoplelabel_16)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.people_counter_widget)
        self.lcdNumber_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lcdNumber_2.setDigitCount(2)
        self.lcdNumber_2.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_2.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_2.setProperty("value", 20.0)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.verticalLayout_9.addWidget(self.lcdNumber_2)
        self.verticalLayout_9.setStretch(1, 1)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.gridLayout_5.addWidget(self.people_counter_widget, 1, 1, 2, 1)
        spacerItem5 = QtWidgets.QSpacerItem(245, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem5, 2, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(245, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem6, 1, 0, 1, 1)
        self.labelnumber = QtWidgets.QWidget(self.peoplepage)
        self.labelnumber.setObjectName("labelnumber")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.labelnumber)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.peoplelabel = QtWidgets.QLabel(self.labelnumber)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.peoplelabel.setFont(font)
        self.peoplelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.peoplelabel.setObjectName("peoplelabel")
        self.gridLayout_4.addWidget(self.peoplelabel, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.labelnumber, 3, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem7, 0, 1, 1, 1)
        self.gridLayout_5.setRowStretch(1, 1)
        self.stackedWidget.addWidget(self.peoplepage)
        self.airconditionerpage = QtWidgets.QWidget()
        self.airconditionerpage.setObjectName("airconditionerpage")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.airconditionerpage)
        self.gridLayout_6.setContentsMargins(200, 0, 200, 0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem8 = QtWidgets.QSpacerItem(20, 130, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem8, 0, 0, 1, 1)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.aclabel_16 = QtWidgets.QLabel(self.airconditionerpage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aclabel_16.sizePolicy().hasHeightForWidth())
        self.aclabel_16.setSizePolicy(sizePolicy)
        self.aclabel_16.setMinimumSize(QtCore.QSize(200, 70))
        self.aclabel_16.setText("")
        self.aclabel_16.setPixmap(QtGui.QPixmap(":/icons/icon/Ac.png"))
        self.aclabel_16.setAlignment(QtCore.Qt.AlignCenter)
        self.aclabel_16.setObjectName("aclabel_16")
        self.verticalLayout_11.addWidget(self.aclabel_16)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.acimageplugin = QtWidgets.QLabel(self.airconditionerpage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.acimageplugin.sizePolicy().hasHeightForWidth())
        self.acimageplugin.setSizePolicy(sizePolicy)
        self.acimageplugin.setMaximumSize(QtCore.QSize(50, 16777215))
        self.acimageplugin.setText("")
        self.acimageplugin.setPixmap(QtGui.QPixmap(":/icons/icon/icons8-connected-50.png"))
        self.acimageplugin.setAlignment(QtCore.Qt.AlignCenter)
        self.acimageplugin.setObjectName("acimageplugin")
        self.horizontalLayout_8.addWidget(self.acimageplugin)
        self.accounter = QtWidgets.QLabel(self.airconditionerpage)
        font = QtGui.QFont()
        font.setPointSize(100)
        self.accounter.setFont(font)
        self.accounter.setAlignment(QtCore.Qt.AlignCenter)
        self.accounter.setObjectName("accounter")
        self.horizontalLayout_8.addWidget(self.accounter)
        self.accounter_2 = QtWidgets.QLabel(self.airconditionerpage)
        font = QtGui.QFont()
        font.setPointSize(100)
        self.accounter_2.setFont(font)
        self.accounter_2.setStyleSheet("background-color: rgb(255, 110, 110);\n"
"")
        self.accounter_2.setAlignment(QtCore.Qt.AlignCenter)
        self.accounter_2.setObjectName("accounter_2")
        self.horizontalLayout_8.addWidget(self.accounter_2)
        self.acplugoff = QtWidgets.QLabel(self.airconditionerpage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.acplugoff.sizePolicy().hasHeightForWidth())
        self.acplugoff.setSizePolicy(sizePolicy)
        self.acplugoff.setMinimumSize(QtCore.QSize(0, 0))
        self.acplugoff.setMaximumSize(QtCore.QSize(50, 16777215))
        self.acplugoff.setText("")
        self.acplugoff.setPixmap(QtGui.QPixmap(":/icons/icon/icons8-disconnected-50.png"))
        self.acplugoff.setAlignment(QtCore.Qt.AlignCenter)
        self.acplugoff.setObjectName("acplugoff")
        self.horizontalLayout_8.addWidget(self.acplugoff)
        self.verticalLayout_11.addLayout(self.horizontalLayout_8)
        self.gridLayout_6.addLayout(self.verticalLayout_11, 1, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 130, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem9, 3, 0, 1, 1)
        self.aclabel = QtWidgets.QLabel(self.airconditionerpage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aclabel.sizePolicy().hasHeightForWidth())
        self.aclabel.setSizePolicy(sizePolicy)
        self.aclabel.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.aclabel.setFont(font)
        self.aclabel.setAlignment(QtCore.Qt.AlignCenter)
        self.aclabel.setObjectName("aclabel")
        self.gridLayout_6.addWidget(self.aclabel, 2, 0, 1, 1)
        self.gridLayout_6.setRowStretch(1, 2)
        self.stackedWidget.addWidget(self.airconditionerpage)
        self.electricfanpage = QtWidgets.QWidget()
        self.electricfanpage.setObjectName("electricfanpage")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.electricfanpage)
        self.gridLayout_7.setContentsMargins(200, 0, 200, 0)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.electricfanlabel_17 = QtWidgets.QLabel(self.electricfanpage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.electricfanlabel_17.sizePolicy().hasHeightForWidth())
        self.electricfanlabel_17.setSizePolicy(sizePolicy)
        self.electricfanlabel_17.setMinimumSize(QtCore.QSize(200, 70))
        self.electricfanlabel_17.setText("")
        self.electricfanlabel_17.setPixmap(QtGui.QPixmap(":/icons/icon/icons8-fan-50.png"))
        self.electricfanlabel_17.setAlignment(QtCore.Qt.AlignCenter)
        self.electricfanlabel_17.setObjectName("electricfanlabel_17")
        self.verticalLayout_12.addWidget(self.electricfanlabel_17)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.electricfanimageplugin_2 = QtWidgets.QLabel(self.electricfanpage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.electricfanimageplugin_2.sizePolicy().hasHeightForWidth())
        self.electricfanimageplugin_2.setSizePolicy(sizePolicy)
        self.electricfanimageplugin_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.electricfanimageplugin_2.setText("")
        self.electricfanimageplugin_2.setPixmap(QtGui.QPixmap(":/icons/icon/icons8-connected-50.png"))
        self.electricfanimageplugin_2.setAlignment(QtCore.Qt.AlignCenter)
        self.electricfanimageplugin_2.setObjectName("electricfanimageplugin_2")
        self.horizontalLayout_9.addWidget(self.electricfanimageplugin_2)
        self.electricfancounter_3 = QtWidgets.QLabel(self.electricfanpage)
        font = QtGui.QFont()
        font.setPointSize(100)
        self.electricfancounter_3.setFont(font)
        self.electricfancounter_3.setAlignment(QtCore.Qt.AlignCenter)
        self.electricfancounter_3.setObjectName("electricfancounter_3")
        self.horizontalLayout_9.addWidget(self.electricfancounter_3)
        self.electricfancounter_4 = QtWidgets.QLabel(self.electricfanpage)
        font = QtGui.QFont()
        font.setPointSize(100)
        self.electricfancounter_4.setFont(font)
        self.electricfancounter_4.setStyleSheet("background-color: rgb(255, 110, 110);\n"
"")
        self.electricfancounter_4.setAlignment(QtCore.Qt.AlignCenter)
        self.electricfancounter_4.setObjectName("electricfancounter_4")
        self.horizontalLayout_9.addWidget(self.electricfancounter_4)
        self.electricfanplugoff_2 = QtWidgets.QLabel(self.electricfanpage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.electricfanplugoff_2.sizePolicy().hasHeightForWidth())
        self.electricfanplugoff_2.setSizePolicy(sizePolicy)
        self.electricfanplugoff_2.setMinimumSize(QtCore.QSize(0, 0))
        self.electricfanplugoff_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.electricfanplugoff_2.setText("")
        self.electricfanplugoff_2.setPixmap(QtGui.QPixmap(":/icons/icon/icons8-disconnected-50.png"))
        self.electricfanplugoff_2.setAlignment(QtCore.Qt.AlignCenter)
        self.electricfanplugoff_2.setObjectName("electricfanplugoff_2")
        self.horizontalLayout_9.addWidget(self.electricfanplugoff_2)
        self.verticalLayout_12.addLayout(self.horizontalLayout_9)
        self.gridLayout_7.addLayout(self.verticalLayout_12, 1, 0, 1, 3)
        self.electricfanlabel_2 = QtWidgets.QLabel(self.electricfanpage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.electricfanlabel_2.sizePolicy().hasHeightForWidth())
        self.electricfanlabel_2.setSizePolicy(sizePolicy)
        self.electricfanlabel_2.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.electricfanlabel_2.setFont(font)
        self.electricfanlabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.electricfanlabel_2.setObjectName("electricfanlabel_2")
        self.gridLayout_7.addWidget(self.electricfanlabel_2, 2, 0, 1, 3)
        spacerItem10 = QtWidgets.QSpacerItem(20, 130, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem10, 3, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 130, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem11, 0, 1, 1, 1)
        self.gridLayout_7.setRowStretch(1, 1)
        self.stackedWidget.addWidget(self.electricfanpage)
        self.lightspage = QtWidgets.QWidget()
        self.lightspage.setObjectName("lightspage")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.lightspage)
        self.gridLayout_10.setContentsMargins(200, 0, 200, 0)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        spacerItem12 = QtWidgets.QSpacerItem(20, 130, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem12, 0, 0, 1, 1)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.lightlabel_18 = QtWidgets.QLabel(self.lightspage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lightlabel_18.sizePolicy().hasHeightForWidth())
        self.lightlabel_18.setSizePolicy(sizePolicy)
        self.lightlabel_18.setMinimumSize(QtCore.QSize(200, 70))
        self.lightlabel_18.setText("")
        self.lightlabel_18.setPixmap(QtGui.QPixmap(":/icons/icon/light.png"))
        self.lightlabel_18.setAlignment(QtCore.Qt.AlignCenter)
        self.lightlabel_18.setObjectName("lightlabel_18")
        self.verticalLayout_13.addWidget(self.lightlabel_18)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lightimageplugin_3 = QtWidgets.QLabel(self.lightspage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lightimageplugin_3.sizePolicy().hasHeightForWidth())
        self.lightimageplugin_3.setSizePolicy(sizePolicy)
        self.lightimageplugin_3.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lightimageplugin_3.setText("")
        self.lightimageplugin_3.setPixmap(QtGui.QPixmap(":/icons/icon/icons8-connected-50.png"))
        self.lightimageplugin_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lightimageplugin_3.setObjectName("lightimageplugin_3")
        self.horizontalLayout_10.addWidget(self.lightimageplugin_3)
        self.lightcounter_5 = QtWidgets.QLabel(self.lightspage)
        font = QtGui.QFont()
        font.setPointSize(100)
        self.lightcounter_5.setFont(font)
        self.lightcounter_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lightcounter_5.setObjectName("lightcounter_5")
        self.horizontalLayout_10.addWidget(self.lightcounter_5)
        self.lightcounter_6 = QtWidgets.QLabel(self.lightspage)
        font = QtGui.QFont()
        font.setPointSize(100)
        self.lightcounter_6.setFont(font)
        self.lightcounter_6.setStyleSheet("background-color: rgb(255, 110, 110);\n"
"")
        self.lightcounter_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lightcounter_6.setObjectName("lightcounter_6")
        self.horizontalLayout_10.addWidget(self.lightcounter_6)
        self.lightplugoff_3 = QtWidgets.QLabel(self.lightspage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lightplugoff_3.sizePolicy().hasHeightForWidth())
        self.lightplugoff_3.setSizePolicy(sizePolicy)
        self.lightplugoff_3.setMinimumSize(QtCore.QSize(0, 0))
        self.lightplugoff_3.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lightplugoff_3.setText("")
        self.lightplugoff_3.setPixmap(QtGui.QPixmap(":/icons/icon/icons8-disconnected-50.png"))
        self.lightplugoff_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lightplugoff_3.setObjectName("lightplugoff_3")
        self.horizontalLayout_10.addWidget(self.lightplugoff_3)
        self.verticalLayout_13.addLayout(self.horizontalLayout_10)
        self.gridLayout_10.addLayout(self.verticalLayout_13, 1, 0, 1, 1)
        self.lightlabel_3 = QtWidgets.QLabel(self.lightspage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lightlabel_3.sizePolicy().hasHeightForWidth())
        self.lightlabel_3.setSizePolicy(sizePolicy)
        self.lightlabel_3.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lightlabel_3.setFont(font)
        self.lightlabel_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lightlabel_3.setObjectName("lightlabel_3")
        self.gridLayout_10.addWidget(self.lightlabel_3, 2, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 130, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem13, 3, 0, 1, 1)
        self.gridLayout_10.setRowStretch(1, 1)
        self.stackedWidget.addWidget(self.lightspage)
        self.doorpage = QtWidgets.QWidget()
        self.doorpage.setObjectName("doorpage")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.doorpage)
        self.gridLayout_11.setContentsMargins(200, 0, 200, 0)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        spacerItem14 = QtWidgets.QSpacerItem(20, 130, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem14, 0, 0, 1, 1)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.doorlabel_19 = QtWidgets.QLabel(self.doorpage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doorlabel_19.sizePolicy().hasHeightForWidth())
        self.doorlabel_19.setSizePolicy(sizePolicy)
        self.doorlabel_19.setMinimumSize(QtCore.QSize(200, 70))
        self.doorlabel_19.setText("")
        self.doorlabel_19.setPixmap(QtGui.QPixmap(":/icons/icon/door.png"))
        self.doorlabel_19.setAlignment(QtCore.Qt.AlignCenter)
        self.doorlabel_19.setObjectName("doorlabel_19")
        self.verticalLayout_14.addWidget(self.doorlabel_19)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.doorimageplugin_4 = QtWidgets.QLabel(self.doorpage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doorimageplugin_4.sizePolicy().hasHeightForWidth())
        self.doorimageplugin_4.setSizePolicy(sizePolicy)
        self.doorimageplugin_4.setMaximumSize(QtCore.QSize(50, 16777215))
        self.doorimageplugin_4.setText("")
        self.doorimageplugin_4.setPixmap(QtGui.QPixmap(":/icons/icon/icons8-door-50.png"))
        self.doorimageplugin_4.setAlignment(QtCore.Qt.AlignCenter)
        self.doorimageplugin_4.setObjectName("doorimageplugin_4")
        self.horizontalLayout_11.addWidget(self.doorimageplugin_4)
        self.doorcounter_7 = QtWidgets.QLabel(self.doorpage)
        font = QtGui.QFont()
        font.setPointSize(100)
        self.doorcounter_7.setFont(font)
        self.doorcounter_7.setAlignment(QtCore.Qt.AlignCenter)
        self.doorcounter_7.setObjectName("doorcounter_7")
        self.horizontalLayout_11.addWidget(self.doorcounter_7)
        self.doorcounter_8 = QtWidgets.QLabel(self.doorpage)
        font = QtGui.QFont()
        font.setPointSize(100)
        self.doorcounter_8.setFont(font)
        self.doorcounter_8.setStyleSheet("background-color: rgb(255, 110, 110);\n"
"")
        self.doorcounter_8.setAlignment(QtCore.Qt.AlignCenter)
        self.doorcounter_8.setObjectName("doorcounter_8")
        self.horizontalLayout_11.addWidget(self.doorcounter_8)
        self.doorplugoff_4 = QtWidgets.QLabel(self.doorpage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doorplugoff_4.sizePolicy().hasHeightForWidth())
        self.doorplugoff_4.setSizePolicy(sizePolicy)
        self.doorplugoff_4.setMinimumSize(QtCore.QSize(0, 0))
        self.doorplugoff_4.setMaximumSize(QtCore.QSize(50, 16777215))
        self.doorplugoff_4.setText("")
        self.doorplugoff_4.setPixmap(QtGui.QPixmap(":/icons/icon/icons8-door-50 (4).png"))
        self.doorplugoff_4.setAlignment(QtCore.Qt.AlignCenter)
        self.doorplugoff_4.setObjectName("doorplugoff_4")
        self.horizontalLayout_11.addWidget(self.doorplugoff_4)
        self.verticalLayout_14.addLayout(self.horizontalLayout_11)
        self.gridLayout_11.addLayout(self.verticalLayout_14, 1, 0, 1, 1)
        self.doorlabel_4 = QtWidgets.QLabel(self.doorpage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doorlabel_4.sizePolicy().hasHeightForWidth())
        self.doorlabel_4.setSizePolicy(sizePolicy)
        self.doorlabel_4.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.doorlabel_4.setFont(font)
        self.doorlabel_4.setAlignment(QtCore.Qt.AlignCenter)
        self.doorlabel_4.setObjectName("doorlabel_4")
        self.gridLayout_11.addWidget(self.doorlabel_4, 2, 0, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 130, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem15, 3, 0, 1, 1)
        self.gridLayout_11.setRowMinimumHeight(2, 1)
        self.gridLayout_11.setRowStretch(1, 1)
        self.stackedWidget.addWidget(self.doorpage)
        self.powerconsumptionpage = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.powerconsumptionpage.sizePolicy().hasHeightForWidth())
        self.powerconsumptionpage.setSizePolicy(sizePolicy)
        self.powerconsumptionpage.setObjectName("powerconsumptionpage")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.powerconsumptionpage)
        self.gridLayout_12.setContentsMargins(10, 0, 10, 0)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.powerconsumptionlabel_22 = QtWidgets.QLabel(self.powerconsumptionpage)
        self.powerconsumptionlabel_22.setText("")
        self.powerconsumptionlabel_22.setPixmap(QtGui.QPixmap(":/icons/icon/Pc.png"))
        self.powerconsumptionlabel_22.setAlignment(QtCore.Qt.AlignCenter)
        self.powerconsumptionlabel_22.setObjectName("powerconsumptionlabel_22")
        self.horizontalLayout_15.addWidget(self.powerconsumptionlabel_22)
        self.powerconsumtioncalendarWidget = QtWidgets.QCalendarWidget(self.powerconsumptionpage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.powerconsumtioncalendarWidget.sizePolicy().hasHeightForWidth())
        self.powerconsumtioncalendarWidget.setSizePolicy(sizePolicy)
        self.powerconsumtioncalendarWidget.setMinimumSize(QtCore.QSize(0, 400))
        self.powerconsumtioncalendarWidget.setMaximumSize(QtCore.QSize(16777215, 400))
        self.powerconsumtioncalendarWidget.setObjectName("powerconsumtioncalendarWidget")
        self.horizontalLayout_15.addWidget(self.powerconsumtioncalendarWidget)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_13.addLayout(self.horizontalLayout_12)
        self.verticalLayout_15.addLayout(self.horizontalLayout_13)
        self.powerconsumptionlabel_5 = QtWidgets.QLabel(self.powerconsumptionpage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.powerconsumptionlabel_5.sizePolicy().hasHeightForWidth())
        self.powerconsumptionlabel_5.setSizePolicy(sizePolicy)
        self.powerconsumptionlabel_5.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.powerconsumptionlabel_5.setFont(font)
        self.powerconsumptionlabel_5.setAlignment(QtCore.Qt.AlignCenter)
        self.powerconsumptionlabel_5.setObjectName("powerconsumptionlabel_5")
        self.verticalLayout_15.addWidget(self.powerconsumptionlabel_5)
        self.gridLayout_12.addLayout(self.verticalLayout_15, 1, 0, 1, 3)
        spacerItem16 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem16, 2, 1, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem17, 0, 1, 1, 1)
        self.stackedWidget.addWidget(self.powerconsumptionpage)
        self.infopage = QtWidgets.QWidget()
        self.infopage.setObjectName("infopage")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.infopage)
        self.gridLayout_13.setContentsMargins(0, 20, 0, 20)
        self.gridLayout_13.setHorizontalSpacing(0)
        self.gridLayout_13.setVerticalSpacing(20)
        self.gridLayout_13.setObjectName("gridLayout_13")
        spacerItem18 = QtWidgets.QSpacerItem(173, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem18, 0, 1, 1, 1)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_26 = QtWidgets.QLabel(self.infopage)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_16.addWidget(self.label_26)
        self.label_27 = QtWidgets.QLabel(self.infopage)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_16.addWidget(self.label_27)
        self.label_28 = QtWidgets.QLabel(self.infopage)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_16.addWidget(self.label_28)
        self.horizontalLayout_19.addLayout(self.verticalLayout_16)
        self.verticalLayout_17.addLayout(self.horizontalLayout_19)
        self.gridLayout_13.addLayout(self.verticalLayout_17, 4, 2, 1, 2)
        self.label_22 = QtWidgets.QLabel(self.infopage)
        self.label_22.setMinimumSize(QtCore.QSize(250, 0))
        self.label_22.setMaximumSize(QtCore.QSize(250, 70))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout_13.addWidget(self.label_22, 0, 2, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.infopage)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_13.addWidget(self.textBrowser, 1, 1, 3, 4)
        spacerItem19 = QtWidgets.QSpacerItem(173, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem19, 4, 1, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(181, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem20, 0, 3, 1, 2)
        spacerItem21 = QtWidgets.QSpacerItem(174, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem21, 4, 4, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem22, 2, 0, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem23, 2, 5, 1, 1)
        self.stackedWidget.addWidget(self.infopage)
        self.gridLayout_2.addWidget(self.stackedWidget, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.pushButton_10.toggled['bool'].connect(self.icons_details_widget.setHidden) # type: ignore
        self.pushButton_10.toggled['bool'].connect(self.icon_only_widget.setVisible) # type: ignore
        self.dashboardbutton_2.toggled['bool'].connect(self.dashboardbutton.setChecked) # type: ignore
        self.peoplebutton_2.toggled['bool'].connect(self.peoplebutton.setChecked) # type: ignore
        self.acbutton_2.toggled['bool'].connect(self.acbutton.setChecked) # type: ignore
        self.eclectricfanbutton.toggled['bool'].connect(self.electricfanbutton.setChecked) # type: ignore
        self.lightsbutton_2.toggled['bool'].connect(self.lightsbutton.setChecked) # type: ignore
        self.doorbutton_2.toggled['bool'].connect(self.doorbutton.setChecked) # type: ignore
        self.powerconsumptionbutton_2.toggled['bool'].connect(self.powerconsumptionbutton.setChecked) # type: ignore
        self.infobutton_2.toggled['bool'].connect(self.infobutton.setChecked) # type: ignore
        self.exitbutton_2.toggled['bool'].connect(self.exitbutton.setChecked) # type: ignore
        self.dashboardbutton.toggled['bool'].connect(self.dashboardbutton_2.setChecked) # type: ignore
        self.peoplebutton.toggled['bool'].connect(self.peoplebutton_2.setChecked) # type: ignore
        self.acbutton.toggled['bool'].connect(self.acbutton_2.setChecked) # type: ignore
        self.electricfanbutton.toggled['bool'].connect(self.eclectricfanbutton.setChecked) # type: ignore
        self.lightsbutton.toggled['bool'].connect(self.lightsbutton_2.setChecked) # type: ignore
        self.doorbutton.toggled['bool'].connect(self.doorbutton_2.setChecked) # type: ignore
        self.powerconsumptionbutton.toggled['bool'].connect(self.powerconsumptionbutton_2.setChecked) # type: ignore
        self.infobutton.toggled['bool'].connect(self.infobutton_2.setChecked) # type: ignore
        self.exitbutton.toggled['bool'].connect(self.exitbutton_2.setChecked) # type: ignore
        self.exitbutton.clicked.connect(MainWindow.close) # type: ignore
        self.exitbutton_2.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dashboardbutton.setText(_translate("MainWindow", "  Dashboard"))
        self.peoplebutton.setText(_translate("MainWindow", "   People"))
        self.acbutton.setText(_translate("MainWindow", "  Air \n"
" Conditioner"))
        self.electricfanbutton.setText(_translate("MainWindow", " Electric fan"))
        self.lightsbutton.setText(_translate("MainWindow", "  Lights"))
        self.doorbutton.setText(_translate("MainWindow", "  Door"))
        self.powerconsumptionbutton.setText(_translate("MainWindow", "     Power \n"
"   Consumption"))
        self.infobutton.setText(_translate("MainWindow", "   Info"))
        self.exitbutton.setText(_translate("MainWindow", "Exit"))
        self.icon_only_Acc.setText(_translate("MainWindow", "ACC"))
        self.label_2.setText(_translate("MainWindow", "Adaptive Classroom Control"))
        self.label_5.setText(_translate("MainWindow", "4"))
        self.label_8.setText(_translate("MainWindow", "2"))
        self.label_12.setText(_translate("MainWindow", "1"))
        self.label_9.setText(_translate("MainWindow", "1"))
        self.label_3.setText(_translate("MainWindow", "2"))
        self.label_14.setText(_translate("MainWindow", "3"))
        self.label_15.setText(_translate("MainWindow", "2"))
        self.label_10.setText(_translate("MainWindow", "0"))
        self.label_19.setText(_translate("MainWindow", "White = On"))
        self.label_20.setText(_translate("MainWindow", "Red = Off"))
        self.label_18.setText(_translate("MainWindow", "Dashboard"))
        self.peoplelabel.setText(_translate("MainWindow", "People that is currently in the area that are being \n"
" detected by the system."))
        self.accounter.setText(_translate("MainWindow", "1"))
        self.accounter_2.setText(_translate("MainWindow", "1"))
        self.aclabel.setText(_translate("MainWindow", "The air conditioner that is currently running inside the room\n"
"will automatically turn on or off depending on the temperature\n"
"and the presence of people in the area."))
        self.electricfancounter_3.setText(_translate("MainWindow", "2"))
        self.electricfancounter_4.setText(_translate("MainWindow", "0"))
        self.electricfanlabel_2.setText(_translate("MainWindow", "The electric fan currently running inside the room will\n"
" automatically turn on or off based on the temperature\n"
" and the presence of people in the area."))
        self.lightcounter_5.setText(_translate("MainWindow", "2"))
        self.lightcounter_6.setText(_translate("MainWindow", "0"))
        self.lightlabel_3.setText(_translate("MainWindow", "The lights currently running inside the room will\n"
" automatically turn on or off based on the temperature\n"
" and the presence of people in the area."))
        self.doorcounter_7.setText(_translate("MainWindow", "2"))
        self.doorcounter_8.setText(_translate("MainWindow", "0"))
        self.doorlabel_4.setText(_translate("MainWindow", "Doors that is currently open or close."))
        self.powerconsumptionlabel_5.setText(_translate("MainWindow", "Power that are currently being consume"))
        self.label_26.setText(_translate("MainWindow", "Version 1.0\n"
" Developers & Researchers"))
        self.label_27.setText(_translate("MainWindow", "Aquino, Marc Adrian\n"
"Carilla, Tristan Paul\n"
"Cerezo, Mario\n"
"Sagun, Argielyn Mae\n"
"Ungos, Warren"))
        self.label_28.setText(_translate("MainWindow", "Develope in November 2023"))
        self.label_22.setText(_translate("MainWindow", "About ACC"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">Adaptive Classroom Contro(ACC)</span><span style=\" font-size:20pt;\">: Utilize YOLO Algorithm for Human Detection, Temperature Control and Electrical EnergyConservation</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Adaptive Classroom Control (ACC), also known as ACC, is a cutting-edge system designed to create a smarter and more efficient classroom environment. ACC seamlessly integrates with various devices, such as air conditioners, electric fans, and lights, to dynamically respond to the presence of people and the temperature inside the room. The goal is to optimize energy usage and create a comfortable learning space.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt;\"><br /></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Future DevelopmentsWe are committed to enhancing ACC to meet the evolving needs of educational environments. Planned future developments include:Integration with Smart Devices: Extend compatibility to include more smart devices for a fully connected classroom experience.Customization Options: Allow users to customize ACC settings to align with specific preferences and classroom requirements.</span></p></body></html>"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
