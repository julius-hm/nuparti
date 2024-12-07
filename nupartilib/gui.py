from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Nupartilib")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.label = QLabel("Bienvenid@", self)
        layout.addWidget(self.label)

        self.button = QPushButton("Presiona aquí", self)
        self.button.clicked.connect(self.change_text)
        layout.addWidget(self.button)

        self.setLayout(layout)

    # Boton para cambio de texto (ejemplo)
    def change_text(self):
        self.label.setText("¡El texto ha cambiado!")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()