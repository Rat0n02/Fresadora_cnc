﻿import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect, QTextBrowser, QSizePolicy
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QColor, QResizeEvent, QMovie
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
import subprocess

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi("C:/Users/ORG LESBOS/PycharmProjects/CnC/interfaz/diseño01.ui", self)

        # Crea un historial vacío
        self.historial = []

        self.bt_menu_uno.clicked.connect(self.mover_menu)
        self.bt_menu_dos.clicked.connect(self.mover_menu)
        # ocultar botones
        self.bt_restaurar.hide()
        self.bt_menu_dos.hide()

        # sombra de los widgets
        self.sombra_frame(self.frame_superior)
        self.sombra_frame(self.toolBox)
        self.sombra_frame(self.bt_uno)
        self.sombra_frame(self.bt_dos)
        self.sombra_frame(self.bt_tres)
        self.sombra_frame(self.bt_cuatro)
        self.sombra_frame(self.bt_cinco)
        self.sombra_frame(self.bt_seis)
      

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
        
        self.bt_dos.clicked.connect(self.Archivos)
        self.bt_tres.clicked.connect(self.Cargando)
        self.bt_cuatro.clicked.connect(self.Cancelando)
        #acceder a las aplicaciones 
        self.bt_cinco.clicked.connect(self.abrir_aplicacion_dos)
        self.bt_seis.clicked.connect(self.abrir_aplicacion_uno)

    def control_bt_minimizar(self):
        self.showMinimized()

    def control_bt_maximizar(self):
        self.showMaximized()
        self.bt_maximizar.hide()
        self.bt_restaurar.show()

    def control_bt_normal(self):
        self.showNormal()
        self.bt_restaurar.hide()
        self.bt_maximizar.show()

    # creamos método de sombras
    def sombra_frame(self, frame):
        sombra = QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(30)
        sombra.setXOffset(8)
        sombra.setYOffset(8)
        sombra.setColor(QColor(20, 172, 53, 164))
        frame.setGraphicsEffect(sombra)

    ## sizeGrip
    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    def mousePressEvent(self, event):
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

    def agregar_al_historial(self, texto):
            self.historial.append(texto)
            texto_historial = '\n'.join(self.historial)
            self.historialTextBrowser.setPlainText(texto_historial)

    # ANIMACION DE PAGINAS
    def Archivos(self):
        self.toolBox.setCurrentWidget(self.page_uno)
        self.animacion_paginas()
         # Cargar GIF en el QLabel de la página page_uno
        gif_path = "C:/Users/ORG LESBOS/PycharmProjects/CnC/interfaz/imagenes/slyven.gif"
        movie = QMovie(gif_path)
        label = self.page_uno.findChild(QtWidgets.QLabel, "label_tres")  
        label.setMovie(movie)
        # Ajustar el tamaño máximo del QLabel
        label.setMaximumSize(431, 331)  # Ajusta según tus necesidades
        # Ajustar la escala del GIF para que se ajuste al tamaño máximo
        label.setScaledContents(True)
        movie.start()
        self.agregar_al_historial("Se abrió la página de Archivos")


    def Cargando(self):
        self.toolBox.setCurrentWidget(self.page_dos)
        self.animacion_paginas()
    # Cargar GIF en el QLabel de la página page_dos
        gif_path = "c:/Users/ORG LESBOS/PycharmProjects/CnC/interfaz/imagenes/baile.gif"  # Reemplaza con la ruta correcta de tu archivo GIF
        movie = QMovie(gif_path)
        label = self.page_dos.findChild(QtWidgets.QLabel, "label_uno")  # Reemplaza "label_uno" con el nombre real de tu QLabel
        label.setMovie(movie)
        # Ajustar el tamaño máximo del QLabel
        label.setMaximumSize(431, 331)  # Ajusta según tus necesidades
        # Ajustar la escala del GIF para que se ajuste al tamaño máximo
        label.setScaledContents(True)
        movie.start()
        self.agregar_al_historial("Se abrió la página de Cargando")
    

    def Cancelando(self):
        self.toolBox.setCurrentWidget(self.page_tres)
        self.animacion_paginas()
        gif_path = "C:/Users/ORG LESBOS/PycharmProjects/CnC/interfaz/imagenes/6OV3.gif"
        movie = QMovie(gif_path)
        label = self.page_tres.findChild(QtWidgets.QLabel, "label_dos")  # Reemplaza "label_dos" con el nombre real de tu QLabel
        label.setMovie(movie)
        # Ajustar el tamaño máximo del QLabel
        label.setMaximumSize(541, 401)  # Ajusta según tus necesidades
        # Ajustar la escala del GIF para que se ajuste al tamaño máximo
        label.setScaledContents(True)
        movie.start()
        self.agregar_al_historial("Se abrió la página de Cancelando")

    def abrir_aplicacion_uno(self):
        try:
            # Reemplaza 'ruta' con la ruta correcta de la aplicación que deseas abrir
            subprocess.run(['C:/Program Files/Inkscape/bin7inkscape.exe'])
        except Exception as e:
            print(f"Error al abrir la aplicación: {e}")
            self.agregar_al_historial("Se abrió la aplicacion Inskape")
    def abrir_aplicacion_dos(self):
        try:
            
            # Reemplaza 'ruta' con la ruta correcta de la aplicación que deseas abrir
            subprocess.run(['c:/Users/ORG LESBOS/PycharmProjects/CnC/ugsplatform-win/bin/ugsplatform64.exe'])
        except Exception as f:
            print(f"Error al abrir la aplicación: {f}")
            self.agregar_al_historial("Se abrió la página de Gcode Universal")
    
    def animacion_paginas(self):
        if True:
            width = self.toolBox.width()
            x1 = self.frame_5.rect().right()

            normal = 100
            if width == 100:
                extender = x1
            else:
                extender = x1
            self.animacion1 = QPropertyAnimation(self.toolBox, b"maximumWidth")
            self.animacion1.setStartValue(width)
            self.animacion1.setEndValue(extender)
            self.animacion1.setDuration(500)
            self.animacion1.setEasingCurve(QEasingCurve.InOutQuad)
            self.animacion1.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())