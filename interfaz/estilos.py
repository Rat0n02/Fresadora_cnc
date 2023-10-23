from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QLabel,QFormLayout,QPushButton
import sys
from  qt_material import apply_stylesheet

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QFormLayout()
        layout.addRow(("QLabel", QLabel("QLabel"))
        layout.addRow("QPushButton",QPushButton("QPushButton"))


       widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet( app ,theme ="dark_amber")
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())