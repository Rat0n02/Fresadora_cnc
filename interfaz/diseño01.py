from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class VentanaPrincipal(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(838, 690)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color:"
                                         u" qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, "
                                         u"stop:0 rgba(245, 224, 176, 255), stop:0.09 rgba(246, 189, 237, 255), "
                                         u"stop:0.14 rgba(194, 207, 246, 255), stop:0.19 rgba(184, 160, 168, 255), "
                                         u"stop:0.25 rgba(171, 186, 248, 255), stop:0.32 rgba(243, 248, 224, 255), "
                                         u"stop:0.385 rgba(249, 162, 183, 255), stop:0.47 rgba(100, 115, 124, 255), "
                                         u"stop:0.58 rgba(251, 205, 202, 255), stop:0.65 rgba(170, 128, 185, 255),"
                                         u" stop:0.75 rgba(252, 222, 204, 255), stop:0.805 rgba(206, 122, 218, 255),"
                                         u" stop:0.86 rgba(254, 223, 175, 255), stop:0.91 rgba(254, 236, 244, 255), "
                                         u"stop:1 rgba(255, 191, 221, 255));")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.frame_superior = QFrame(self.frame)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMaximumSize(QSize(16777215, 40))
        self.frame_superior.setStyleSheet(u"background-color: rgb(172, 53, 164);")
        self.frame_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Raised)

        self.horizontalLayout = QHBoxLayout(self.frame_superior)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.label_MENU = QLabel(self.frame_superior)
        self.label_MENU.setObjectName(u"label_MENU")
        font = QFont()
        font.setFamily(u"Gill Sans Ultra Bold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_MENU.setFont(font)
        self.label_MENU.setStyleSheet(u"font: 14pt \"Gill Sans Ultra Bold\";\n"
"color:rgb(255, 255, 255);\n"
"bord: rgb(1, 227, 252);")

        self.horizontalLayout.addWidget(self.label_MENU)

        self.horizontalSpacer = QSpacerItem(551, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.bt_bajar = QPushButton(self.frame_superior)
        self.bt_bajar.setObjectName(u"bt_bajar")
        self.bt_bajar.setStyleSheet(u"background-color:rgb(255, 170, 255)")
        icon = QIcon()
        icon.addFile(u"imagenes/bajar.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_bajar.setIcon(icon)

        self.horizontalLayout.addWidget(self.bt_bajar)

        self.bt_minimizar = QPushButton(self.frame_superior)
        self.bt_minimizar.setObjectName(u"bt_minimizar")
        self.bt_minimizar.setStyleSheet(u"background-color:rgb(255, 170, 255)")
        icon1 = QIcon()
        icon1.addFile(u"imagenes/minimizar.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_minimizar.setIcon(icon1)

        self.horizontalLayout.addWidget(self.bt_minimizar)

        self.bt_maximizar = QPushButton(self.frame_superior)
        self.bt_maximizar.setObjectName(u"bt_maximizar")
        self.bt_maximizar.setStyleSheet(u"background-color:rgb(255, 170, 255)")
        icon2 = QIcon()
        icon2.addFile(u"imagenes/maximizar.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_maximizar.setIcon(icon2)

        self.horizontalLayout.addWidget(self.bt_maximizar)

        self.pushButton = QPushButton(self.frame_superior)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background-color:rgb(255, 170, 255)")
        icon3 = QIcon()
        icon3.addFile(u"imagenes/cerrar.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon3)

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_2.addWidget(self.frame_superior)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setEnabled(True)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(246, 158, 252);\n"
"\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.bt_uno = QPushButton(self.frame_2)
        self.bt_uno.setObjectName(u"bt_uno")
        self.bt_uno.setStyleSheet(u"font: 16pt \"Bauhaus 93\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(220, 178, 73);\n"
"alternate-background-color: rgb(0, 0, 0);")
        icon4 = QIcon()
        icon4.addFile(u"imagenes/eevee_icon-icons.com_67563.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_uno.setIcon(icon4)
        self.bt_uno.setIconSize(QSize(40, 40))

        self.verticalLayout_7.addWidget(self.bt_uno)

        self.bt_dos = QPushButton(self.frame_2)
        self.bt_dos.setObjectName(u"bt_dos")
        self.bt_dos.setLayoutDirection(Qt.LeftToRight)
        self.bt_dos.setStyleSheet(u"font: 16pt \"Bauhaus 93\";\n"
"COLOR:rgb(255, 255, 255);\n"
"background-color: rgb(162, 252, 93);")
        icon5 = QIcon()
        icon5.addFile(u"imagenes/bulbasaur_icon-icons.com_67580.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_dos.setIcon(icon5)
        self.bt_dos.setIconSize(QSize(40, 40))

        self.verticalLayout_7.addWidget(self.bt_dos)

        self.bt_tres = QPushButton(self.frame_2)
        self.bt_tres.setObjectName(u"bt_tres")
        self.bt_tres.setLayoutDirection(Qt.LeftToRight)
        self.bt_tres.setAutoFillBackground(False)
        self.bt_tres.setStyleSheet(u"font: 16pt \"Bauhaus 93\";\n"
"COLOR:rgb(255, 255, 255);\n"
"background-color: rgb(87, 180, 252);")
        icon6 = QIcon()
        icon6.addFile(u"imagenes/snorlax_icon-icons.com_67505.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_tres.setIcon(icon6)
        self.bt_tres.setIconSize(QSize(40, 40))

        self.verticalLayout_7.addWidget(self.bt_tres)

        self.bt_cuatro = QPushButton(self.frame_2)
        self.bt_cuatro.setObjectName(u"bt_cuatro")
        self.bt_cuatro.setStyleSheet(u"font: 16pt \"Bauhaus 93\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(248, 110, 64);")
        icon7 = QIcon()
        icon7.addFile(u"imagenes/charmander_icon-icons.com_67576.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_cuatro.setIcon(icon7)
        self.bt_cuatro.setIconSize(QSize(40, 40))

        self.verticalLayout_7.addWidget(self.bt_cuatro)

        self.bt_cinco = QPushButton(self.frame_2)
        self.bt_cinco.setObjectName(u"bt_cinco")
        self.bt_cinco.setStyleSheet(u"font: 16pt \"Bauhaus 93\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 0, 0);\n"
"\n"
"")
        icon8 = QIcon()
        icon8.addFile(u"imagenes/Pokeball_icon-icons.com_67533.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_cinco.setIcon(icon8)

        self.verticalLayout_7.addWidget(self.bt_cinco)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.frame_paginas = QFrame(self.frame_3)
        self.frame_paginas.setObjectName(u"frame_paginas")
        self.frame_paginas.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 224, 176, 255), stop:0.09 rgba(246, 189, 237, 255), stop:0.14 rgba(194, 207, 246, 255), stop:0.19 rgba(184, 160, 168, 255), stop:0.25 rgba(171, 186, 248, 255), stop:0.32 rgba(243, 248, 224, 255), stop:0.385 rgba(249, 162, 183, 255), stop:0.47 rgba(100, 115, 124, 255), stop:0.58 rgba(251, 205, 202, 255), stop:0.65 rgba(170, 128, 185, 255), stop:0.75 rgba(252, 222, 204, 255), stop:0.805 rgba(206, 122, 218, 255), stop:0.86 rgba(254, 223, 175, 255), stop:0.91 rgba(254, 236, 244, 255), stop:1 rgba(255, 191, 221, 255));\n"
"\n"
"\n"
"")
        self.frame_paginas.setFrameShape(QFrame.StyledPanel)
        self.frame_paginas.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_paginas)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_4 = QFrame(self.frame_paginas)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 50))
        self.frame_4.setStyleSheet(u"background-color:rgb(246, 158, 252);\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.bt_menu_uno = QPushButton(self.frame_4)
        self.bt_menu_uno.setObjectName(u"bt_menu_uno")
        self.bt_menu_uno.setStyleSheet(u"background-color: rgb(97, 252, 242);")
        icon9 = QIcon()
        icon9.addFile(u"imagenes/left-arrows_icon-icons.com_70075.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_menu_uno.setIcon(icon9)
        self.bt_menu_uno.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.bt_menu_uno)

        self.bt_menu_dos = QPushButton(self.frame_4)
        self.bt_menu_dos.setObjectName(u"bt_menu_dos")
        self.bt_menu_dos.setStyleSheet(u"\n"
"background-color: rgb(97, 252, 242);")
        icon10 = QIcon()
        icon10.addFile(u"imagenes/right-arrows_icon-icons.com_69943.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_menu_dos.setIcon(icon10)
        self.bt_menu_dos.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.bt_menu_dos)

        self.lineEdit = QLineEdit(self.frame_4)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.pushButton_12 = QPushButton(self.frame_4)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setStyleSheet(u"background-color: rgb(169, 235, 255);")
        icon11 = QIcon()
        icon11.addFile(u"imagenes/loupe_78956.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon11)

        self.horizontalLayout_3.addWidget(self.pushButton_12)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_paginas)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgb(255, 202, 250);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.toolBox = QToolBox(self.frame_5)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"\n"
"QToolBox::tab{\n"
"	background-color: rgb(255, 0, 255);\n"
"font: 75 16pt \"Bauhaus 93\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QToolBox::tab:selected{\n"
"	background-color: rgb(255, 0, 255);\n"
"font: 75 16pt \"Bauhaus 93\";\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 589, 491))
        icon12 = QIcon()
        icon12.addFile(u"imagenes/squirtle_icon-icons.com_67504.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.widget, icon12, u"Archivos")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 589, 491))
        self.toolBox.addItem(self.page_2, u"carga")

        self.horizontalLayout_4.addWidget(self.toolBox)


        self.verticalLayout_3.addWidget(self.frame_5)


        self.horizontalLayout_2.addWidget(self.frame_paginas)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.verticalLayout_2.setStretch(0, 1)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(1)
        self.toolBox.layout().setSpacing(7)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_MENU.setText(QCoreApplication.translate("MainWindow", u"MENU CNC", None))
        self.bt_bajar.setText("")
        self.bt_minimizar.setText("")
        self.bt_maximizar.setText("")
        self.pushButton.setText("")
        self.bt_uno.setText(QCoreApplication.translate("MainWindow", u"ENCENDER       ", None))
        self.bt_dos.setText(QCoreApplication.translate("MainWindow", u"SUBIR ARCIVO", None))
        self.bt_tres.setText(QCoreApplication.translate("MainWindow", u"COMENZAR", None))
        self.bt_cuatro.setText(QCoreApplication.translate("MainWindow", u"CANCELAR", None))
        self.bt_cinco.setText(QCoreApplication.translate("MainWindow", u"APAGAR", None))
        self.bt_menu_uno.setText("")
        self.bt_menu_dos.setText("")
        self.pushButton_12.setText("")
        self.toolBox.setItemText(self.toolBox.indexOf(self.widget), QCoreApplication.translate("MainWindow", u"Archivos", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"carga", None))
    # retranslateUi


class Ventana(QMainWindow,):
    def __init__(self):
        super().__init__()
        self.resize(300, 200)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = VentanaPrincipal()
    mi_app.show()
    sys.exit(app.exec_())
