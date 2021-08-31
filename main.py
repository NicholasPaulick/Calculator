import tkinter as tk
import tkinter.font as tkFont

import numpy as np

class Calculator():
    #
    # Sets everything up on run
    #
    def __init__(self):
        #
        # STORES YOUR EQUATION
        #

        self.equation = ""

        #
        # Creates GUI Parts
        #

        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.Displayfont = tkFont.Font(family = "Lucida Grande", size=40)
        self.Buttonfont = tkFont.Font(family = "Lucida Grande", size=35)

        self.Frames()
        self.Display()
        self.Pack()
        
        #
        # Mainloop
        #
        self.root.mainloop()

    #
    # frames
    #
    def Frames(self):
        # Display Bar Frame
        self.dframe = tk.Frame(self.root)

        # Top row of numbers frame (7,8,9, /)
        self.tframe = tk.Frame(self.root)

        # Top Mid row of numbers frame (4, 5, 6, *)
        self.tmframe = tk.Frame(self.root)

        # Bottom Mid Row of numbers Frame (1, 2, 3, -)
        self.bmframe = tk.Frame(self.root)

        # Bottom Row of numbers frame (0, 00, ., +)
        self.bframe = tk.Frame(self.root)

        # = Button Frame
        self.fframe = tk.Frame(self.root)

        #packs the frames in order
        self.dframe.pack()
        self.tframe.pack()
        self.tmframe.pack()
        self.bmframe.pack()
        self.bframe.pack()
        self.fframe.pack()

    #
    # Different Buttons and Labels
    #
    def Display(self):
        # Display
        self.display = tk.Label(self.dframe, text = "Working on it rn", font = self.Displayfont)

        # Top Row
        self.seven = tk.Button(self.tframe, text = "7", font = self.Buttonfont, command=lambda : self.Store("7"))
        self.eight = tk.Button(self.tframe, text = "8", font = self.Buttonfont, command=lambda : self.Store("8"))
        self.nine = tk.Button(self.tframe, text = "9", font = self.Buttonfont, command=lambda : self.Store("9"))
        self.divide = tk.Button(self.tframe, text = "/", font = self.Buttonfont, command=lambda : self.Store("/"))

        # Top Mid Row
        self.four = tk.Button(self.tmframe, text = "4", font = self.Buttonfont, command=lambda : self.Store("4"))
        self.five = tk.Button(self.tmframe, text = "5", font = self.Buttonfont, command=lambda : self.Store("5"))
        self.six = tk.Button(self.tmframe, text = "6", font = self.Buttonfont, command=lambda : self.Store("6"))
        self.multipy = tk.Button(self.tmframe, text = "*", font = self.Buttonfont, command=lambda : self.Store("*"))

        # Bottom Mid Row
        self.one = tk.Button(self.bmframe, text = "1", font = self.Buttonfont, command=lambda : self.Store("1"))
        self.two = tk.Button(self.bmframe, text = "2", font = self.Buttonfont, command=lambda : self.Store("2"))
        self.three = tk.Button(self.bmframe, text = "3", font = self.Buttonfont, command=lambda : self.Store("3"))
        self.subtract = tk.Button(self.bmframe, text = "-", font = self.Buttonfont, command=lambda : self.Store("-"))

        # Bottom Row
        self.zero = tk.Button(self.bframe, text = "0", font = self.Buttonfont, command=lambda : self.Store("0"))
        self.zerotwo = tk.Button(self.bframe, text = "00", font = self.Buttonfont, command=lambda : self.Store("00"))
        self.dot = tk.Button(self.bframe, text = ".", font = self.Buttonfont, command=lambda : self.Store("."))
        self.add = tk.Button(self.bframe, text = "+", font = self.Buttonfont, command=lambda : self.Store("+"))

        # Functions Row
        self.equal = tk.Button(self.fframe, text = "=", font = self.Buttonfont, command=lambda : self.Calculate())
        self.clear = tk.Button(self.fframe, text = "C", font = self.Buttonfont, command=lambda : self.Store("C"))

    #
    # Packs the Buttons and Labels
    #
    def Pack(self):
        # Display Pack
        self.display.pack(pady=10)

        # Top Row Pack
        self.seven.pack(side=tk.LEFT, padx = 10, pady=10)
        self.eight.pack(side=tk.LEFT, padx = 10, pady=10)
        self.nine.pack(side=tk.LEFT, padx = 10, pady=10)
        self.divide.pack(side=tk.RIGHT, padx = 10, pady=10)

        # Top Mid Row Pack
        self.four.pack(side=tk.LEFT, padx = 10, pady=10)
        self.five.pack(side=tk.LEFT, padx = 10, pady=10)
        self.six.pack(side=tk.LEFT, padx = 10, pady=10)
        self.multipy.pack(side=tk.RIGHT, padx = 10, pady=10)

        # Bottom Mid Row Pack
        self.one.pack(side=tk.LEFT, padx = 10, pady=10)
        self.two.pack(side=tk.LEFT, padx = 10, pady=10)
        self.three.pack(side=tk.LEFT, padx = 10, pady=10)
        self.subtract.pack(side=tk.RIGHT, padx = 10, pady=10)

        # Bottom Row Pack
        self.zero.pack(side=tk.LEFT, padx = 10, pady=10)
        self.zerotwo.pack(side=tk.LEFT, padx = 10, pady=10)
        self.dot.pack(side=tk.LEFT, padx = 10, pady=10)
        self.add.pack(side=tk.RIGHT, padx = 10, pady=10)

        # Functions Row Pack
        self.clear.pack(side=tk.LEFT)
        self.equal.pack(side=tk.RIGHT)

    # 
    # Updates the variable holding the inputs and the display bar
    #
    def Store(self, val):
        #Checks to see if It needs to clear the variable and display or update it
        if val == "C":
            self.equation = ""
            self.display['text'] = "                         "
        else:
            self.equation = self.equation + val
            self.display['text'] = self.equation

    #
    # Runs the Calculation and displays it
    #
    def Calculate(self):
        # Solves the equation and puts it back into string form
        self.equation = str(eval(self.equation))

        # Auto rounds the answer if the decimal is longer that 3 places
        if len(self.equation) >= 8:
            self.equation = str(round(eval(self.equation), 3))

        # Displays the answer
        self.display['text'] = self.equation


# Calls the program to run
if True:
    try:
        Calculator()
    except:
        print("Something went wrong")
        exit()