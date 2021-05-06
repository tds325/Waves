#!/usr/bin/python

import tkinter

class tkinterGUI:

    def __init__(self, window):
        ratio = 1.618

        self.canvas_width = 970
        self.canvas_height = round(self.canvas_width / ratio)

        self.window = window
        window.title("Waves")
        window.geometry(f"{self.canvas_width}x{self.canvas_height}+10+10")
        #window is the parent widget

        self.wavecanvas = tkinter.Canvas(window, bg="black", \
        width= self.canvas_width, height = self.canvas_height, highlightbackground = "black")
        self.wavecanvas.place(relx = "0", rely = "0")

        self.canvas = tkinter.Canvas(window, bg="white", \
        width=self.canvas_width/2,height = self.canvas_height/3)

        #dividing to balance second canvas in the middle
        x_ratio = ((self.canvas_width) / self.canvas_width)/4
        y_ratio = ((self.canvas_height) / self.canvas_height)/6

        self.canvas.place(relx = f"{x_ratio}",x = "0", rely = f"{y_ratio}")

def main():

    root = tkinter.Tk()
    root.resizable(False, False)
    gui = tkinterGUI(root)
    #root.config(highlightbackground = "black")
    #add widgets between here and mainloop

    #widget = tkinter.Canvas(window, bg="black",height=canvas_height,width=canvas_width)

    root.mainloop()


if __name__ == '__main__':
    main()
