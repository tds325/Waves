#!/usr/bin/python

import tkinter, tkinter.filedialog
import os
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

#import logging
#logging.debug("hello there")

ROOT_DIR = os.path.dirname(os.path.abspath("screen.py"))
os.chdir("..")

class tkinterGUI:

    # window class is the parent (root) widget for tkinter library
    def __init__(self, window):
        # golden ratio magic number for reference
        ratio = 1.618
        # magic number TODO - make window resizable
        self.canvas_width = 970
        self.canvas_height = round(self.canvas_width / ratio)
        self.wavecanvas_width = self.canvas_width / 2
        self.wavecanvas_height = self.canvas_height / 3

        #print(self.__dict__)

        self.initialize_canvases(window)
        plot(self.canvas)

        #self.initialize_bitmap(window)


    def initialize_canvases(self, window):
        # gui window properties
        self.window = window
        window.title("Waves")
        window.geometry(f"{self.canvas_width}x{self.canvas_height}+10+10")

        # black background window
        self.wavecanvas = tkinter.Canvas(window, bg="black", \
        width= self.canvas_width, height = self.canvas_height, highlightbackground = "black")
        self.wavecanvas.place(relx = "0", rely = "0")

        # smaller window
        self.canvas = tkinter.Canvas(window, bg="LightSteelBlue3", \
        width=self.wavecanvas_width,height = self.wavecanvas_height)

        #dividing to balance second canvas in the middle
        x_ratio = ((self.canvas_width) / self.canvas_width)/4
        y_ratio = ((self.canvas_height) / self.canvas_height)/6
        self.canvas.place(relx = f"{x_ratio}", x = "0", rely = f"{y_ratio}")

def plot(root):
    time = np.arange(0, 10, 0.1)
    amplitude = np.sin(time)

    fig, ax = plt.subplots(figsize=(5, 3))
    print(type(fig))
    print(type(ax))
    ax.box_aspect = 1.612
    plot = fig.add_subplot()
    plt.plot(time, amplitude)

    #plot.xlabel('Time')
    #plot.ylabel('Amplitude')
    #plot.grid(True, which = 'both')
    #plot.axhline(y = 0, color = 'k')
    #plot.show()
    
    canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master = root)
    canvas.draw()
    canvas.get_tk_widget().pack()
    plt.close()


    #fig = plt.Figure(figsize = (5, 2.5), dpi = 100)
    #plot1 = fig.add_subplot(111)
    #y = [np.cos(i) for i in range(int(2*np.pi))]
    #plot1.plot(y)
    #canvas =  matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master = root)
    #canvas.draw()

    #canvas.get_tk_widget().pack()

    #toolbar =  matplotlib.backends.backend_tkagg.NavigationToolbar2Tk(canvas, root)
    #toolbar.update()

    #canvas.get_tk_widget().pack()

def main():

    root = tkinter.Tk()
    root.resizable(False, False)

    gui = tkinterGUI(root)
    root.mainloop()
    quit()
    #root.destroy()
    #plt.close()

if __name__ == '__main__':
    main()



    #def initialize_bitmap(self, window):
        # 'overwrite_bitmap' returns the file name of the bitmap
        #filename = overwrite_bitmap(self.canvas_width, self.canvas_height)

        # filename of bitmap found using os - Root directory -> xbm file
        #bitmap = os.path.join(ROOT_DIR, filename)

        #print(f"bitmap: {bitmap}")

        # bitmap created in tkinter using its 'create_bitmap' method
        #self.bitmap = self.canvas.create_bitmap("0", "0", anchor = "w", \
        #bitmap = f"@{bitmap}", background = "green")

# after writing initial bitmap boilerplate, loops through and writes each
# '0xXX' term to be displayed in the file - returns the string to be written
# in the bitmap file in object
#def overwrite_bitmap(width, height):
    # print(f"{width}\n{height}")
    #filename = "bitmap.xbm"
    #file = open(f"{ROOT_DIR}\{filename}", "w")

    #file.write(f'#define im_width {width}\n#define im_height {height}\n\
#static char im_bits[] = {{\n')

    #ans = write_bitmap_lines(width, height)
    #file.write(f"{ans}}};")

    #file.close()

    #return filename

# given the width and height of the bitmap, return a string of the bitmap
# values to be written in the xbm file
#def write_bitmap_lines(width, height):
    #width=485
    #height=200
    #print(f"\twidth: {width}\n\theight: {height}")
    #file_write = ""
    #count = 0
    #innercount = 0
    #term = 73200

    #test = "0x01, 0x03, 0x07, 0x0f, 0x1f, 0x3f, 0x7f, 0xff, "
    #for count in range(int(term / 8) - 1):
        #for innercount in range(8):
            #count += 1
        #file_write += test

    #file_write += "0x00, "
    #file_write += "0x00, "
    #file_write += "0x00, "
    #file_write += "0x00, "
    #file_write += "0x00, "
    #file_write += "0x00, "
    #file_write += "0x00, "
    #file_write += "0x00 "
    #print(f"\tcount: {count}")
    #return file_write
