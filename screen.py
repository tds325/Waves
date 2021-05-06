#!/usr/bin/python

import tkinter, tkinter.filedialog
import os

ROOT_DIR = os.path.dirname(os.path.abspath("screen.py"))
os.chdir("..")

class tkinterGUI:

    # window is the parent widget
    def __init__(self, window):
        # golden ratio
        ratio = 1.618

        self.canvas_width = 970
        self.canvas_height = round(self.canvas_width / ratio)

        self.window = window
        window.title("Waves")
        window.geometry(f"{self.canvas_width}x{self.canvas_height}+10+10")

        self.wavecanvas = tkinter.Canvas(window, bg="black", \
        width= self.canvas_width, height = self.canvas_height, highlightbackground = "black")
        self.wavecanvas.place(relx = "0", rely = "0")

        self.canvas = tkinter.Canvas(window, bg="LightSteelBlue3", \
        width=self.canvas_width/2,height = self.canvas_height/3)

        #dividing to balance second canvas in the middle
        x_ratio = ((self.canvas_width) / self.canvas_width)/4
        y_ratio = ((self.canvas_height) / self.canvas_height)/6

        self.canvas.place(relx = f"{x_ratio}", x = "0", rely = f"{y_ratio}")

        filename = overwrite_bitmap(self.canvas_width, self.canvas_height)
        bitmap = os.path.join(ROOT_DIR, filename)

        print(f"bitmap: {bitmap}")

        self.bitmap = self.canvas.create_bitmap("0", "0", anchor = "w", \
        bitmap = f"@{bitmap}")

def overwrite_bitmap(width, height):
    print(f"{width}\n{height}")
    filename = "bitmap.xbm"
    file = open(f"{ROOT_DIR}\{filename}", "w")
    file.write(f'#define im_width {width}\n#define im_height {height}\n\
static char im_bits[] = {{\n')
    ans = write_bitmap_lines(width, height)
    file.write(f"{ans}}};")
    file.close()

    return filename

def write_bitmap_lines(width, height):
    file_write = ""
    count = 0
    term = width * height

    while(count < term - 1):
        if((count + 1) % 16 == 0):
            file_write += "0x00, \n"
        else:
            file_write += "0x00, "
        count += 1
    file_write += "0x00 "

    return file_write


def main():

    root = tkinter.Tk()
    root.resizable(False, False)
    gui = tkinterGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
