from typing import *
from PyQt6.QtCore import *
from . import clock
from src.typelib import *
from src.ToolWindow import ToolWindowUI
from playsound import playsound


class MainWindow(MainWindowUI):
    def __init__(self) -> None:
        super().__init__()

        self.clock = clock.Ui_TomatoClock()
        self.clock.setupUi(self)

        self.time_timer = QTimer()
        self.time_timer.timeout.connect(self.time_update)
        
        self.clock.toolButton.clicked.connect(self.tool_button_clicked)
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
        self.toolwindow = ToolWindowUI(self)
        self.toolwindow.show()

    def time_update(self):
        now = self.clock.time.text().split(':')
        if self.parent.state == "工作中":
            time = self.worktime
        else:
            time = self.resttime
        if is_end(now, time):
            self.stop()
            self.time_to_zero()
            playsound("./clock.wav")
            if self.state == "工作中":
                self.state = "休息中"
            else:
                self.state = "工作中"
            self.clock.state.setText(self.state)
            self.start()
        else:
            self.clock.time.setText(sec_next(now))

    def start(self):
        self.time_timer.start(1000)

    def stop(self):
        self.time_timer.stop()

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
