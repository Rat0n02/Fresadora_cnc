from PySide6.QtWidgets import *
from PySide6.QtCore import *
from __feature__ import snake_case, true_property


class myFirstWindow(QMainWindow):
    style_sheet: str

    def setup_ui(self):
        self.set_fixed_size(500, 300)
        self.style_sheet = "background: #ba04ab;"

        self.fr_titulo = QFrame(self)
        self.fr_titulo.geometry = QRect(10, 10, 480, 50)
        self.fr_titulo.style_sheet = "background: #fc79f2;"
#TITULO INICIAL
        self.titulo = QLabel(self.fr_titulo)
        self.titulo.text = "MENU"
        self.titulo.geometry = QRect(0, 0, 480, 50)
        self.titulo.alignment = Qt.AlignCenter
        self.titulo.style_sheet = '''
            color:white;
            font-size: 35px;
            font-weight: bold;
        '''

        self.fr_inputs = QFrame(self)
        self.fr_inputs.geometry = QRect(10, 80, 480, 210)
        self.fr_inputs.style_sheet = "background: #fc79f2;"


#BOTON
        self.boton = QPushButton(self.fr_inputs)
        self.boton.text = ("Subir archivo")

        self.boton.geometry = QRect(10, 25, 220, 40)
        self.boton.alignment = Qt.AlignCenter
        self.boton.style_sheet = '''
            background:#0cebe7;
            color:#650ceb;
            font-size: 35px;
            font-weight: bold;
        '''


import sys
app = QApplication(sys.argv)

window = myFirstWindow()
window.setup_ui()
window.show()

sys.exit(app.exec_())
