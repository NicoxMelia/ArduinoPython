from .State import *

class NormalState(State):
    def drawPicture(self, frame):
        # imagen = PhotoImage(file=source)
        # Label(frame, image=imagen).place(x="0", y="0")
        self.drawText(frame)
        
    def drawText(self, frame):
        text = Label(frame, text="Inserte una tarjeta...")
        text.place(x="100", y="100")