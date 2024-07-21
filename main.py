import sys
import os
from PyQt6.QtWidgets import QApplication
from src.MainWindow import MainWindow
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
