from .State import *

class MoonState(State):
    def drawPicture(self, frame):
        self.width = frame.winfo_width()
        self.height = frame.winfo_height()
        self.aux = Image.open("moon3.png").resize((self.width, self.height), Image.CONTAINER)
        self.imagen = ImageTk.PhotoImage(self.aux)
        Label(frame, image=self.imagen).place(x="0", y="0")