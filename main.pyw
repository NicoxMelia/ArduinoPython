from tkinter import *
from loaderPackage import loader
from threading import Thread

root = Tk()
root.title("Python RFID")
frame = Frame(root)
frame.pack()
frame.config(width="1920", height="1080")
# label = Label(frame, text="hola perro")
# label.place(x="100", y="100")
loader = loader.Loader(frame)
loaderThread = Thread(target=loader.read)
loaderThread.start()
root.mainloop()
loader.leave()