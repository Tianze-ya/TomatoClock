from src.tool import *
from src.typelib import *
from PyQt6.QtWidgets import QWidget


class ToolWindowUI(QWidget):
    def __init__(self, parent: MainWindowUI):
        super().__init__()
        
        self.ui = Ui_Tool()
        self.ui.setupUi(self)
        self.parent = parent
        
        self.ui.SaveButton.clicked.connect(self.save_button_clicked)
        
        self.ui.worktime_h.setText(self.parent.worktime[0])
        self.ui.worktime_m.setText(self.parent.worktime[1])
        self.ui.resttime_h.setText(self.parent.resttime[0])
        self.ui.resttime_m.setText(self.parent.resttime[1])

    def save_button_clicked(self):
        self.parent.worktime = [self.ui.worktime_h.text().zfill(2), self.ui.worktime_m.text().zfill(2)]
        self.parent.resttime = [self.ui.resttime_h.text().zfill(2), self.ui.resttime_m.text().zfill(2)]
        
        self.close()
