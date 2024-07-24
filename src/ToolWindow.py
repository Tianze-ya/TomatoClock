from src.tool import *
from src.typelib import MainWindow
from PyQt6.QtWidgets import QWidget


class ToolWindowUI(QWidget):
    def __init__(self, parent: MainWindow):
        super().__init__()
        self.ui = Ui_Tool()
        self.ui.setupUi(self)
        self.parent = parent
        self.ui.SaveButton.clicked.connect(self.save_button_clicked)

    def save_button_clicked(self):
        if self.parent.state == "工作中":
            self.parent.time_h = self.ui.worktime_h.text().zfill(2)
            self.parent.time_m = self.ui.worktime_m.text().zfill(2)
        else:
            self.parent.time_h = self.ui.resttime_h.text().zfill(2)
            self.parent.time_m = self.ui.resttime_m.text().zfill(2)
