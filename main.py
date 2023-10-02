from PySide6.QtWidgets import*
from PySide6.QtCore import*
from _feature_ import snake_case,true_property

class myFirtsWindow(QMainWindow):
    def setup_ui(self):
        self.set_fixed_Size (600,440)
        self.style_sheet = "background: #242526;"
#contenedor del titulo
        self.fr_titulo = QFrame(self)
        self.fr_titulo.geometry = QRect(10,10,580,100)
        self.fr_titulo.style_sheet = "background: #0766F5;"
#texto del titulo
        self.titulo = QLabel(self.fr_titulo)
        self.titulo.text = 'MAQUINA_FRESADORA_CNC'
        self.titulo.geometry = QRect(0,0,580,20)
        self.titulo.alignment = Qt.AlignmentCenter
        self.titulo.style_sheet''''''

        self.frame2 = QFrame(self)
        self.frame2.geometry = QRect(10,120,580,310)
        self.frame2.style_sheet = "background: #07F5E5;"

        self.fr_inputs = QFrame(self)
        self.fr_inputs.geometry = QRect(145,340,290,80)
        self.fr_inputs.style_sheet = "background: #F5070F;"
3312

import sys
app = QApplication(sys.argv)

window = myFirtsWindow()
window.setup_ui()
window.show()

