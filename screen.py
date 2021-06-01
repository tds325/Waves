#!/usr/bin/python
#------------------Imports
import tkinter, tkinter.filedialog
import os
import matplotlib
matplotlib.use('TkAgg')
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

    time = np.arange(0, 10, 0.1)
    amplitude = np.sin(time)

    print(time)
    print(amplitude)

    fig, ax = plt.subplots(figsize=(5, 4))
    #line, = ax.plot([],[], lw = 3)

    ax.set_title('Wave function')
    ax.set_ylabel('Amplitude')
    ax.set_xlabel('Time')

    data = plt.plot(time, amplitude)
    plt.xlim([time.min(), time.max()])
    plt.ylim([amplitude.min() * y_axis_buffer_ratio, amplitude.max() * y_axis_buffer_ratio])
    #plt.xticks(np.arange(min(time), max(time) + 1, 1.0))
    #anim = matplotlib.animation.FuncAnimation(fig, animate, init_func=init, frames = 200, interval = 20, blit = True)

    canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master = root)
    line, = ax.plot(x, np.sin(x))
    print(line)
    #canvas.draw()
    canvas.get_tk_widget().pack()
    ani = matplotlib.animation.FuncAnimation(fig, animate, np.arange(1, 200), interval = 25, blit = False, cache_frame_data = True, fargs = (line, x))
    #plt.close()
    return (ani, line)

def update(root):
    time = np.arange(0, 10, 0.1)
    amplitude = np.sin(time + 9)
    data.xdata = time
    data.ydata = amplitude

    print(data.xdata)
    print(data.ydata)


def init():
    pass
    #line.set_data([],[])
    #return line

def animate(i, line, x):
    line.set_ydata(np.sin(x+i / 10.0))
    return line
    #x = np.linespace(0, 4, 1000)
    #y = np.sin(2 * np.pi * (x - 0.01 * i))
    #line.set_data(x, y)
    #return line

def main():

    fig = plt.Figure()
    x = np.arange(0, 2*np.pi, 0.01)

    root = tkinter.Tk()
    root.resizable(False, False)
    root.wm_attributes("-topmost", 1)
    gui = tkinterGUI(root)

    gui.initialize_canvases(root)
    ani, line = plot(gui.canvas, x)
    print(ani)
    def animate(i):
        line.set_ydata(np.sin(x + i/10.0))
        return line

    #root.after(16, update(root))
    root.mainloop()

    quit()

if __name__ == '__main__':
    main()
