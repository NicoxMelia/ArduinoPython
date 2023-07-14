from .State import *

class ErrorState(State):
    def drawPicture(self, frame):
        Label(frame, text="ERROR, DEVICE IS DISCONNECTED...").place(x="100", y="100")