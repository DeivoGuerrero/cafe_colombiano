import ctypes
import time
import math

user32 = ctypes.windll.user32

radio = 20
time_step = 0.003
interval = 20

VK_SHIFT = 0x10
KEYEVENTF_KEYUP = 0x0002

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]


def get_mouse_position():
    pt = POINT()
    user32.GetCursorPos(ctypes.byref(pt))
    return pt.x, pt.y


def move_mouse(x, y):
    user32.SetCursorPos(int(x), int(y))


while True:
    x0, y0 = get_mouse_position()
    
    user32.keybd_event(VK_SHIFT, 0, 0, 0)  # presiona Shift
    time.sleep(0.1)
    user32.keybd_event(VK_SHIFT, 0, KEYEVENTF_KEYUP, 0)  # suelta Shift
    for angulo in range(0, 180, 5):
        rad = math.radians(angulo)
        x = x0 + radio * math.cos(rad)
        y = y0 + radio * math.sin(rad)
        move_mouse(x, y)
        time.sleep(time_step)

    time.sleep(interval)