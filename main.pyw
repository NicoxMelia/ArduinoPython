from tkinter import *
from loaderPackage import loader
from threading import Thread

root = Tk()
root.title("Python RFID")
frame = Frame(root)
frame.pack(fill="both", expand="True")
frame.config(width="640", height="480")
loader = loader.Loader(frame)
loaderThread = Thread(target=loader.read)
loaderThread.start()
root.mainloop()
loader.leave()