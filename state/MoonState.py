from .State import *

class MoonState(State):
    def drawPicture(self, frame):
        imagen = PhotoImage(file="moon3.png")
        Label(frame, image=imagen).place(x="0", y="0")
        # self.drawText(frame)

    # def drawText(self, frame):
    #     text = Label(frame, text="prueba de texto")
    #     text.place(x="100", y="100")