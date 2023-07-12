from .State import *

class SaturnoState(State):
    def drawPicture(self, frame):
        self.imagen = PhotoImage(file="saturno.png")
        Label(frame, image=self.imagen).place(x="0", y="0")