#!/usr/bin/python
#------------------Imports
import tkinter, tkinter.filedialog
import os
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np
#------------------End of Imports

data = matplotlib.lines.Line2D
anim = matplotlib.animation.FuncAnimation

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
#
        #dividing to balance second canvas in the middle
        x_ratio = ((self.canvas_width) / self.canvas_width)/4
        y_ratio = ((self.canvas_height) / self.canvas_height)/6
        self.canvas.place(relx = f"{x_ratio}", x = "0", rely = f"{y_ratio}")

# implements matplotlib onto tkinter gui
def plot(root, x):

    y_axis_buffer_ratio = 11/10

    time = np.arange(0, 2 * np.pi, 0.01)
    amplitude = np.sin(time)

    fig, ax = plt.subplots(figsize=(5, 4))

    ax.set_title('Wave function')
    ax.set_ylabel('Amplitude')
    ax.set_xlabel('Time')

    plt.xlim([time.min(), time.max()])
    plt.ylim([amplitude.min() * y_axis_buffer_ratio, amplitude.max() * y_axis_buffer_ratio])

    canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master = root)
    line, = ax.plot(x, np.sin(x))

    canvas.get_tk_widget().pack()
    ani = matplotlib.animation.FuncAnimation(fig, animate, np.arange(1, 200), interval = 25, blit = False, cache_frame_data = True, fargs = (line, x))

    return (ani, line)

#def update(root):
#    time = np.arange(0, 10, 0.1)
#    amplitude = np.sin(time + 9)
#    data.xdata = time
#    data.ydata = amplitude
#
#    print(data.xdata)
#    print(data.ydata)

def animate(i, line, x):
    line.set_ydata(np.sin(x+i / 10.0))
    return line

def end():
    quit()

def main():

    fig = plt.Figure()
    x = np.arange(0, 2*np.pi, 0.01)

    root = tkinter.Tk()
    root.resizable(False, False)
    root.wm_attributes("-topmost", 1)
    root.protocol("WM_DELETE_WINDOW", end)
    gui = tkinterGUI(root)

    gui.initialize_canvases(root)
    ani, line = plot(gui.canvas, x)

    def animate(i):
        line.set_ydata(np.sin(x + i/10.0))
        return line

    root.mainloop()
    plt.close('all')
    quit()

if __name__ == '__main__':
    main()
