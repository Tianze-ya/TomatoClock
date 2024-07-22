from typing import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QMainWindow
from . import clock
from PyQt6.QtMultimedia import QSoundEffect


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.full_window = None

        self.clock = clock.Ui_TomatoClock()
        self.clock.setupUi(self)

        self.time_timer = QTimer()
        self.time_timer.timeout.connect(self.time_update)

        self.state = "工作中"
        self.clock.pushButton.clicked.connect(self.push_button_clicked)

        self.effect = QSoundEffect()
        self.effect.setSource(QUrl.fromLocalFile("./sound/clock.wav"))
        self.effect.setVolume(1)

    def push_button_clicked(self):
        if self.clock.pushButton.text() == "开始":
            self.clock.pushButton.setText("暂停")
            self.clock.state.setText(self.state)
            self.start()
        else:
            self.clock.pushButton.setText("开始")
            self.clock.state.setText("暂停中")
            self.stop()

    def start(self):
        self.time_timer.start(1000)

    def stop(self):
        self.time_timer.stop()

    def time_update(self):
        now = self.clock.time.text().split(':')
        if self.state == "工作中":
            time_h = self.clock.worktime_h.text().zfill(2)
            time_m = self.clock.worktime_m.text().zfill(2)
        else:
            time_h = self.clock.resttime_h.text().zfill(2)
            time_m = self.clock.resttime_m.text().zfill(2)

        if is_end(now, [time_h, time_m]):
            self.effect.play()
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
        if self.full_window:
            self.full_window.update_time()

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
