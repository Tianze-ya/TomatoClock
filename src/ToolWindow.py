from src.tool import *
from src.typing import MainWindow
from PyQt6.QtWidgets import QWidget


class ToolWindowUI(Ui_Tool, QWidget):
    def __init__(self, parent: MainWindow):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.SaveButton.clicked.connect(self.save_button_clicked)

    def save_button_clicked(self):
        if self.parent.state == "工作中":
            self.parent.time_h = self.worktime_h.text().zfill(2)
            self.parent.time_m = self.worktime_m.text().zfill(2)
        else:
            self.parent.time_h = self.resttime_h.text().zfill(2)
            self.parent.time_m = self.resttime_m.text().zfill(2)

