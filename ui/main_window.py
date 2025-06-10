from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SMM Assistant")
        self.setGeometry(100, 100, 800, 600)
        label = QLabel("Приложение запущено!", self)
        label.move(50, 50)
