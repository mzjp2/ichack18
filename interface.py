import time

from tkinter.filedialog import askopenfilename
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Team SSA Image to Playlist"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="Upload Image", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("Made by Christopher Smith, Joe Rosenberg, Khalid Hassan and Zain Patel")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
filename = askopenfilename()