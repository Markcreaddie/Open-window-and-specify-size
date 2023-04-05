import pygetwindow

import monitor

#Notepad.txt file should be open

win = pygetwindow.getWindowsWithTitle('Notepad')[0]
#win.size = (640, 400)
win.maximize()
#win.move(-1000,100)

print(monitor.get_size())
