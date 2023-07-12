from abc import ABC, abstractmethod
from tkinter import *

class State(ABC):
    @abstractmethod
    def drawPicture():
        pass
    