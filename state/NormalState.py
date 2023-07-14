from .State import *

class NormalState():
    def drawPicture(self, frame):
        self.drawText(frame)
        
    def drawText(self, frame):
        text = Label(frame, text="Insert an RFID card...")
        text.place(x="100", y="100")