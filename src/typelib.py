from PyQt6.QtWidgets import QMainWindow


class MainWindowUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.toolwindow = None
        self.state = "工作中"
        self.worktime = ["00","25"]
        self.resttime = ["00","5"]

