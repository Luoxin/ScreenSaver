import subprocess
import sys
from ctypes import *


if sys.platform == 'win32':
    class LASTINPUTINFO(Structure):
      _fields_ = [
       ('cbSize', c_uint),
       ('dwTime', c_int),
      ]
    def get_idle_duration():
        lastInputInfo = LASTINPUTINFO()
        lastInputInfo.cbSize = sizeof(lastInputInfo)
        if windll.user32.GetLastInputInfo(byref(lastInputInfo)):
            millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
            return millis / 1000.0
        else:
            return 0
else:
    def get_idle_duration():
        return 0

def run():

    p = subprocess.Popen("python ScreenSaver.py", shell=True)
    p.wait()
    # from ScreenSaver import ScreenSaver
    # try:
    #     i = open(".\setting.ini", "r")
    #     num = int(i.readline())
    #     i.close()
    #     if num > 50:
    #         num = 50
    #     print(num)
    #     a = ScreenSaver()
    #     a.run(num)
    #     print("successful")
    # except:
    #     a = ScreenSaver()
    #     a.run(18)

if __name__ == '__main__':
    while True:
        duration = get_idle_duration()
        if duration >= 300:
            # pass
            run()
        else:
            print(duration)
      # print('User idle for %.2f seconds.' % duration,time.sleep(1))