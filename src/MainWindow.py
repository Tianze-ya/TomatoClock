from typing import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QMainWindow
from . import clock
from src.ToolWindow import ToolWindowUI
from PyQt6.QtMultimedia import QSoundEffect


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.time_m = None
        self.time_h = None

        self.clock = clock.Ui_TomatoClock()
        self.clock.setupUi(self)

        self.clock.toolButton.clicked.connect(self.tool_button_clicked)

        self.time_timer = QTimer()
        self.time_timer.timeout.connect(self.time_update)

        self.state = "工作中"
        self.clock.pushButton.clicked.connect(self.push_button_clicked)

    def push_button_clicked(self):
        if self.clock.pushButton.text() == "开始":
            self.clock.pushButton.setText("暂停")
            self.clock.state.setText(self.state)
            self.start()
        else:
            self.clock.pushButton.setText("开始")
            self.clock.state.setText("暂停中")
            self.stop()

    def tool_button_clicked(self):
        toolwindow = ToolWindowUI(self)
        toolwindow.show()

    def start(self):
        self.time_timer.start(1000)

    def stop(self):
        self.time_timer.stop()

    def time_update(self):
        now = self.clock.time.text().split(':')

        if is_end(now, [self.time_h, self.time_m]):
            effect = QSoundEffect()
            effect.setSource(QUrl.fromLocalFile("./sound/clock.wav"))
            effect.setVolume(1)
            effect.play()
            self.stop()
            self.time_to_zero()
            if self.state == "工作中":
                self.state = "休息中"
            else:
                self.state = "工作中"
            self.clock.state.setText(self.state)
            self.start()
        else:
            self.clock.time.setText(sec_next(now))
    def time_to_zero(self):
        self.clock.time.setText("00:00:00")


def sec_next(time_a: List[str]) -> str:
    time = time_a
    if time[2] == "59":
        time[2] = "00"
        time[1] = str(int(time[1]) + 1).zfill(2)
    else:
        time[2] = str(int(time[2]) + 1).zfill(2)
    if time[1] == "60":
        time[1] = "00"
        time[0] = str(int(time[0]) + 1).zfill(2)
    time = ":".join(time)
    return time


def is_end(now: List[str], time: List[str]) -> bool:
    if now[:-1] == time:
        return True
    else:
        return False
