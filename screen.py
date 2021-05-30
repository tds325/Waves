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

    y_axis_buffer_ratio = 11/10
    time = np.arange(0, 10, 0.1)
    amplitude = np.sin(time)
    #print(time)
    #print(amplitude)

    fig, ax = plt.subplots(figsize=(5, 4))

    ax.set_title('Wave function')
    ax.set_ylabel('Amplitude')
    ax.set_xlabel('Time')

    print(type(fig))
    print(type(ax))


    plt.plot(time, amplitude)


    plt.xlim([time.min(), time.max()])
    plt.ylim([amplitude.min() * y_axis_buffer_ratio, amplitude.max() * y_axis_buffer_ratio])
    plt.xticks(np.arange(min(time), max(time) + 1, 1.0))

    canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master = root)
    canvas.draw()
    canvas.get_tk_widget().pack()

    plt.close()

def main():

    root = tkinter.Tk()
    root.resizable(False, False)

    gui = tkinterGUI(root)
    root.mainloop()
    quit()

if __name__ == '__main__':
    main()
