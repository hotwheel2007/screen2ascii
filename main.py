from PIL import Image
from mss import mss
import image2ascii

def capture_screenshot(monitor):
    with mss() as sct:
        monitor = sct.monitors[monitor]
        sct_img = sct.grab(monitor)
        return Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')

def get_frame(res, display):
    frame = capture_screenshot(display)
    frame = frame.resize([res, int(res / frame.width * frame.height)])
    frame = frame.convert("L")
    frame_load = frame.load()
    return [frame, frame_load]

def draw_frame(res, display):
    frame = get_frame(res, display)
    ascii_img = image2ascii.convert(frame[0], frame[1])
    for i in range(0, 1024):
        print("")
    for row in ascii_img:
        print(row)


resolution = int(input("Output width (176 is recommended): "))
display = int(input("Display to convert to ASCII (Use 1 for primary display): "))

while True:
    draw_frame(resolution, display)
    print("")
    print("screen2ascii v1.0 by hw2007")
