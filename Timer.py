import time


class Timer(object):

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def countDown(self):
        count = 0
        while self.hours or self.minutes or self.seconds != 0:
            if self.hours - 9 < 1:
                hours = "0" + str(self.hours)
            else:
                hours = str(self.hours)
            if self.minutes - 9 < 1:
                minutes = "0" + str(self.minutes)
            else:
                minutes = str(self.minutes)
            if self.seconds - 9 < 1:
                seconds = "0" + str(self.seconds)
            else:
                seconds = str(self.seconds)
            time_remaining = hours + ":" + minutes + ":" + seconds
            print(time_remaining)
            if self.seconds == 0 and (self.minutes != 0 or self.hours != 0):
                self.seconds = 59
                count = 0
                if self.minutes != 0:
                    self.minutes -= 1
                else:
                    self.minutes = 59
                    self.hours -= 1
            else:
                self.seconds -= 1
            time.sleep(1)
        print("Times up!")

timer = Timer(0, 0, 3)
timer.countDown()
