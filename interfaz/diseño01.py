import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QColor, QResizeEvent
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi("diseño01.ui", self)

        self.bt_menu_uno.clicked.connect(self.mover_menu)
        self.bt_menu_dos.clicked.connect(self.mover_menu)
        # ocultar botones
        self.bt_restaurar.hide()
        self.bt_menu_dos.hide()
        # control de la barra de título
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.bt_restaurar.clicked.connect(self.control_bt_normal)
        self.bt_maximizar.clicked.connect(self.control_bt_maximizar)
        self.bt_cerrar.clicked.connect(lambda: self.close())

        # eliminar barra y de título -opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        # SizeGrip
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        # mover ventana
        self.frame_superior.mouseMoveEvent = self.mover_ventana

        # acceder a las páginas
        self.bt_dos.clicked.connect(self.pagina_uno)
        self.bt_tres.clicked.connect(self.pagina_dos)
        self.bt_cuatro.clicked.connect(self.pagina_tres)

    def control_bt_minimizar(self):
        self.showMinimized()

    def control_bt_normal(self):
        self.showNormal()
        self.bt_restairar.hide()
        self.bt_maximizar.show()

    def control_bt_maximizar(self):
        self.showMaximizar()
        self.bt_maximizar.hide()
        self.bt_restaurar.show()

    # creamos metodo de sombras
    def sombra_frame(self, frame):
        sombra = QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(30)
        sombra.setXOffset(8)
        sombra.setYOffset(8)
        sombra.setColor(QColor(20, 172, 53, 164))
        frame.setGraphicsEffect(sombra)

    ## sizeGrip
    def resizeEvent(self, event):
        self.clickPosition = event.globalPos()

    def mover_ventana(self, event):
        if self.isMaximized() == False:
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        if event.globalPos().y() <= 10:
            self.showMaximized()
            self.bt_maximizar.hide()
            self.bt_restaurar.show()
        else:
            self.showNormal()
            self.bt_restaurar.hide()
            self.bt_maximizar.show()

    # Metodo para mover el menu lateral izquierdo
    def mover_menu(self):
        if True:
            width = self.menu_lateral.width()
            normal = 0
            if width == 0:
                extender = 300
                self.bt_menu_dos.hide()
                self.bt_menu_uno.show()
            else:
                self.bt_menu_dos.show()
                self.bt_menu_uno.hide()
                extender = normal
            self.animacion = QPropertyAnimation(self.menu_lateral, b"maximumWidth")
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setDuration(500)
            self.animacion.setEasingCurve(QEasingCurve.OutInBack)
            self.animacion.start()

    # ANIMACION DE PAGINAS
    def pagina_uno(self):
        self.stackedWidget.setCurrentWidget(self.page_uno)
        self.animacion_paginas()

    def pagina_dos(self):
        self.stackedWidget.setCurrentWidget(self.page_dos)
        self.animacion_paginas()

    def pagina_tress(self):
        self.stackedWidget.setCurrentWidget(self.page_tres)
        self.animacion_paginas()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
