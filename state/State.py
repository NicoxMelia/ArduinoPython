from abc import ABC, abstractmethod
from tkinter import *
from PIL import Image, ImageTk

class State(ABC):
    @abstractmethod
    def drawPicture(self, frame):
        pass
    