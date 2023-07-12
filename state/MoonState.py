from .State import *

class MoonState(State):
    def drawPicture(self, frame):
        self.imagen = PhotoImage(file="moon3.png")
        Label(frame, image=self.imagen).place(x="0", y="0")