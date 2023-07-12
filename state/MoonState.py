from .State import *

class MoonState(State):
    def drawPicture(self, frame):
        self.source = "..."
        imagen = PhotoImage(file=self.source)
        Label(frame, image=imagen).place(x="0", y="0")