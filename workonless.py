import datetime
import calendar
from threading import Timer
from tkinter import *
import time

# Constants
bigText = ('Future Rt', 50, 'bold')
smallText = ('Future Rt', 20, 'bold')
Fg = '#6aff00'
Bg = "#00001C"


class Clock(Frame):
    def __init__(self, parent):
        self.date = datetime.datetime.now()
        self.timer = Timer(1, self.update_time)
        Frame.__init__(self, parent)

        self.startButton = Button(self, text='Старт', bg=Bg, fg=Fg, bd=3, command=self.start_timer_button_click)
        self.startButton.grid(row=6, column=0)
        self.stopButton = Button(self, text='Стоп', bg=Bg, fg=Fg, bd=3, command=self.stop_timer_button_click)
        self.stopButton.grid(row=6, column=1)

        self.timeLabel = Label(self, font=bigText, fg=Fg, bg=Bg)
        self.timeLabel.grid(row=2, column=0, columnspan=3)
        self.dateLabel = Label(self, font=smallText, fg=Fg, bg=Bg)
        self.dateLabel.grid(row=3, column=0, columnspan=3)

        self.incSecondButton = Button(self, text='+', bg=Bg, fg=Fg, bd=3, width=2, command=lambda: self.inc_button_click('second'))
        self.incSecondButton.grid(row=0, column=2)
        self.incMinuteButton = Button(self, text='+', bg=Bg, fg=Fg, bd=3, width=2, command=lambda: self.inc_button_click('minute'))
        self.incMinuteButton.grid(row=0, column=1)
        self.incHourButton = Button(self, text='+', bg=Bg, fg=Fg, bd=3, width=2, command=lambda: self.inc_button_click('hour'))
        self.incHourButton.grid(row=0, column=0)
        self.incDayButton = Button(self, text='+', bg=Bg, fg=Fg, bd=3, width=2, command=lambda: self.inc_button_click('day'))
        self.incDayButton.grid(row=4, column=0)
        self.incMonthButton = Button(self, text='+', bg=Bg, fg=Fg, bd=3, width=2, command=lambda: self.inc_button_click('month'))
        self.incMonthButton.grid(row=4, column=1)
        self.incYearButton = Button(self, text='+', bg=Bg, fg=Fg, bd=3, width=2, command=lambda: self.inc_button_click('year'))
        self.incYearButton.grid(row=4, column=2)
        self.decSecondButton = Button(self, text='-', bg=Bg, fg=Fg, bd=3, width=2, command=lambda: self.dec_button_click('second'))
        self.decSecondButton.grid(row=1, column=2)
        self.decMinuteButton = Button(self, text='-', bg=Bg, fg=Fg, bd=3, width=2, command=lambda: self.dec_button_click('minute'))
        self.decMinuteButton.grid(row=1, column=1)
        self.decHourButton = Button(self, text='-', bg=Bg, fg=Fg, bd=3, width=2, command=lambda: self.dec_button_click('hour'))
        self.decHourButton.grid(row=1, column=0)
        self.decDayButton = Button(self, text='-', bg=Bg, fg=Fg, bd=3, width=2, command=lambda: self.dec_button_click('day'))
        self.decDayButton.grid(row=5, column=0)
        self.decMonthButton = Button(self, text='-', bg=Bg, fg=Fg, bd=3, width=2, command=lambda: self.dec_button_click('month'))
        self.decMonthButton.grid(row=5, column=1)
        self.decYearButton = Button(self, text='-', bg=Bg, fg=Fg, bd=3, width=2, command=lambda: self.dec_button_click('year'))
        self.decYearButton.grid(row=5, column=2)

        self.update_labels()

    def update_labels(self):
        self.dateLabel.config(text=self.date.strftime('%d.%m.%Y'))
        self.timeLabel.config(text=self.date.strftime('%H:%M:%S'))

    def update_time(self):
        self.update_labels()
        self.date += datetime.timedelta(seconds=1)
        self.timer = Timer(1, self.update_time)
        self.timer.start()

    def start_timer_button_click(self):
        self.timer.start()

    def stop_timer_button_click(self):
        self.timer.cancel()

    def inc_button_click(self, param):
        if param == 'second':
            self.date += datetime.timedelta(seconds=1)
        if param == 'minute':
            self.date += datetime.timedelta(minutes=1)
        if param == 'hour':
            self.date += datetime.timedelta(hours=1)
        if param == 'day':
            self.date += datetime.timedelta(days=1)
        if param == 'month':
            self.date += datetime.timedelta(days=calendar.monthrange(self.date.year, self.date.month)[-1])
        if param == 'year':
            if calendar.isleap(self.date.year) and self.date.month < 3:
                self.date += datetime.timedelta(days=366)
            else:
                self.date += datetime.timedelta(days=365)
        self.update_labels()

    def dec_button_click(self, param):
        if param == 'second':
            self.date -= datetime.timedelta(seconds=1)
        if param == 'minute':
            self.date -= datetime.timedelta(minutes=1)
        if param == 'hour':
            self.date -= datetime.timedelta(hours=1)
        if param == 'day':
            self.date -= datetime.timedelta(days=1)
        if param == 'month':
            self.date -= datetime.timedelta(days=calendar.monthrange(self.date.year, self.date.month)[-1])
        if param == 'year':
            if calendar.isleap(self.date.year) and self.date.month < 3:
                self.date -= datetime.timedelta(days=366)
            else:
                self.date -= datetime.timedelta(days=365)
        self.update_labels()


if __name__ == "__main__":
    win = Tk()
    win.geometry("500x260")
    win['bg'] = Bg
    win.title("Clock")
    win.resizable(False, False)

    Clock(win).pack(side='top', fill='both', expand=True)

    win.mainloop()